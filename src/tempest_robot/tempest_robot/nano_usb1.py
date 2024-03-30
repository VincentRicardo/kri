import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep
import serial

class MyNode(Node):
    def __init__(self):
        super().__init__("nano_usb1")
        self.subscriber_sudut0 = self.create_subscription(String, "/sudut1", self.repeat_, 1)
    
    def repeat_(self, message:String):
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.reset_input_buffer()
        ser.write(str(message.data).encode('utf-8'))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()