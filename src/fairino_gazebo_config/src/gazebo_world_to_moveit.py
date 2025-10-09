#!/usr/bin/env python3
import os
import math
import sys
import xml.etree.ElementTree as ET

import rclpy
from rclpy.node import Node
from moveit_msgs.msg import CollisionObject, PlanningScene
from moveit_msgs.srv import ApplyPlanningScene
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

        models = self.parse_world(world_file)
        self.get_logger().info(f'Found {len(models)} models.')

        # Connect to MoveIt
        self.cli = self.create_client(ApplyPlanningScene, '/apply_planning_scene')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /apply_planning_scene service...')

        # Build PlanningScene diff
        ps = PlanningScene()
        ps.is_diff = True
        for model in models:
            co = self.create_collision_object(model)
            if co:
                ps.world.collision_objects.append(co)

        # Apply Planning Scene
        req = ApplyPlanningScene.Request(scene=ps)
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('✅ All collision objects added to MoveIt!')
        else:
            self.get_logger().error('❌ Failed to apply planning scene.')

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
                print(size)
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

                mesh = trimesh.load(mesh_path, force='mesh')
                mesh.apply_scale(scale)

                # --- Simplify Mesh ---
                original_faces = len(mesh.faces)
                target_faces = max(500, int(original_faces * 0.2))  # keep 20% or at least 500 faces

                try:
                    simplified = mesh.simplify_quadratic_decimation(target_faces)
                    if simplified and len(simplified.faces) < original_faces:
                        self.get_logger().info(
                            f"Mesh '{model['name']}' simplified {original_faces} → {len(simplified.faces)} faces"
                        )
                        mesh = simplified
                    else:
                        self.get_logger().info(f"Mesh '{model['name']}' simplification skipped (already small)")
                except Exception as e:
                    self.get_logger().warn(f"Simplification failed for '{model['name']}': {e}")
                    mesh = mesh.convex_hull
                    self.get_logger().info(f"Used convex hull instead for '{model['name']}'")

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
