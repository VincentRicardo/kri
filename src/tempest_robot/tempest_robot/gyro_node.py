#!/usr/bin/env python3
import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import String

from DFRobot_BMX160 import BMX160

bmx = BMX160(1)
measurement = 0
while not bmx.begin():
    pass


class MyNode(Node):                      
    def __init__(self):
        super().__init__("gyro_node")
        self.talking_one = self.create_publisher(String, "/gyro_", 1)
        self.subscriber_flag = self.create_subscription(String, "/flag", self.kirim_, 1)
        self.timer_ = self.create_timer(0.1, self.ngitung_gyro)
        self.measurement = 0
   
    def kirim_(self, message:String):
        info = String()   
        info.data = str(self.measurement)
        self.get_logger().info("Sending Gyro = " + str(self.measurement))
        self.talking_one.publish(info)
        self.measurement = 0

    def ngitung_gyro(self):
        gyro= bmx.get_all_data()
        if gyro[5] >= 0.1 or gyro[5] <= -0.1:
            self.measurement = self.measurement + gyro[5]
        #print(self.measurement)

    
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()
