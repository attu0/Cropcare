#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial
import time

class CmdVelSerial(Node):

    def __init__(self):
        super().__init__('cmd_vel_serial')

        self.ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1)
        time.sleep(2)

        self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

        self.get_logger().info("Listening to /cmd_vel")

    def cmd_callback(self, msg):

        lin = msg.linear.x
        ang = msg.angular.z

        left = int((lin - ang) * 70)
        right = int((lin + ang) * 70)

        left = max(-100, min(100, left))
        right = max(-100, min(100, right))

        cmd = f"m {left} {right}\n"
        self.ser.write(cmd.encode())

        self.get_logger().info(cmd.strip())

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelSerial()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()