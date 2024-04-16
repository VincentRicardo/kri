import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray

def servo_calculation(gyro, cam):
    pass

class MyNode(Node):
    def __init__(self):
        super().__init__("olah_node")
        self.subscriber_gyro = self.create_subscription(String, "/gyro_", self.gyro_, 1)
        self.subscriber_cam = self.create_subscription(String, "/cam_", self.cam_, 1)
        self.publish_data = self.create_publish(Int32MultiArray, "/state", 1)
    
    def cam(self, message = String):
        pass

    def gyro(self, message = String):
        self.get_logger().info("Receiving Gyro = " + message.data)
        
            

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()