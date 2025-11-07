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
import threading


class rt_state_data(Node):
    def __init__(self):
        super().__init__('rt_joint_publisher')

        # --- Parameters ---
        self.declare_parameter('robot_model', 'fairino5')
        self.declare_parameter('robot_ip', '192.168.56.2')
        self.declare_parameter('robot_port', 20004)

        self.robot_model = self.get_parameter('robot_model').value
        self.robot_ip = self.get_parameter('robot_ip').value
        self.robot_port = self.get_parameter('robot_port').value

        # --- Publishers ---
        self.joint_state_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.traj_pub = self.create_publisher(
            JointTrajectory, f'{self.robot_model}_controller/joint_trajectory', 10
        )

        # --- Joint names ---
        self.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']

        # --- Socket and threading setup ---
        self.sock = None
        self._buffer = b""
        self.sock_lock = threading.Lock()
        self.latest_data = None
        self.running = True

        self.connect_socket()

        # Start background thread for socket reading
        self.reader_thread = threading.Thread(target=self.socket_reader_loop, daemon=True)
        self.reader_thread.start()

        # ROS2 Timer for publishing (non-blocking)
        self.timer = self.create_timer(0.02, self.publish_latest)  # 50 Hz publish rate

        self.get_logger().info("rt_state_data node initialized.")

    # ===============================================================
    #                      SOCKET CONNECTION
    # ===============================================================
    def connect_socket(self):
        """Attempt to connect to robot socket."""
        try:
            if self.sock:
                self.sock.close()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            self.sock.settimeout(None)
            self.sock.connect((self.robot_ip, self.robot_port))
            self._buffer = b""
            self.get_logger().info(f"Connected to robot at {self.robot_ip}:{self.robot_port}")
        except Exception as e:
            self.get_logger().error(f"Failed to connect to robot: {e}")
            self.sock = None

    # ===============================================================
    #                        FRAME PARSING
    # ===============================================================
    def parse_frame(self):
        """Buffered parser for one complete frame."""
        while True:
            # Read more data from the socket
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("Socket closed by robot")
            self._buffer += chunk

            # Look for frame header
            start = self._buffer.find(b'\x5A\x5A')
            if start == -1:
                # No header yet; discard old garbage
                self._buffer = b""
                continue

            # Wait until we have enough bytes for header + frame_count + data_len
            if len(self._buffer) < start + 5:
                # Need more data
                continue

            # Safely unpack header, frame_count, and data_len
            header = self._buffer[start:start+2]
            frame_count = self._buffer[start+2]
            data_len = struct.unpack_from("<H", self._buffer, start+3)[0]

            total_len = 2 + 1 + 2 + data_len + 2  # header + count + len + data + checksum

            # Wait until the full frame is in the buffer
            if len(self._buffer) < start + total_len:
                continue  # not yet complete

            # Extract frame and consume it from buffer
            frame = self._buffer[start:start + total_len]
            self._buffer = self._buffer[start + total_len:]

            # Validate checksum
            data = frame[5:-2]
            checksum = struct.unpack("<H", frame[-2:])[0]
            total = sum(frame[:-2]) & 0xFFFF

            if checksum != total:
                self.get_logger().warn("Checksum mismatch, skipping frame.")
                continue

            return data


    def extract_joint_positions(self, data):
        """Extract 6 joint positions (degrees) from frame payload."""
        offset = 11  # skip status bytes
        joint_positions = []
        for i in range(6):
            val = struct.unpack_from("<d", data, offset)[0]
            joint_positions.append(val)
            offset += 8
        return joint_positions

    # ===============================================================
    #                      BACKGROUND THREAD
    # ===============================================================
    def socket_reader_loop(self):
        """Continuously read frames from the robot in a separate thread."""
        while self.running:
            if not self.sock:
                self.connect_socket()
                time.sleep(0.5)
                continue
            try:
                frame = self.parse_frame()
                with self.sock_lock:
                    self.latest_data = frame
            except (socket.error, ConnectionError) as e:
                self.get_logger().warning(f"Socket error: {e}. Reconnecting...")
                time.sleep(0.5)
                self.connect_socket()
            except Exception as e:
                self.get_logger().error(f"Error parsing frame: {e}")
                time.sleep(0.05)

    # ===============================================================
    #                        ROS2 PUBLISHING
    # ===============================================================
    def publish_latest(self):
        """Publish the most recent joint data safely."""
        with self.sock_lock:
            data = self.latest_data
        if data is None:
            return

        try:
            joint_positions_deg = self.extract_joint_positions(data)
            joint_positions_rad = [math.radians(j) for j in joint_positions_deg]

            # JointState (deg)
            joint_state = JointState()
            joint_state.header.stamp = self.get_clock().now().to_msg()
            joint_state.name = self.joint_names
            joint_state.position = joint_positions_deg
            self.joint_state_pub.publish(joint_state)

            # JointTrajectory (rad)
            traj_msg = JointTrajectory()
            traj_msg.joint_names = self.joint_names
            point = JointTrajectoryPoint()
            point.positions = joint_positions_rad
            point.time_from_start = Duration(sec=1)
            traj_msg.points.append(point)
            self.traj_pub.publish(traj_msg)

            self.get_logger().debug(f"Published joint positions (deg): {joint_positions_deg}")

        except Exception as e:
            self.get_logger().error(f"Publish error: {e}")

    # ===============================================================
    #                      CLEAN SHUTDOWN
    # ===============================================================
    def destroy_node(self):
        """Clean shutdown for socket and thread."""
        self.running = False
        if self.sock:
            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except Exception:
                pass
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
