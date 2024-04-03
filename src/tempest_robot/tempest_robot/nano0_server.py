import rclpy
from rclpy.node import Node
from nano0servo_interfaces.action import SendAngleN0
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle

from std_msgs.msg import String
from time import sleep
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
sleep(2)
class SendAngle0ServerNode(Node):
    def __init__(self):
        super().__init__("nano0_server")
        self.send_angle0_server = ActionServer(self, SendAngleN0, "nano0_action", execute_callback = self.sending_angle0)
        self.get_logger().info("Action server 0 has been started")
    
    def sending_angle0(self, goal_handle: ServerGoalHandle):
        #Get request
        for i in range(10):
            dat[i] = goal_handle.request.servo[i]
            
        check = goal_handle.request.check
        servo1 = goal_handle.request.servo1
        servo2 = goal_handle.request.servo2
        servo3 = goal_handle.request.servo3
        servo4 = goal_handle.request.servo4
        servo5 = goal_handle.request.servo5
        servo6 = goal_handle.request.servo6
        servo7 = goal_handle.request.servo7
        servo8 = goal_handle.request.servo8
        servo9 = goal_handle.request.servo9

        #Execute the action
        self.get_logger().info("Sending Angle to Nano 0")
        # ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        # sleep(2)
        ser.reset_input_buffer()
        kalimat = "{} {} {} {} {} {} {} {} {} {}".format(dat[0], dat[1], dat[2], dat[3], dat[4], dat[5], dat[6], dat[7], dat[8], dat[9])
        kalimat = "{} {} {} {} {} {} {} {} {} {}".format(check, servo1, servo2, servo3, servo4, servo5, servo6, servo7, servo8, servo9)
        ser.write(kalimat.encode())
        self.get_logger().info(kalimat)
        # line = ser.readline().decode().strip()
        # self.get_logger().info(line)

        #once done, set goal final state
        while True:
            numbercheck = ser.read()
            if numbercheck != b'':
                if int.from_bytes(numbercheck, byteorder = 'big') == 18:
                    goal_handle.succeed()
                    break

        #and send the result
        result = SendAngleN0.Result()
        # result.send = True
        result.servoo[0] = goal_handle.request.servo[0]
        for i in range(9):
            result.servoo[i+1] = goal_handle.request.servo[i+10]
        
        result.check2 = goal_handle.request.check
        result.servoo10 = goal_handle.request.servo10
        result.servoo11 = goal_handle.request.servo11
        result.servoo12 = goal_handle.request.servo12
        result.servoo13 = goal_handle.request.servo13
        result.servoo14 = goal_handle.request.servo14
        result.servoo15 = goal_handle.request.servo15
        result.servoo16 = goal_handle.request.servo16
        result.servoo17 = goal_handle.request.servo17
        result.servoo18 = goal_handle.request.servo18
        return result

def main(args=None):
    rclpy.init(args=args)
    node = SendAngle0ServerNode()
    rclpy.spin(node)
    rclpy.shutdown()
