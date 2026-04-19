#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial
import time
from pynput import keyboard

class SerialTeleop(Node):

    def __init__(self):
        super().__init__('serial_teleop')

        # Serial connection
        self.ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1)
        time.sleep(2)

        self.current_cmd = "m 0 0\n"

        self.get_logger().info("Connected to rover")
        self.get_logger().info("Controls:")
        self.get_logger().info("W = Forward")
        self.get_logger().info("S = Back")
        self.get_logger().info("A = Left")
        self.get_logger().info("D = Right")
        self.get_logger().info("SPACE = Stop")

        # Start keyboard listener
        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

        # Send command continuously
        self.create_timer(0.1, self.send_command)

    def on_press(self, key):
        try:
            if key.char == 'w':
                self.current_cmd = "m 70 70\n"

            elif key.char == 's':
                self.current_cmd = "m -70 -70\n"

            elif key.char == 'a':
                self.current_cmd = "m 70 -70\n"

            elif key.char == 'd':
                self.current_cmd = "m -70 70\n"

        except AttributeError:
            if key == keyboard.Key.space:
                self.current_cmd = "m 0 0\n"

    def on_release(self, key):
        # Stop when movement key released
        try:
            if key.char in ['w', 'a', 's', 'd']:
                self.current_cmd = "m 0 0\n"
        except:
            pass

    def send_command(self):
        self.ser.write(self.current_cmd.encode())

def main(args=None):
    rclpy.init(args=args)
    node = SerialTeleop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()