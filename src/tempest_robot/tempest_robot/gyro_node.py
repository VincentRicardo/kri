#!/usr/bin/env python3
import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import String

import sys
from DFRobot_BMX160 import BMX160

bmx = BMX160(1)
measurement = 0
while not bmx.begin():
    pass


class MyNode(Node):                      
    def __init__(self):
        super().__init__("gyro_node")
        self.talking_one = self.create_publisher(String, "/gyro_", 1)
        self.subscriber_gyro = self.create_subscription(String, "/gyro_", self.kirim, 1)
    
    def kirim(self):
        message = String()
        message.data = measurement
        self.get_logger().info("Sending Gyro = " + message.data)
        self.talking_one.publish(message)
        measurement = 0

    while True:
        gyro= bmx.get_all_data()
        measurement = measurement + gyro[5]

    
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()
