#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial
import threading

class SerialControl(Node):

    def __init__(self):
        super().__init__('serial_control')

        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.get_logger().info("Connected to rover")

        thread = threading.Thread(target=self.keyboard_loop)
        thread.daemon = True
        thread.start()

    def keyboard_loop(self):

        while rclpy.ok():

            cmd = input("Enter command (f b l r s): ").strip()

            if cmd == 'f':
                self.send("m 50 50\n")

            elif cmd == 'b':
                self.send("m -50 -50\n")

            elif cmd == 'l':
                self.send("m 50 -50\n")

            elif cmd == 'r':
                self.send("m -50 50\n")

            elif cmd == 's':
                self.send("m 0 0\n")

    def send(self, msg):
        self.ser.write(msg.encode())
        self.get_logger().info(f"Sent: {msg.strip()}")

def main(args=None):
    rclpy.init(args=args)
    node = SerialControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()