#!/usr/bin/env python3
"""
gazebo_to_moveit_obstacles/node/extract_and_publish.py

ROS2 Humble node that:
 - queries Gazebo (classic) for model list + poses
 - finds model SDF/mesh files in GAZEBO_MODEL_PATH / common locations
 - converts primitives to moveit_msgs/CollisionObject
 - for meshes: attempts a minimal STL reader to compute bounding box and publishes that box (conservative)
 - publishes a PlanningScene diff to the `planning_scene` topic

Usage:
  ros2 run gazebo_to_moveit_obstacles extract_and_publish.py
(or add an entry point in setup.py)
"""

import os
import sys
import struct
import math
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Optional, Tuple
import ignition.transport
import rclpy
from rclpy.node import Node

# Gazebo services (classic)
from gazebo_msgs.srv import GetWorldProperties, GetModelState

# MoveIt + geometry msgs
from moveit_msgs.msg import CollisionObject, PlanningScene
from shape_msgs.msg import SolidPrimitive, Mesh, MeshTriangle
from geometry_msgs.msg import Pose, Point, Quaternion
from std_msgs.msg import Header

# ----------------------------------------
# Helper: minimal STL loader to compute AABB
# ----------------------------------------
def compute_aabb_from_stl(path: Path) -> Optional[Tuple[Tuple[float,float,float], Tuple[float,float,float]]]:
    """
    Return (min_xyz, max_xyz) or None on failure.
    Supports ASCII and binary STL (basic).
    """
    try:
        with open(path, 'rb') as f:
            head = f.read(80)
            # Seek back
            f.seek(0)
            # Heuristic: if starts with "solid" and not binary header, try ASCII parse
            start = head[:5].decode('utf-8', errors='ignore').lower()
            if start == 'solid':
                # try ascii
                try:
                    f.seek(0)
                    min_x = min_y = min_z = float('inf')
                    max_x = max_y = max_z = float('-inf')
                    for line in f:
                        try:
                            s = line.decode('utf-8').strip()
                        except Exception:
                            continue
                        if s.startswith('vertex'):
                            parts = s.split()
                            if len(parts) >= 4:
                                x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                                min_x = min(min_x, x); min_y = min(min_y, y); min_z = min(min_z, z)
                                max_x = max(max_x, x); max_y = max(max_y, y); max_z = max(max_z, z)
                    if min_x == float('inf'):
                        return None
                    return ( (min_x, min_y, min_z), (max_x, max_y, max_z) )
                except Exception:
                    # fallback to binary parse below
                    pass
            # Binary STL parse
            f.seek(80)
            count_bytes = f.read(4)
            if len(count_bytes) < 4:
                return None
            tri_count = struct.unpack('<I', count_bytes)[0]
            min_x = min_y = min_z = float('inf')
            max_x = max_y = max_z = float('-inf')
            # Each triangle: normal(3 floats) + 3 verts (9 floats) + ushort attribute = 50 bytes
            for i in range(tri_count):
                data = f.read(50)
                if len(data) < 50:
                    break
                floats = struct.unpack('<12fH', data)  # 12 floats + ushort
                # floats[3:12] are the 3 vertices (9 floats)
                v = floats[3:12]
                for vi in range(0, 9, 3):
                    x, y, z = v[vi], v[vi+1], v[vi+2]
                    min_x = min(min_x, x); min_y = min(min_y, y); min_z = min(min_z, z)
                    max_x = max(max_x, x); max_y = max(max_y, y); max_z = max(max_z, z)
            if min_x == float('inf'):
                return None
            return ( (min_x, min_y, min_z), (max_x, max_y, max_z) )
    except Exception:
        return None

# ----------------------------------------
# Helper: find model folder and model.sdf/model.config
# ----------------------------------------
def find_model_folder(model_name: str) -> Optional[Path]:
    # search GAZEBO_MODEL_PATH
    paths = []
    env = os.environ.get('GAZEBO_MODEL_PATH', '')
    if env:
        paths.extend(env.split(':'))
    # common locations
    paths.append(str(Path.home() / '.gazebo' / 'models'))
    # typical system location (depends on distro and gazebo version)
    paths.append('/usr/share/gazebo/models')
    # iterate
    for base in paths:
        if not base:
            continue
        p = Path(base) / model_name
        if p.exists() and p.is_dir():
            return p
    return None

