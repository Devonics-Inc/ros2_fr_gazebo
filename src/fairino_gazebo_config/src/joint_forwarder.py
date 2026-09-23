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
from RolandRobot import RolandRobot


class ROS2Forwarder(Node):
    def __init__(self, robot):
        super().__init__('ros2_forwarder')
        self.robot = robot
        self.timer = self.create_timer(0.01, self.publish_state)
        self.joint_names = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        self.traj_pub = self.create_publisher(
            JointTrajectory, f'fairino5_controller/joint_trajectory', 10
        )
        self.mill_traj_pub = self.create_publisher(
            JointTrajectory, f'sync_table2_controller/joint_trajectory', 10
        )
        self.door_joint = 0.0
        self.top_drawer_pos = 0.0
        self.btm_drawer_pos = 0.0

        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = self.joint_names + ["sync_table2_joint", "bottom_drawer_joint", "top_drawer_joint"]
        js.position = [math.radians(self.robot.robot_state_pkg.jt_cur_pos[i]) for i in range(6)] + [self.door_joint, float(0.4), float(0.0)]
        self.pub.publish(js)

    def publish_state(self):

        poses = [math.radians(self.robot.robot_state_pkg.jt_cur_pos[i]) for i in range(6)]

        # if(self.top_drawer_queue or self.btm_drawer_queue):            
        #     js = JointState()
        #     js.header.stamp = self.get_clock().now().to_msg()
        #     js.name = []
        #     js.position = []
        #     if(self.top_drawer_queue):
        #         js.name.append("top_drawer_joint")
        #         js.position.append(self.top_drawer_queue.pop(0))
        #     if(self.btm_drawer_queue):
        #         js.name.append("bottom_drawer_joint")
        #         js.position.append(self.btm_drawer_queue.pop(0))
                            
        #     self.pub.publish(js)

        traj_msg = JointTrajectory()
        traj_msg.joint_names = self.joint_names
        point = JointTrajectoryPoint()
        point.positions = poses
        point.time_from_start = Duration(sec=0, nanosec=10000000)
        traj_msg.points.append(point)
        self.traj_pub.publish(traj_msg)

        mill_traj_msg = JointTrajectory()
        mill_traj_msg.joint_names = ['sync_table2_joint', 'top_drawer_joint', 'bottom_drawer_joint']
        mill_point = JointTrajectoryPoint()
        mill_point.positions = [float(self.door_joint), float(self.top_drawer_pos), float(self.btm_drawer_pos)]
        mill_point.time_from_start = Duration(sec=0, nanosec=250000000)
        mill_traj_msg.points.append(mill_point)
        self.mill_traj_pub.publish(mill_traj_msg)




def main():
    robot = RolandRobot(isSim=True)
    rclpy.init()
    ros_node = ROS2Forwarder(robot)
    poses = [math.radians(ros_node.robot.robot_state_pkg.jt_cur_pos[i]) for i in range(6)]
            
    js = JointState()
    js.header.stamp = ros_node.get_clock().now().to_msg()
    js.name = ros_node.joint_names + ["sync_table2_joint", "bottom_drawer_joint", "top_drawer_joint"]
    js.position = poses + [ros_node.door_joint, float(0.0), float(0.0)]
    ros_node.pub.publish(js)
    ros_thread = threading.Thread(target=rclpy.spin, args=(ros_node,), daemon=False)
    ros_thread.start()
    jp1, cp = robot.getPoseFromDB("MILL_POSES", "home")
    jp2, cp = robot.getPoseFromDB("MILL_POSES", "tending")
    # TradeShowLoop(robot)
    count = 0
    while(True):
        # TestFunc(robot)
        robot.MoveJ(jp1, 1, 0)
        robot.MoveJ(jp2, 1, 0)
        count += 1
        ros_node.door_joint = float(0.1 * (count % 6))
        ros_node.top_drawer_joint = float(0.1 * (count % 6))
        ros_node.btm_drawer_joint = float(0.1 * (count % 6))


if __name__ == "__main__":
    main()