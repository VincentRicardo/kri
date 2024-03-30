import rclpy
from rclpy.node import Node
from nano0servo_interfaces.action import SendAngleN0
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle

from std_msgs.msg import String
from time import sleep
import serial

class SendAngle0ServerNode(Node):
    def __init__(self):
        super().__init__("service0_node")
        self.send_angle0_server = ActionServer(self, SendAngleN0, "nano0_action", execute_callback = self.sending_angle0)
        self.get_logger().info("Action server 0 has been started")
    
    def sending_angle0(self, goal_handle: ServerGoalHandle):
        #Get request
        check = goal_handle.request.check
        servo1 = goal_handle.request.servo1
        servo2 = goal_handle.request.servo2
        servo3 = goal_handle.request.servo3
        servo7 = goal_handle.request.servo7
        servo8 = goal_handle.request.servo8
        servo9 = goal_handle.request.servo9

        #Execute the action
        self.get_logger().info("Sending Angle to Nano 0")
        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.reset_input_buffer()
        ser.write((str(check) + " " + str(servo1) + " " + str(servo2) + " " + str(servo3) + " " + str(servo7) + " " + str(servo8) + " " + str(servo9)).encode('utf-8'))
        self.get_logger().info((str(check) + " " + str(servo1) + " " + str(servo2) + " " + str(servo3) + " " + str(servo7) + " " + str(servo8) + " " + str(servo9)).encode('utf-8'))
        # line = ser.readline().decode('utf-8').rstrip()
        # self.get_logger().info(line)
        #once done, set goal final state
        goal_handle.succeed()

        #and send the result
        result = SendAngleN0.Result()
        result.send = True
        return result

def main(args=None):
    rclpy.init(args=args)
    node = SendAngle0ServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
