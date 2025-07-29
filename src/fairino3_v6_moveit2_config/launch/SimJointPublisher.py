#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math
import time
from fairino_msgs.msg import RobotNonrtState  # Replace with actual msg type
from builtin_interfaces.msg import Duration # For ROS2

class SimJointPublisher(Node):
	def __init__(self):
		super().__init__('sim_joint_publisher')
		# /joint_state topic
		self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
		self.publisher_2 = self.create_publisher(JointTrajectory, 'fairino3_controller/joint_trajectory', 10)
		timer_period = 0.1  # seconds
		self.subscription = self.create_subscription(
			RobotNonrtState,
			'/nonrt_state_data',
			self.listener_callback,
			10
		)
		self.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']  # replace with real names
		self.start_time = time.time()


	def listener_callback(self, msg):
		# Convert joint positions from /nonrt_state_data
		joint_positions = [
			math.radians(msg.j1_cur_pos), math.radians(msg.j2_cur_pos), math.radians(msg.j3_cur_pos),
			math.radians(msg.j4_cur_pos), math.radians(msg.j5_cur_pos), math.radians(msg.j6_cur_pos)
		]
		# /joint_state callback
		joint_state = JointState()
		joint_state.header.stamp = self.get_clock().now().to_msg()
		joint_state.name = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
		joint_state.position = joint_positions
		self.publisher_.publish(joint_state)

		# /joint_trajectory callback
		joint_trajectory = JointTrajectory()
		joint_trajectory.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
		point =JointTrajectoryPoint()
		point.time_from_start = Duration(sec=1, nanosec=0)

		# p1.positions, p2.positions, p3.positions, p4.positions, p5.positions, p6.positions = joint_positions
		point.positions = joint_positions
		joint_trajectory.points.append(point)
		# joint_trajectory.points.append(p2)
		# joint_trajectory.points.append(p3)
		# joint_trajectory.points.append(p4)
		# joint_trajectory.points.append(p5)
		# joint_trajectory.points.append(p6)
		self.publisher_2.publish(joint_trajectory)
    
	def on_shutdown(self):
		self.destroy_publisher(self.publisher_)
		self.destroy_publisher(self.publisher_2)
		self.destroy_subscription(self.subscription)

		self.get_logger().info('on_shutdown() is called.')

		
def main(args=None):
	rclpy.init(args=args)
	node = SimJointPublisher()
	rclpy.spin(node)
	rclpy.shutdown()


if __name__ == '__main__':
	main()
