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
import json


class rt_state_data(Node):
    def __init__(self):
        super().__init__('rt_joint_publisher')
        self.declare_parameter('robot_model', 'fairino5')
        self.robot_model = self.get_parameter('robot_model').value
        self.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.traj_pub = self.create_publisher(
            JointTrajectory, f'{self.robot_model}_controller/joint_trajectory', 10
        )
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 5005)) # SDK PORT FORWARD SOCKET
        self.sock.setblocking(False)
        self.timer = self.create_timer(0.01, self.loop)

    def loop(self):
        try:
            data, _ = self.sock.recvfrom(4096)
            msg = json.loads(data.decode())
            js = JointState()
            js.header.stamp = self.get_clock().now().to_msg()
            js.name = [f"joint_{i+1}" for i in range(6)]
            js.position = msg["joints"]
            self.pub.publish(js)
            # JointTrajectory (rad)
            traj_msg = JointTrajectory()
            traj_msg.joint_names = self.joint_names
            point = JointTrajectoryPoint()
            joint_positions_rad = [math.radians(j) for j in msg["joints"]]
            point.positions = joint_positions_rad
            point.time_from_start = Duration(sec=0, nanosec=12000000)
            traj_msg.points.append(point)
            self.traj_pub.publish(traj_msg)
        except BlockingIOError:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = rt_state_data()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()