#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from fairino_msgs.srv import RemoteCmdInterface  # Make sure this matches your package and srv name

class RemoteCommandClient(Node):

    def __init__(self):
        super().__init__('remote_command_client')
        self.cli = self.create_client(RemoteCmdInterface, '/fairino_remote_command_service')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting...')

    def send_command(self, command_str):
        req = RemoteCmdInterface.Request()
        req.cmd_str = command_str

        future = self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f'Result: {future.result()}')
        else:
            self.get_logger().error('Service call failed')


def main(args=None):
    rclpy.init(args=args)

    client = RemoteCommandClient()

    # EXAMPLES
    client.send_command("CARTPoint(1,-330,50,500,180,0,0)")
    client.send_command("MoveL(CART1,10)")

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
