import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle
from nano0servo_interfaces.action import SendAngleN0

from std_msgs.msg import Int32MultiArray
from time import sleep

class SendAngle0ClientNode(Node):
    def __init__(self):
        super().__init__("sending_angle")
        self.subscriber_sudut0 = self.create_subscription(Int32MultiArray, "/state", self.data_, 1)
        self.send_angle0_client = ActionClient(self, SendAngleN0, "nano0_action")
        self.send_angle1_client = ActionClient(self, SendAngleN0, "nano1_action")

    def data_ (self, message: Int32MultiArray):
        #Wait for server
        self.send_angle0_client.wait_for_server()

        #Create a goal
        goal = SendAngleN0.Goal()
        goal.check = message.data[0]
        goal.servo1 = message.data[1]
        goal.servo2 = message.data[2]
        goal.servo3 = message.data[3]
        goal.servo4 = message.data[4]
        goal.servo5 = message.data[5]
        goal.servo6 = message.data[6]
        goal.servo7 = message.data[7]
        goal.servo8 = message.data[8]
        goal.servo9 = message.data[9]
        goal.servo10 = message.data[10]
        goal.servo11 = message.data[11]
        goal.servo12 = message.data[12]
        goal.servo13 = message.data[13]
        goal.servo14 = message.data[14]
        goal.servo15 = message.data[15]
        goal.servo16 = message.data[16]
        goal.servo17 = message.data[17]
        goal.servo18 = message.data[18]


        #send the goal
        self.get_logger().info("Sending Angle 0 Data")
        self.send_angle0_client.send_goal_async(goal).add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        self.goal_handle_: ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
            self.goal_handle_.get_result_async().add_done_callback(self.goal_result_callback)
    
    def goal_result_callback(self, future):
        self.send_angle1_client.wait_for_server()

        goal = SendAngleN0.Goal()
        result = future.result().result
        goal.check = result.check2
        goal.servo10 = result.servoo10
        goal.servo11 = result.servoo11
        goal.servo12 = result.servoo12
        goal.servo13 = result.servoo13
        goal.servo14 = result.servoo14
        goal.servo15 = result.servoo15
        goal.servo16 = result.servoo16
        goal.servo17 = result.servoo17
        goal.servo18 = result.servoo18

        #send the goal
        self.get_logger().info("Sending Angle 1 Data")
        self.send_angle1_client.send_goal_async(goal)



def main(args=None):
    rclpy.init(args=args)
    node = SendAngle0ClientNode()
    rclpy.spin(node)
    rclpy.shutdown()