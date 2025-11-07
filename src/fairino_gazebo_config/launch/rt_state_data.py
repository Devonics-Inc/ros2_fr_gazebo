#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math
import time
from fairino_msgs.msg import RobotNonrtState  # Replace with actual msg type
from builtin_interfaces.msg import Duration # For ROS2
import socket
import struct


class rt_state_data(Node):
    def __init__(self):
        super().__init__('rt_joint_publisher')

        # Declare parameters
        self.declare_parameter('robot_model', 'fairino5')
        self.declare_parameter('robot_ip', '192.168.56.2')
        self.declare_parameter('robot_port', 20004)

        self.robot_model = self.get_parameter('robot_model').value
        self.robot_ip = self.get_parameter('robot_ip').value
        self.robot_port = self.get_parameter('robot_port').value

        # Publishers
        self.joint_state_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.traj_pub = self.create_publisher(
            JointTrajectory, f'{self.robot_model}_controller/joint_trajectory', 10
        )

        # Joint names
        self.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']

        # Socket setup
        self.sock = None
        self.connect_socket()

        # Timer for reading and publishing data
        self.timer = self.create_timer(0.05, self.timer_callback)  # 20 Hz update rate

    def connect_socket(self):
        """Attempt to connect to robot socket."""
        try:
            if self.sock:
                self.sock.close()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(2.0)
            self.sock.connect((self.robot_ip, self.robot_port))
            self.get_logger().info(f"Connected to robot at {self.robot_ip}:{self.robot_port}")
        except Exception as e:
            self.get_logger().error(f"Failed to connect to robot: {e}")
            self.sock = None

    def read_exact(self, size: int) -> bytes:
        """Read exactly `size` bytes from the socket."""
        buf = b""
        while len(buf) < size:
            chunk = self.sock.recv(size - len(buf))
            if not chunk:
                raise ConnectionError("Socket closed by robot")
            buf += chunk
        return buf

    def parse_frame(self):
        """Read and parse one feedback frame from the robot."""
        header = self.read_exact(2)
        if header != b'\x5A\x5A':
            raise ValueError(f"Invalid header: {header.hex()}")

        frame_count = struct.unpack("<B", self.read_exact(1))[0]
        data_len = struct.unpack("<H", self.read_exact(2))[0]
        data = self.read_exact(data_len)
        checksum = struct.unpack("<H", self.read_exact(2))[0]

        total = sum(header + bytes([frame_count]) + struct.pack("<H", data_len) + data) & 0xFFFF
        if checksum != total:
            raise ValueError(f"Checksum mismatch: got {checksum}, expected {total}")

        return data

    def extract_joint_positions(self, data):
        """Extract 6 joint positions (degrees) from the payload."""
        offset = 11  # skip program_state, error_code, robot_mode | 3 for 8083, 11 for 20004
        joint_positions = []
        for i in range(6):
            val = struct.unpack_from("<d", data, offset)[0]
            joint_positions.append(val)
            offset += 8
        return joint_positions

    def timer_callback(self):
        """Main data read/publish loop."""
        if not self.sock:
            self.connect_socket()
            return

        try:
            frame = self.parse_frame()
            joint_positions_deg = self.extract_joint_positions(frame)
            joint_positions_rad = [math.radians(j) for j in joint_positions_deg]

            # Publish JointState (degrees)
            joint_state = JointState()
            joint_state.header.stamp = self.get_clock().now().to_msg()
            joint_state.name = self.joint_names
            joint_state.position = joint_positions_deg
            self.joint_state_pub.publish(joint_state)

            # Publish JointTrajectory (radians)
            traj_msg = JointTrajectory()
            traj_msg.joint_names = self.joint_names
            point = JointTrajectoryPoint()
            point.positions = joint_positions_rad
            point.time_from_start = Duration(sec=1)
            traj_msg.points.append(point)
            self.traj_pub.publish(traj_msg)

            self.get_logger().debug(f"Published joint positions (deg): {joint_positions_deg}")

        except (socket.error, ConnectionError) as e:
            self.get_logger().warning(f"Socket error: {e}. Reconnecting...")
            self.connect_socket()
        except Exception as e:
            self.get_logger().error(f"Error parsing data: {e}")

    def destroy_node(self):
        if self.sock:
            self.sock.close()
        super().destroy_node()
        self.get_logger().info("rt_state_data node shut down cleanly.")


def main(args=None):
    rclpy.init(args=args)
    node = rt_state_data()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard interrupt received.")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
