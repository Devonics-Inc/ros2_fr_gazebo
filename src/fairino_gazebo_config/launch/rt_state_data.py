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

### EDIT THIS TO ADD STATE_DATA PUBLISHING ###

ROBOT_IP = "192.168.55.2" # Find another way to grab IP from fairino_hardware
ROBOT_PORT = 8083	# DO NOT CHANGE!

class rt_state_data(Node):
	def __init__(self):
		super().__init__('rt_joint_publisher')
		# Grab parameter value for robot model:
		self.declare_parameter('robot_model', 'fairino3') # Get robot model from launch file (defualt_val=fairino3)
		fr_model = self.get_parameter('robot_model').value
		# /joint_state topic creation
		self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
		# /connect to joint_traj to send data to
		self.publisher_2 = self.create_publisher(JointTrajectory, f'{fr_model}_controller/joint_trajectory', 10)
		# Create socket for real time state data from robot
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ROBOT_IP, ROBOT_PORT))
		self.get_logger().info(f"Connected to robot at {ROBOT_IP}:{ROBOT_PORT}")

		# Create callback loop for joint_states
		timer_period = 0.1  # seconds
		self.subscription = self.create_subscription(
			JointState,
			'/joint_states',
			self.listener_callback,
			10
		)
		self.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']  # replace with real names
		self.start_time = time.time()


	def listener_callback(self, msg):
		# Convert and publish joint pos from socket
		try:
			frame = self.parse_frame()
			joint_positions = self.extract_joint_positions(frame)
			# Create and populate JointState message
			joint_state = JointState()
			joint_state.header.stamp = self.get_clock().now().to_msg()
			joint_state.name = self.joint_names
			joint_state.position = joint_positions
			#self.get_logger().info(f"Joint positions (rad): {joint_state.position}")

			self.publisher_.publish(joint_state) # Publish

			# Create and populate joint_trajectory message
			joint_positions = [math.radians(j) for j in joint_positions] # Convert to rads for joint_traj 
			joint_trajectory = JointTrajectory()
			joint_trajectory.joint_names = self.joint_names
			point =JointTrajectoryPoint()
			point.time_from_start = Duration(sec=1, nanosec=0)
			point.positions = joint_positions
			joint_trajectory.points.append(point)
			
			self.publisher_2.publish(joint_trajectory) # Publish

		except Exception as e:
			self.get_logger().info(f"Error: {e}")
    
	def on_shutdown(self):
		self.destroy_publisher(self.publisher_)
		self.destroy_publisher(self.publisher_2)
		self.destroy_subscription(self.subscription)
		self.destroy_node()
		self.get_logger().info('on_shutdown() is called.')

	# Data gathering from robot state package socker
	def read_exact(self, size):
	    """Read exactly `size` bytes from the socket."""
	    buf = b""
	    while len(buf) < size:
	        chunk = self.sock.recv(size - len(buf))
	        if not chunk:
	            raise ConnectionError("Socket closed")
	        buf += chunk
	    return buf

	def parse_frame(self):
	    """Read and parse one feedback frame from the robot."""
	    # Read header (2 bytes), frame count (1 byte), data length (2 bytes)
	    header = self.read_exact(2)
	    if header != b'\x5A\x5A':
	        raise ValueError(f"Invalid header: {header.hex()}")

	    frame_count = struct.unpack("<B", self.read_exact(1))[0]
	    data_len = struct.unpack("<H", self.read_exact(2))[0]

	    # Read data and checksum
	    data = self.read_exact(data_len)
	    checksum = struct.unpack("<H", self.read_exact(2))[0]

	    # Verify checksum: sum of all bytes from header..data
	    total = sum(header + bytes([frame_count]) + struct.pack("<H", data_len) + data) & 0xFFFF
	    if checksum != total:
	        raise ValueError(f"Checksum mismatch: got {checksum}, expected {total}")

	    return data

	def extract_joint_positions(self, data):
	    """Extract 6 joint positions (degrees) from the payload."""
	    # From Table 2-2, jt_cur_pos[0..5] are the 4th–9th entries (after program_state, error_code, robot_mode).
	    offset = 3  # 3 bytes before joint data: program_state, error_code, robot_mode
	    pos_offset = offset
	    joint_positions = []
	    for i in range(6):
	        val = struct.unpack_from("<d", data, pos_offset)[0]
	        joint_positions.append(val)
	        pos_offset += 8
	    return joint_positions


def main(args=None):
	rclpy.init(args=args)
	node = rt_state_data()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()


if __name__ == '__main__':
	main()
