#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from moveit_msgs.msg import CollisionObject, PlanningScene
from moveit_msgs.srv import ApplyPlanningScene
from shape_msgs.msg import SolidPrimitive
from geometry_msgs.msg import Pose
import xml.etree.ElementTree as ET
import math
import sys


def rpy_to_quaternion(roll, pitch, yaw):
    """Convert RPY to quaternion (geometry_msgs standard)."""
    qx = math.sin(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) - math.cos(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)
    qy = math.cos(roll/2) * math.sin(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.cos(pitch/2) * math.sin(yaw/2)
    qz = math.cos(roll/2) * math.cos(pitch/2) * math.sin(yaw/2) - math.sin(roll/2) * math.sin(pitch/2) * math.cos(yaw/2)
    qw = math.cos(roll/2) * math.cos(pitch/2) * math.cos(yaw/2) + math.sin(roll/2) * math.sin(pitch/2) * math.sin(yaw/2)
    return qx, qy, qz, qw


class WorldToMoveIt(Node):
    def __init__(self, world_file):
        super().__init__('gazebo_world_to_moveit')
        self.get_logger().info(f'Parsing world file: {world_file}')

        # Parse world file
        models = self.parse_world(world_file)
        self.get_logger().info(f'Found {len(models)} models.')

        # Client to apply planning scene
        self.cli = self.create_client(ApplyPlanningScene, '/apply_planning_scene')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /apply_planning_scene service...')

        # Build PlanningScene request
        ps = PlanningScene()
        ps.is_diff = True

        for model in models:
            co = self.create_collision_object(model)
            ps.world.collision_objects.append(co)

        # Apply to MoveIt
        req = ApplyPlanningScene.Request(scene=ps)
        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info('All collision objects added!')
        else:
            self.get_logger().error('Failed to apply planning scene.')

    def parse_world(self, world_file):
        """Extracts simple shapes (box, cylinder, sphere) from Gazebo world."""
        with open(world_file, 'r', encoding='utf-8', errors='ignore') as f:
            xml_text = f.read()
        tree = ET.parse(world_file)
        root = tree.getroot()
        models = []

        for model in root.findall('.//model'):
            name = model.attrib.get('name', 'unnamed')
            pose_text = model.findtext('pose', default='0 0 0 0 0 0')
            px, py, pz, rr, pp, yy = map(float, pose_text.split())

            # Find the first collision geometry
            geom = model.find('.//geometry')
            if geom is None:
                continue

            shape = None
            size = [0.1, 0.1, 0.1]  # default

            if geom.find('box') is not None:
                shape = 'box'
                size_text = geom.findtext('box/size', default='0.1 0.1 0.1')
                size = list(map(float, size_text.split()))
            elif geom.find('sphere') is not None:
                shape = 'sphere'
                size = [float(geom.findtext('sphere/radius', default='0.05'))]
            elif geom.find('cylinder') is not None:
                shape = 'cylinder'
                radius = float(geom.findtext('cylinder/radius', default='0.05'))
                length = float(geom.findtext('cylinder/length', default='0.1'))
                size = [length, radius]
            else:
                continue

            models.append({
                'name': name,
                'shape': shape,
                'size': size,
                'pose': (px, py, pz, rr, pp, yy)
            })
        return models

    def create_collision_object(self, model):
        """Convert parsed model data to a CollisionObject."""
        co = CollisionObject()
        co.id = model['name']
        co.header.frame_id = 'world'
        co.operation = CollisionObject.ADD

        prim = SolidPrimitive()
        if model['shape'] == 'box':
            prim.type = SolidPrimitive.BOX
            prim.dimensions = model['size']
        elif model['shape'] == 'sphere':
            prim.type = SolidPrimitive.SPHERE
            prim.dimensions = model['size']
        elif model['shape'] == 'cylinder':
            prim.type = SolidPrimitive.CYLINDER
            prim.dimensions = model['size']

        pose = Pose()
        px, py, pz, rr, pp, yy = model['pose']
        pose.position.x = px
        pose.position.y = py
        pose.position.z = pz
        pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w = rpy_to_quaternion(rr, pp, yy)

        co.primitives.append(prim)
        co.primitive_poses.append(pose)
        return co


def main(args=None):
    rclpy.init(args=args)

    if len(sys.argv) < 2:
        print("Usage: ros2 run <package> <node> -- <world_file.sdf>")
        sys.exit(1)

    world_file = sys.argv[1]
    world_path = '/usr/share/ignition/ignition-gazebo6/worlds/' + world_file
    node = WorldToMoveIt(world_path)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
