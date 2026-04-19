#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

class WasdTeleop(Node):

    def __init__(self):
        super().__init__('wasd_teleop')

        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.get_logger().info("WASD Teleop Ready")
        self.get_logger().info("W Forward | S Back | A Left | D Right | SPACE Stop")

        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        listener.start()

    def publish_cmd(self, lin, ang):
        msg = Twist()
        msg.linear.x = lin
        msg.angular.z = ang
        self.pub.publish(msg)

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.publish_cmd(1.0, 0.0)

            elif key.char == 's':
                self.publish_cmd(-1.0, 0.0)

            elif key.char == 'a':
                self.publish_cmd(0.0, 1.0)

            elif key.char == 'd':
                self.publish_cmd(0.0, -1.0)

        except:
            if key == keyboard.Key.space:
                self.publish_cmd(0.0, 0.0)

    def on_release(self, key):
        try:
            if key.char in ['w', 'a', 's', 'd']:
                self.publish_cmd(0.0, 0.0)
        except:
            pass


def main(args=None):
    rclpy.init(args=args)
    node = WasdTeleop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()