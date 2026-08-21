#!/usr/bin/env python3

import math
import os
import struct

import yaml
import rclpy
from rclpy.node import Node
from ament_index_python.packages import get_package_share_directory
from moveit_msgs.msg import CollisionObject
from moveit_msgs.srv import ApplyPlanningScene
from shape_msgs.msg import SolidPrimitive, Mesh, MeshTriangle
from geometry_msgs.msg import Pose, Point, Vector3
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA


class ScenePublisherNode(Node):

    def __init__(self):
        super().__init__('scene_publisher')
        self.get_logger().info('\n[SCENE PUB] Creating scene pub...\n')
        self.declare_parameter('environment_file', '')

        self._col_pub = self.create_publisher(CollisionObject, '/collision_object', 10)
        self._col_marker_pub = self.create_publisher(
            MarkerArray, '/environment_collision', 10
        )
        self._vis_marker_pub = self.create_publisher(
            MarkerArray, '/environment_visual', 10
        )

        # Use the service purely as a readiness gate — if the service exists,
        # move_group is running and subscribed to /collision_object
        self._ready_client = self.create_client(
            ApplyPlanningScene, '/apply_planning_scene'
        )

        self._timer = self.create_timer(1.0, self._try_publish)

    def _try_publish(self):
        if not self._ready_client.service_is_ready():
            self.get_logger().info('\n[SCENE PUB] Waiting for move_group to start...\n')
            return

        self._timer.cancel()
        self.get_logger().info(
            '\n[SCENE PUB] move_group is ready, waiting for DDS endpoint matching...\n'
        )
        # Delay to allow DDS to match our publisher to move_group's subscriber
        self._publish_timer = self.create_timer(3.0, self._do_publish)

    def _do_publish(self):
        self._publish_timer.cancel()

        config_path = self.get_parameter('environment_file').get_parameter_value().string_value
        if not config_path:
            config_path = os.path.join(
                get_package_share_directory('sim_config'), 'config', 'environment.yaml'
            )
        self.get_logger().info(f'Loading: {config_path}')

        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        # --- Collision objects (MoveIt planning scene + RViz markers) ---
        objects = config.get('collision_objects', [])
        self.get_logger().info(f'Found {len(objects)} collision objects')
        col_markers = MarkerArray()
        self.get_logger().info(f"[SCENE PUB] {len(objects)} found in env file")
        for idx, obj in enumerate(objects):
            co = self._make_collision_object(obj)
            if co:
                self._col_pub.publish(co)
                self.get_logger().info(f"\n Collision: {obj['name']}\n")

            marker = self._make_collision_marker(obj, idx)
            if marker:
                col_markers.markers.append(marker)

        if col_markers.markers:
            self._col_marker_pub.publish(col_markers)

        # --- Visual-only objects (RViz markers only) ---
        visuals = config.get('visual_objects', [])
        if visuals:
            self.get_logger().info(f'Found {len(visuals)} visual objects')
            vis_markers = MarkerArray()
            for idx, vobj in enumerate(visuals):
                marker = self._make_visual_marker(vobj, idx)
                if marker:
                    vis_markers.markers.append(marker)
                    self.get_logger().info(f"\n\n  Visual: {vobj['name']}")
            self._vis_marker_pub.publish(vis_markers)

        self.get_logger().info('Done')

    # -- helpers ----------------------------------------------------------

    def _make_pose(self, obj):
        pos = obj.get('position', [0, 0, 0])
        pose = Pose()
        pose.position.x = float(pos[0])
        pose.position.y = float(pos[1])
        pose.position.z = float(pos[2])

        rpy = obj.get('orientation', [0, 0, 0])
        q = self._quaternion_from_rpy(float(rpy[0]), float(rpy[1]), float(rpy[2]))
        pose.orientation.x = q[0]
        pose.orientation.y = q[1]
        pose.orientation.z = q[2]
        pose.orientation.w = q[3]

        return pose

    # -- collision objects ------------------------------------------------

    def _make_collision_object(self, obj):
        co = CollisionObject()
        co.header.frame_id = 'world'
        co.header.stamp = self.get_clock().now().to_msg()
        co.id = obj['name']

        pose = self._make_pose(obj)

        # Mesh-based collision object
        if 'mesh' in obj:
            file_path = self._resolve_package_uri(obj['mesh'])
            if not file_path:
                return None

            mesh = self._load_stl(file_path, obj.get('scale', [1.0, 1.0, 1.0]))
            if not mesh:
                return None

            co.meshes.append(mesh)
            co.mesh_poses.append(pose)
            return co

        # Primitive-based collision object
        obj_type = obj.get('type', '')
        if obj_type == 'box':
            size = obj.get('size', [1, 1, 1])
            primitive = SolidPrimitive()
            primitive.type = SolidPrimitive.BOX
            primitive.dimensions = [float(s) for s in size]
            co.primitives.append(primitive)
            co.primitive_poses.append(pose)
            return co

        self.get_logger().warn(f"Unsupported collision object '{obj['name']}': "
                               f"needs 'mesh' or 'type' field")
        return None

    def _make_collision_marker(self, obj, marker_id):
        """RViz marker mirroring a collision object (for toggle-able display)."""
        marker = Marker()
        marker.header.frame_id = 'world'
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = 'environment_collision'
        marker.id = marker_id
        marker.action = Marker.ADD
        marker.pose = self._make_pose(obj)

        rgba = obj.get('color', [0.0, 1.0, 0.0, 0.5])
        marker.color = ColorRGBA(
            r=float(rgba[0]), g=float(rgba[1]),
            b=float(rgba[2]), a=float(rgba[3])
        )

        if 'mesh' in obj:
            marker.type = Marker.MESH_RESOURCE
            marker.mesh_resource = obj['mesh']
            sc = obj.get('scale', [1.0, 1.0, 1.0])
            marker.scale = Vector3(x=float(sc[0]), y=float(sc[1]), z=float(sc[2]))
        elif obj.get('type') == 'box':
            marker.type = Marker.CUBE
            size = obj.get('size', [1, 1, 1])
            marker.scale = Vector3(
                x=float(size[0]), y=float(size[1]), z=float(size[2])
            )
        else:
            return None

        return marker

    # -- visual-only objects ----------------------------------------------

    def _make_visual_marker(self, obj, marker_id):
        mesh = obj.get('mesh', '')
        if not mesh:
            self.get_logger().warn(
                f"No mesh for visual object '{obj.get('name', '?')}'"
            )
            return None

        marker = Marker()
        marker.header.frame_id = 'world'
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = 'environment_visual'
        marker.id = marker_id
        marker.type = Marker.MESH_RESOURCE
        marker.action = Marker.ADD
        marker.mesh_resource = mesh
        marker.pose = self._make_pose(obj)

        sc = obj.get('scale', [1.0, 1.0, 1.0])
        marker.scale = Vector3(x=float(sc[0]), y=float(sc[1]), z=float(sc[2]))

        rgba = obj.get('color', [0.8, 0.8, 0.8, 1.0])
        marker.color = ColorRGBA(
            r=float(rgba[0]), g=float(rgba[1]),
            b=float(rgba[2]), a=float(rgba[3])
        )

        return marker

    # -- STL loading ------------------------------------------------------

    def _resolve_package_uri(self, uri):
        if not uri.startswith('package://'):
            return uri
        rest = uri[len('package://'):]
        pkg_name, _, rel_path = rest.partition('/')
        try:
            pkg_dir = get_package_share_directory(pkg_name)
            return os.path.join(pkg_dir, rel_path)
        except Exception as e:
            self.get_logger().error(f"Package '{pkg_name}' not found: {e}")
            return None

    def _load_stl(self, file_path, scale=None):
        if scale is None:
            scale = [1.0, 1.0, 1.0]
        sx, sy, sz = float(scale[0]), float(scale[1]), float(scale[2])

        try:
            with open(file_path, 'rb') as f:
                f.read(80)  # header
                num_triangles = struct.unpack('<I', f.read(4))[0]

                mesh = Mesh()
                for _ in range(num_triangles):
                    data = f.read(50)
                    values = struct.unpack('<12fH', data)
                    # [0:3]=normal, [3:12]=3 vertices (x,y,z each), [12]=attr

                    tri = MeshTriangle()
                    base = len(mesh.vertices)
                    for v in range(3):
                        x = values[3 + v * 3] * sx
                        y = values[4 + v * 3] * sy
                        z = values[5 + v * 3] * sz
                        mesh.vertices.append(Point(x=x, y=y, z=z))
                    tri.vertex_indices = [base, base + 1, base + 2]
                    mesh.triangles.append(tri)

                self.get_logger().info(
                    f"  STL loaded: {num_triangles} triangles, "
                    f"{len(mesh.vertices)} vertices from {os.path.basename(file_path)}"
                )
                return mesh
        except Exception as e:
            self.get_logger().error(f"Failed to load STL '{file_path}': {e}")
            return None

    # -- math -------------------------------------------------------------

    @staticmethod
    def _quaternion_from_rpy(roll, pitch, yaw):
        cr, sr = math.cos(roll / 2), math.sin(roll / 2)
        cp, sp = math.cos(pitch / 2), math.sin(pitch / 2)
        cy, sy = math.cos(yaw / 2), math.sin(yaw / 2)
        return (
            sr * cp * cy - cr * sp * sy,
            cr * sp * cy + sr * cp * sy,
            cr * cp * sy - sr * sp * cy,
            cr * cp * cy + sr * sp * sy,
        )


def main(args=None):
    print("called")
    rclpy.init(args=args)
    node = ScenePublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()