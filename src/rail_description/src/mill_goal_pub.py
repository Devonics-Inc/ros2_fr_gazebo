#!/usr/bin/env python3

import rclpy, sys
from rclpy.node import Node
from sensor_msgs.msg import JointState

class MillJointPublisher(Node):


    def __init__(self, position):
        super().__init__('mill_joint_publisher')

        self.position = position

        self.publisher = self.create_publisher(
            JointState,
            '/joint_states',
            10
        )
        self.publish_joint_state()
        # self.timer = self.create_timer(
        #     0.1,
        #     self.publish_joint_state
        # )

    def publish_joint_state(self):

        msg = JointState()

        msg.header.stamp = self.get_clock().now().to_msg()

        msg.name = [
            'mill_to_door_joint'
        ]

        msg.position = [
            self.position
        ]

        self.publisher.publish(msg)


def main(args=None):
    if len(sys.argv) > 1:
        position = float(sys.argv[1])
    else:
        position = 0.0
    position = min(position, 0.5)

    rclpy.init(args=args)

    node = MillJointPublisher(position)

    rclpy.spin_once(node, timeout_sec=0.5)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()