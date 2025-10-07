#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from gazebo_msgs.msg import ModelStates  # or the ROS-ign bridge equivalent
from geometry_msgs.msg import Pose
from std_msgs.msg import String
from your_msgs_pkg.srv import GetObstacleList  # you can define your own service/message types
"""
You’ll likely need to adapt it depending on what exact message types your ros_gz bridge uses
(for example, the topic name might be /model/pose/info or /world/…/model/…/pose/info in Ignition).
Also, the ModelStates message above is from gazebo_msgs (classic Gazebo); in Ignition, it might be different (e.g. ignition_msgs or gz_msgs).
But the pattern is:

    1. Subscribe to a message listing all models + poses

    2. Filter out non-obstacles (robot, ground)

    3. Republish or expose via a service / topic in a format your planner will consume

You might instead define a custom message like:

    string[] names
    geometry_msgs/Pose[] poses
    geometry_msgs/Vector3[] extents  # bounding box half-sizes or dims

"""
class GazeboWorldListener(Node):
    def __init__(self):
        super().__init__("gazebo_world_listener")
        # Subscribe to the model states topic (ros_gz bridge should bridge it)
        self.sub = self.create_subscription(
            ModelStates,
            "/gazebo/model_states",
            self.cb_model_states,
            10
        )
        # Publisher or service to send the obstacle list to planning node
        self.pub = self.create_publisher(String, "world_objects", 10)
        # Alternatively, define a custom message or service with name + pose + bounding box

    def cb_model_states(self, msg: ModelStates):
        # msg.name: list of model names
        # msg.pose: list of poses (same length)
        # msg.twist etc.
        # Filter out your robot itself (you don’t want robot as obstacle)
        obstacles = []
        for name, pose in zip(msg.name, msg.pose):
            if name == "your_robot_model_name":
                continue
            # Optionally exclude ground plane or world, etc.
            # For each obstacle, you might want its bounding box size (if known a priori)
            obstacles.append((name, pose))
        # Serialize or publish
        s = ""
        for (n, p) in obstacles:
            s += f"{n}:{p.position.x},{p.position.y},{p.position.z};"
        self.pub.publish(String(data=s))


def main(args=None):
    rclpy.init(args=args)
    node = GazeboWorldListener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
