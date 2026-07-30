#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import socket, json
 
class JointForwarder(Node):
    def init(self):
        super().init('joint_state_bridge')
        print("Post super-init")
        self.pub = self.create_publisher(JointState, 'joint_states', 10)
        print("Pub created")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 5005))
        self.sock.setblocking(False)
        self.timer = self.create_timer(0.01, self.loop)
        print("Post init")
 
    def loop(self):
        print("Started loop")
        try:
            data = self.sock.recvfrom(4096)
            msg = json.loads(data.decode())
            js = JointState()
            js.header.stamp = self.getclock().now().to_msg()
            js.name = [f"j{i+1}" for i in range(6)]
            js.position = msg["joints"]
            self.get_logger(f"js.position")
            self.pub.publish(js)
        except BlockingIOError:
            self.get_logger("ioError")
            pass
 
def main(args=None):
    rclpy.init(args=args)
    print("Post init")
    node = JointForwarder('joint_forwarder')
    print("Created the obj")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()
