import rclpy
from rclpy.node import Node
from nano0servo_interfaces.action import SendAngleN0
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle

from std_msgs.msg import String
from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
sleep(2)
class SendAngle1ServerNode(Node):
    def __init__(self):
        super().__init__("nano1_server")
        self.send_angle1_server = ActionServer(self, SendAngleN0, "nano1_action", execute_callback = self.sending_angle0)
        self.get_logger().info("Action server 1 has been started")
    
    def sending_angle0(self, goal_handle: ServerGoalHandle):
        #Get request
        
        dat[0] = goal_handle.request.servo[0]
        for i in range(10,19):
            dat[i-9] = goal_handle.request.servo[i]
            
        check = goal_handle.request.check
        servo10 = goal_handle.request.servo10
        servo11 = goal_handle.request.servo11
        servo12 = goal_handle.request.servo12
        servo13 = goal_handle.request.servo13
        servo14 = goal_handle.request.servo14
        servo15 = goal_handle.request.servo15
        servo16 = goal_handle.request.servo16
        servo17 = goal_handle.request.servo17
        servo18 = goal_handle.request.servo18

        #Execute the action
        self.get_logger().info("Sending Angle to Nano 0")
        # ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        # sleep(2)
        ser.reset_input_buffer()
        kalimat = "{} {} {} {} {} {} {} {} {} {}".format(dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6], dat[7], dat[8], dat[9])
        kalimat = "{} {} {} {} {} {} {} {} {} {}".format(check, servo10, servo11, servo12, servo13, servo14, servo15, servo16, servo17, servo18)
        ser.write(kalimat.encode())
        self.get_logger().info(kalimat)
        # line = ser.readline().decode().strip()
        # self.get_logger().info(line)

        #once done, set goal final state
        goal_handle.succeed()

        #and send the result
        result = SendAngleN0.Result()
        result.send1 = True
        return result

def main(args=None):
    rclpy.init(args=args)
    node = SendAngle1ServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
