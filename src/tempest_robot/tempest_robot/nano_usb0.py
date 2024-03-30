import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nano0servo_interfaces.action import SendAngleN0

from std_msgs.msg import Int32MultiArray
from time import sleep

class SendAngle0ClientNode(Node):
    def __init__(self):
        super().__init__("nano_usb0")
        self.subscriber_sudut0 = self.create_subscription(Int32MultiArray, "/state", self.data_, 10)
        self.send_angle0_client = ActionClient(self, SendAngleN0, "nano0_action")

    def data_ (self, message: Int32MultiArray):
        #Wait for server
        self.send_angle0_client.wait_for_server()

        #Create a goal
        goal = SendAngleN0.Goal()
        goal.check = message.data[0]
        goal.servo1 = message.data[1]
        goal.servo2 = message.data[2]
        goal.servo3 = message.data[3]
        goal.servo7 = message.data[4]
        goal.servo8 = message.data[5]
        goal.servo9 = message.data[6]

        #send the goal
        self.get_logger().info("Sending Angle 0 Data")
        self.send_angle0_client.send_goal_async(goal)




def main(args=None):
    rclpy.init(args=args)
    node = SendAngle0ClientNode()
    rclpy.spin(node)
    rclpy.shutdown()