# ----------------------------------------
# Convert geometry from SDF node into collision objects
# ----------------------------------------
def parse_geometries_from_sdf(model_folder: Path) -> List[dict]:
    """
    Return list of geometry dicts describing primitives or meshes.
    Each dict: {'type': 'box'|'cylinder'|'sphere'|'mesh', 'size': [x,y,z] or 'uri': 'path/to/file'}
    """
    model_sdf_candidates = [model_folder / 'model.sdf', model_folder / 'model.urdf', model_folder / 'model.config']
    sdf_path = None
    for c in model_sdf_candidates:
        if c.exists():
            sdf_path = c
            break
    result = []
    if not sdf_path:
        return result
    # If model.config (XML) points to sdf file, try to parse it
    try:
        tree = ET.parse(str(sdf_path))
        root = tree.getroot()
    except Exception:
        return result

    # Search for <collision> elements and geometry children
    # This attempts both SDF and simplistic URDF style
    for geom in root.findall('.//geometry'):
        # box
        box = geom.find('box')
        if box is not None:
            size_el = box.find('size')
            if size_el is not None and size_el.text:
                size = [float(x) for x in size_el.text.split()]
                result.append({'type': 'box', 'size': size})
            continue
        # cylinder
        cyl = geom.find('cylinder')
        if cyl is not None:
            radius_el = cyl.find('radius')
            length_el = cyl.find('length') or cyl.find('height')
            if radius_el is not None and length_el is not None:
                r = float(radius_el.text)
                h = float(length_el.text)
                result.append({'type': 'cylinder', 'radius': r, 'height': h})
            continue
        # sphere
        sph = geom.find('sphere')
        if sph is not None:
            r_el = sph.find('radius')
            if r_el is not None:
                result.append({'type': 'sphere', 'radius': float(r_el.text)})
            continue
        # mesh
        mesh = geom.find('mesh')
        if mesh is not None:
            uri_el = mesh.find('uri')
            if uri_el is not None and uri_el.text:
                uri = uri_el.text.strip()
                # handle model:// and file://
                if uri.startswith('model://'):
                    rel = uri[len('model://'):]
                    # find within model folder (model-specific)
                    mesh_path = model_folder / rel
                    # sometimes mesh_path is directory + file; normalize
                    mesh_path = mesh_path.resolve()
                    result.append({'type': 'mesh', 'uri': str(mesh_path)})
                elif uri.startswith('file://'):
                    # absolute file path
                    fp = uri[len('file://'):]
                    result.append({'type': 'mesh', 'uri': fp})
                else:
                    # other URI schemes (skip or try relative)
                    result.append({'type': 'mesh', 'uri': uri})
            continue

    # If nothing found, fallback: look for meshes folder in model folder
    if not result:
        meshes = list(model_folder.rglob('*.stl')) + list(model_folder.rglob('*.dae')) + list(model_folder.rglob('*.obj'))
        for m in meshes:
            result.append({'type': 'mesh', 'uri': str(m)})
    return result

