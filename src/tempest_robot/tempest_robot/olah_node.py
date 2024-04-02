import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import Int32MultiArray
from time import sleep

def servo_calculation(gyro, cam):
    pass

class MyNode(Node):
    def __init__(self):
        super().__init__("olah_node")
        self.subscriber_gyro = self.create_subscription(Int32, "/gyro_", self.gyro_, 1)
        self.subscriber_cam = self.create_subscription(Int32, "/cam_", self.cam_, 1)
        self.publish_data = self.create_publish(Int32MultiArray, "/state", 10)
    
    def cam(self):
        pass
    def gyro(self):
        pass
        
            

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()