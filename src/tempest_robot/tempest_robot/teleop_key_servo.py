import rclpy
from rclpy.node import Node
from getkey import getkey, keys
from std_msgs.msg import Int32MultiArray
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.BUTTON = 21

GPIO.setup(GPIO.BUTTON, GPIO.IN)


class MyNode(Node):
    def __init__(self):
        super().__init__("teleop_key_servo")
        self.talking_one = self.create_publisher(Int32MultiArray, "/state", 10)
        self.timer_ = self.create_timer(0.1, self.send_message)
    def send_message(self):
        # if GPIO.input(GPIO.BUTTON)==1:
        #     self.get_logger().info("Aktif")
        key = getkey()
        message = Int32MultiArray()
        if key == 'w':
            self.get_logger().info("Maju") #yang diubah yang index 1 sama 4 sama 7
            message.data = [0, 30, 110, 180, 50, 70, 0, 65, 120, 180]
            self.talking_one.publish(message)
        elif key == 's':
            self.get_logger().info("Mundur") # yang diubah yang index 1 sama 4 sama 7
            message.data = [0, 80, 110, 180, 100, 70, 0, 15, 120, 180]
            self.talking_one.publish(message)
        # elif key == 'd':
        #     self.get_logger().info("Kanan")
        #     message.data = str(3)
        #     self.talking_one.publish(message)
        # elif key == 'a':
        #     self.get_logger().info("Kiri")
        #     message.data = str(4)
        #     self.talking_one.publish(message)
        elif key == ' ':
            self.get_logger().info("Berdiri")
            message.data = [1, 55, 110, 180, 75, 70 ,0, 40, 120, 180]
            self.talking_one.publish(message)
        else:
            self.get_logger().info("Wrong Key")
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()