# ----------------------------------------
# Node class
# ----------------------------------------
class GazeboToMoveIt(Node):
    def __init__(self):
        super().__init__('gazebo_to_moveit_obstacles')

        # Gazebo service clients (classic)
        self.cli_world = self.create_client(GetWorldProperties, '/gazebo/get_world_properties')
        self.cli_model_state = self.create_client(GetModelState, '/gazebo/get_model_state')

        # MoveIt planning_scene publisher
        self.planning_scene_pub = self.create_publisher(PlanningScene, 'planning_scene', 10)

        # Wait for services
        self.get_logger().info('Waiting for Gazebo services...')
        # Wait but don't block forever
        for cli in [self.cli_world, self.cli_model_state]:
            if not cli.wait_for_service(timeout_sec=5.0):
                self.get_logger().error(f'Service {cli.srv_name} not available after timeout. Make sure gazebo_core/gazebo_ros is running.')
                # continue; we may still try later
        self.get_logger().info('Gazebo clients created (or timed out).')

    def run_once_and_publish(self):
        # 1) Get model list
        req = GetWorldProperties.Request()
        fut = self.cli_world.call_async(req)
        rclpy.spin_until_future_complete(self, fut, timeout_sec=5.0)
        if not fut.result():
            self.get_logger().error('Failed to call /gazebo/get_world_properties')
            return

        model_names = fut.result().model_names
        self.get_logger().info(f'Found {len(model_names)} models: {model_names}')

        scene = PlanningScene()
        scene.is_diff = True

        for model_name in model_names:
            # skip the 'ground_plane' optionally
            if model_name.lower().startswith('ground') or model_name == 'ground_plane':
                continue

            # get model pose
            mreq = GetModelState.Request()
            mreq.model_name = model_name
            mfut = self.cli_model_state.call_async(mreq)
            rclpy.spin_until_future_complete(self, mfut, timeout_sec=3.0)
            if not mfut.result():
                self.get_logger().warn(f'Could not get state for model {model_name}')
                continue
            model_state = mfut.result()
            pose: Pose = model_state.pose

            # find model folder
            folder = find_model_folder(model_name)
            if folder is None:
                self.get_logger().warn(f'Could not find local model folder for {model_name}. Looking for meshes skipped.')
                # create a small placeholder box at model pose (safe)
                co = CollisionObject()
                co.id = model_name
                co.header.frame_id = 'world'
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.BOX
                prim.dimensions = [0.5, 0.5, 0.5]  # conservative placeholder
                co.primitives.append(prim)
                co.primitive_poses.append(pose)
                co.operation = CollisionObject.ADD
                scene.world.collision_objects.append(co)
                continue

            geoms = parse_geometries_from_sdf(folder)
            if not geoms:
                # fallback: small placeholder box
                self.get_logger().info(f'No geometries found for {model_name}; adding placeholder box.')
                co = CollisionObject()
                co.id = model_name
                co.header.frame_id = 'world'
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.BOX
                prim.dimensions = [0.5, 0.5, 0.5]
                co.primitives.append(prim)
                co.primitive_poses.append(pose)
                co.operation = CollisionObject.ADD
                scene.world.collision_objects.append(co)
                continue

            # For each geometry, create a collision object. For simplicity we will combine them into one per model by offsetting poses to model pose.
            # Here we create one object per model using first geometry (you can extend to multiple)
            # Prefer primitives
            created = False
            for g in geoms:
                co = CollisionObject()
                co.id = f'{model_name}'
                co.header.frame_id = 'world'

                if g['type'] == 'box':
                    prim = SolidPrimitive()
                    prim.type = SolidPrimitive.BOX
                    # SDF box size is "x y z"
                    size = g['size']
                    # MoveIt order for box dims: x,y,z
                    prim.dimensions = [size[0], size[1], size[2]]
                    co.primitives.append(prim)
                    co.primitive_poses.append(pose)
                    co.operation = CollisionObject.ADD
                    scene.world.collision_objects.append(co)
                    created = True
                    break

                elif g['type'] == 'cylinder':
                    prim = SolidPrimitive()
                    prim.type = SolidPrimitive.CYLINDER
                    # MoveIt uses [height, radius] order for cylinder dims
                    prim.dimensions = [g['height'], g['radius']]
                    co.primitives.append(prim)
                    co.primitive_poses.append(pose)
                    co.operation = CollisionObject.ADD
                    scene.world.collision_objects.append(co)
                    created = True
                    break

                elif g['type'] == 'sphere':
                    prim = SolidPrimitive()
                    prim.type = SolidPrimitive.SPHERE
                    prim.dimensions = [g['radius']]
                    co.primitives.append(prim)
                    co.primitive_poses.append(pose)
                    co.operation = CollisionObject.ADD
                    scene.world.collision_objects.append(co)
                    created = True
                    break

                elif g['type'] == 'mesh':
                    uri = g.get('uri', '')
                    # Try to resolve path
                    mesh_path = Path(uri)
                    if not mesh_path.exists():
                        # try join with folder
                        cand = (folder / uri).resolve()
                        if cand.exists():
                            mesh_path = cand
                    if mesh_path.exists() and mesh_path.suffix.lower() == '.stl':
                        aabb = compute_aabb_from_stl(mesh_path)
                        if aabb:
                            (minx,miny,minz), (maxx,maxy,maxz) = aabb
                            dx = maxx - minx
                            dy = maxy - miny
                            dz = maxz - minz
                            # center in mesh local coordinates
                            cx = (minx + maxx) / 2.0
                            cy = (miny + maxy) / 2.0
                            cz = (minz + maxz) / 2.0

                            # Create a box primitive sized to AABB. Place it at model pose shifted by mesh center.
                            prim = SolidPrimitive()
                            prim.type = SolidPrimitive.BOX
                            prim.dimensions = [dx, dy, dz]

                            mp = Pose()
                            mp.position.x = pose.position.x + cx
                            mp.position.y = pose.position.y + cy
                            mp.position.z = pose.position.z + cz
                            mp.orientation = pose.orientation  # approximate

                            co.primitives.append(prim)
                            co.primitive_poses.append(mp)
                            co.operation = CollisionObject.ADD
                            scene.world.collision_objects.append(co)
                            created = True
                            break
                        else:
                            self.get_logger().warn(f'Failed to parse STL for {mesh_path}; using fallback box.')
                    else:
                        self.get_logger().info(f'Mesh file missing or non-STL ({uri}). Using fallback box for {model_name}.')
                    # fallback
                    prim = SolidPrimitive()
                    prim.type = SolidPrimitive.BOX
                    prim.dimensions = [0.5, 0.5, 0.5]
                    co.primitives.append(prim)
                    co.primitive_poses.append(pose)
                    co.operation = CollisionObject.ADD
                    scene.world.collision_objects.append(co)
                    created = True
                    break

            if not created:
                # last resort
                co = CollisionObject()
                co.id = model_name
                co.header.frame_id = 'world'
                prim = SolidPrimitive()
                prim.type = SolidPrimitive.BOX
                prim.dimensions = [0.5, 0.5, 0.5]
                co.primitives.append(prim)
                co.primitive_poses.append(pose)
                co.operation = CollisionObject.ADD
                scene.world.collision_objects.append(co)

        # publish planning scene diff
        self.planning_scene_pub.publish(scene)
        self.get_logger().info(f'Published PlanningScene with {len(scene.world.collision_objects)} collision objects.')

def main(args=None):
    rclpy.init(args=args)
    node = GazeboToMoveIt()
    try:
        node.get_logger().info('Running single extraction & publish...')
        node.run_once_and_publish()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
