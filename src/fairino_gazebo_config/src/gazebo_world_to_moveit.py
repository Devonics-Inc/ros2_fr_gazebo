#!/usr/bin/env python3
import os
import math
import sys
import xml.etree.ElementTree as ET

from ollama import ps

import rclpy
from rclpy.node import Node
from moveit_msgs.msg import CollisionObject, PlanningScene, AllowedCollisionEntry, AllowedCollisionMatrix
from moveit_msgs.srv import ApplyPlanningScene, GetPlanningScene
from shape_msgs.msg import SolidPrimitive, Mesh, MeshTriangle
from geometry_msgs.msg import Pose, Point

import trimesh  # pip install trimesh


def rpy_to_quaternion(roll, pitch, yaw):
    qx = math.sin(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) - math.cos(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
    qy = math.cos(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2)
    qz = math.cos(roll / 2) * math.cos(pitch / 2) * math.sin(yaw / 2) - math.sin(roll / 2) * math.sin(pitch / 2) * math.cos(yaw / 2)
    qw = math.cos(roll / 2) * math.cos(pitch / 2) * math.cos(yaw / 2) + math.sin(roll / 2) * math.sin(pitch / 2) * math.sin(yaw / 2)
    return qx, qy, qz, qw


class WorldToMoveIt(Node):
    def __init__(self, world_file):
        super().__init__('gazebo_world_to_moveit')
        self.get_logger().info(f'Parsing world file: {world_file}')
        self.models_path = os.getenv("GAZEBO_MODEL_PATH", "/usr/share/gazebo/models")

        # 1. Parse models from SDF
        models = self.parse_world(world_file)

        # 2. Setup Clients
        self.cli = self.create_client(ApplyPlanningScene, '/apply_planning_scene')
        self.get_scene_cli = self.create_client(GetPlanningScene, '/get_planning_scene')
        
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for services...')

        # 3. FETCH current scene to get the existing Allowed Collision Matrix (ACM)
        scene_req = GetPlanningScene.Request()
        scene_req.components.components = 0
        
        future_scene = self.get_scene_cli.call_async(scene_req)
        rclpy.spin_until_future_complete(self, future_scene)
        
        # This is the "Master" ACM that MoveIt currently knows about
        acm = future_scene.result().scene.allowed_collision_matrix

        # Get planning scene
        ps = PlanningScene()
        ps.is_diff = True


        # ADD ROBOT LINKS TO BE IGNORED HERE
        link_names = ["base_link", "rail_carriage"]
        
        # Loop through models in world and add to planning scene
        for model in models:
            co = self.create_collision_object(model)
            if co:
                ps.world.collision_objects.append(co)
                
                if "ground" in model['name'].lower():
                    for link in link_names:
                        self.update_acm(acm, model['name'], link, True)

        # Apply allowed collision matrix
        ps.allowed_collision_matrix = acm

        # Uppdate planning scene
        req = ApplyPlanningScene.Request(scene=ps)
        future_apply = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future_apply)
        
        self.get_logger().info('✅ Scene and ACM updated.')

    def update_acm(self, acm, name1, name2, enabled):
        """Ensures both names exist in ACM and sets their collision status."""
        for name in [name1, name2]:
            if name not in acm.entry_names:
                acm.entry_names.append(name)
                # Add a new column to all existing rows
                for entry in acm.entry_values:
                    entry.enabled.append(False)
                # Add the new row itself
                new_row = AllowedCollisionEntry(enabled=[False] * len(acm.entry_names))
                acm.entry_values.append(new_row)

        idx1 = acm.entry_names.index(name1)
        idx2 = acm.entry_names.index(name2)
        acm.entry_values[idx1].enabled[idx2] = enabled
        acm.entry_values[idx2].enabled[idx1] = enabled

    def set_acm_for_object(self, acm, obj, other=None, enabled=False):
        """Updates the MoveIt PlanningScene using the AllowedCollisionMatrix to ignore collisions for an object"""
        if other is None:
            self.set_acm_default_for_object(acm, obj, enabled)
            return

        other_idx = acm.entry_names.index(other)
        if obj not in acm.entry_names:
            acm.entry_names.append(obj)
            for entry in acm.entry_values:
                entry.enabled.append(enabled)
            acm.entry_values.append(AllowedCollisionEntry(enabled=[enabled for i in range(len(acm.entry_names))]))
            acm.entry_values[-1].enabled[other_idx] = enabled
        else:
            obj_idx = acm.entry_names.index(obj)
            acm.entry_values[obj_idx].enabled[other_idx] = enabled
            acm.entry_values[other_idx].enabled[obj_idx] = enabled

    def set_acm_default_for_object(self,acm, obj, enabled=False):
        if obj not in acm.default_entry_names:
            acm.default_entry_names.append(obj)
            acm.default_entry_values.append(enabled)
        else:
            idx = acm.default_entry_names.index(obj)
            acm.default_entry_values[idx] = enabled
    # ------------------- PARSE WORLD -------------------

    def parse_world(self, world_file):
        tree = ET.parse(world_file)
        root = tree.getroot()
        models = []

        for model in root.findall('.//model'):
            name = model.attrib.get('name', 'unnamed')
            pose_text = model.findtext('pose', default='0 0 0 0 0 0')
            px, py, pz, rr, pp, yy = map(float, pose_text.split())

            geom = model.find('.//geometry')
            if geom is None:
                continue

            shape, data = None, {}

            if geom.find('box') is not None:
                shape = 'box'
                size = list(map(float, geom.findtext('box/size', '0.1 0.1 0.1').split()))
                data['size'] = size

            elif geom.find('sphere') is not None:
                shape = 'sphere'
                data['radius'] = float(geom.findtext('sphere/radius', '0.05'))

            elif geom.find('cylinder') is not None:
                shape = 'cylinder'
                data['radius'] = float(geom.findtext('cylinder/radius', '0.05'))
                data['length'] = float(geom.findtext('cylinder/length', '0.1'))

            ##### Treat ellipsoid as boxes #####
            elif geom.find('ellipsoid') is not None:
                shape = 'box'
                size = list(map(float, geom.findtext('ellipsoid/radii', '0.1 0.1 0.1').split()))
                for i in range(len(size)):
                    size[i] = size[i] * 2
                data['size'] = size

            ##### Treat capsules as cylinders #####
            elif geom.find('capsule') is not None:
                shape = 'cylinder'
                data['radius'] = float(geom.findtext('capsule/radius', '0.05'))
                data['length'] = float(geom.findtext('capsule/length', '0.1'))
                data['length'] += data['radius'] * 2

            elif geom.find('plane') is not None:
                shape = 'plane'
                data['size'] = [10.0, 10.0, 0.01]

            elif geom.find('mesh') is not None:
                shape = 'mesh'
                uri = geom.findtext('mesh/uri', '')
                scale = list(map(float, geom.findtext('mesh/scale', '1 1 1').split()))
                data['uri'] = self.resolve_uri(uri)
                data['scale'] = scale

            elif geom.find('heightmap') is not None:
                shape = 'heightmap'
                data['size'] = [5.0, 5.0, 0.1]



            else:
                self.get_logger().warn(f"Unsupported geometry type in model '{name}'")
                continue

            models.append({
                'name': name,
                'shape': shape,
                'data': data,
                'pose': (px, py, pz, rr, pp, yy)
            })
            
        return models

    def resolve_uri(self, uri):
        if uri.startswith('file://'):
            return uri.replace('file://', '')
        elif uri.startswith('model://'):
            rel_path = uri.replace('model://', '')
            return os.path.join(self.models_path, rel_path)
        else:
            return uri

    # ------------------- BUILD COLLISION OBJECTS -------------------

    def create_collision_object(self, model):
        co = CollisionObject()
        co.id = model['name']
        co.header.frame_id = 'world'
        co.operation = CollisionObject.ADD

        px, py, pz, rr, pp, yy = model['pose']
        pose = Pose()
        pose.position.x = px
        pose.position.y = py
        pose.position.z = pz
        pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w = rpy_to_quaternion(rr, pp, yy)

        shape = model['shape']
        data = model['data']

        try:
            if shape == 'box':
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.BOX
                prim.dimensions = data['size']
                co.primitives.append(prim)
                co.primitive_poses.append(pose)

            elif shape == 'sphere':
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.SPHERE
                prim.dimensions = [data['radius']]
                co.primitives.append(prim)
                co.primitive_poses.append(pose)

            elif shape == 'cylinder':
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.CYLINDER
                prim.dimensions = [data['length'], data['radius']]
                co.primitives.append(prim)
                co.primitive_poses.append(pose)

            elif shape == 'plane' or shape == 'heightmap':
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.BOX
                prim.dimensions = data['size']
                co.primitives.append(prim)
                co.primitive_poses.append(pose)

            elif shape == 'mesh':
                mesh_path = data['uri']
                scale = data.get('scale', [1.0, 1.0, 1.0])

                if not os.path.exists(mesh_path):
                    self.get_logger().warn(f"Mesh file not found: {mesh_path}")
                    return None

                # --- Load FULL mesh (no simplification) ---
                try:
                    mesh = trimesh.load(mesh_path, force='mesh')

                    # Apply scaling exactly as in the SDF
                    mesh.apply_scale(scale)

                    self.get_logger().info(
                        f"Loaded mesh '{model['name']}' fully: "
                        f"{len(mesh.vertices)} vertices, {len(mesh.faces)} triangles"
                    )

                except Exception as e:
                    self.get_logger().error(f"Failed to load mesh '{model['name']}': {e}")
                    return None

                # Convert full mesh to shape_msgs/Mesh
                moveit_mesh = self.trimesh_to_shape_msgs(mesh)

                co.meshes.append(moveit_mesh)
                co.mesh_poses.append(pose)

        except Exception as e:
            self.get_logger().error(f"Error creating CollisionObject for {model['name']}: {e}")
            return None

        return co

    def trimesh_to_shape_msgs(self, mesh):
        msg = Mesh()
        for face in mesh.faces:
            tri = MeshTriangle()
            tri.vertex_indices = [int(i) for i in face]
            msg.triangles.append(tri)
        for vertex in mesh.vertices:
            pt = Point()
            pt.x, pt.y, pt.z = map(float, vertex)
            msg.vertices.append(pt)
        return msg


def main(args=None):
    rclpy.init(args=args)
    if len(sys.argv) < 2:
        print("Usage: ros2 run <package> <node> -- <world_file.sdf>")
        sys.exit(1)

    world_file = sys.argv[1]
    if not os.path.isfile(world_file):
        world_file = os.path.join('/usr/share/ignition/ignition-gazebo6/worlds', world_file)

    node = WorldToMoveIt(world_file)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
