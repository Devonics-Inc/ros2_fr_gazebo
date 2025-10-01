#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import time
import re

class SimTrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('sim_trajectory_pub')
        # Find correct fairino controller topic
        joint_traj_topic = None
        topic_list = self.get_topic_names_and_types()
        # Loop over all topics and find active fairino controller
        for info in topic_list:
            # self.get_logger().info(info[0])
            if re.search('fairino[0-50]_controller/joint_trajectory', info[0]) != None:
                joint_traj_topic = info[0]
                break
        if(joint_traj_topic == None):
            self.get_logger("Failed to find /fairino_controller")
            return
        self.publisher = self.create_publisher(JointTrajectory, joint_traj_topic, 10)
        timer_period = 2.0  # Delay to ensure controller is active
        self.timer = self.create_timer(timer_period, self.send_trajectory)
        self.sent = False

    def send_trajectory(self):
        if self.sent:
            return

        msg = JointTrajectory()
        msg.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']

        point = JointTrajectoryPoint()
        point.positions = [0.0, -0.5, 0.6, 0.0, 0.2, 0.0]
        point.time_from_start.sec = 2

        msg.points.append(point)

        self.get_logger().info('Publishing trajectory...')
        self.publisher.publish(msg)
        self.sent = True


def main(args=None):
    rclpy.init(args=args)
    node = SimTrajectoryPublisher()
    rclpy.spin_once(node, timeout_sec=5)  # Only send once and exit
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
