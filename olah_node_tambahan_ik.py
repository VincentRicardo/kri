import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Float32MultiArray

import math

coxa = 5
femur = 6
tibia = 13
theta1_Zero = 0
theta2_Zero = 209.73539429556138
theta3_Zero = 63.74878606504425
alpha = 10

def servo_calculation(gyro, cam):
    derajat = [80, 90, 140, 65, 95 ,15, 40, 110, 180, 30, 80, 5, 65, 105, 170, 65, 95, 25]
    y = 3 #maju 3 cm, nilai cam distance ngaruh kesini
    x = 11 # lebarnya, nilai gyro yaw dan angle cam ngaruh kesini
    theta_1 = math.degrees(math.atan(y/x))
    theta_2 = (math.degrees(math.acos((pow(femur, 2) + pow((math.sqrt(pow (alpha, 2) + pow((math.sqrt(pow(x ,2) + pow(y, 2)) - coxa), 2))), 2) - pow (tibia, 2))/(2 * femur * (math.sqrt(pow (alpha, 2) + pow(math.sqrt(pow(x ,2) + pow(y, 2)) - coxa, 2))))))) + (math.degrees(math.atan((math.sqrt(pow(x ,2) + pow(y, 2)) - coxa)/alpha))) + 90 - theta2_Zero
    theta_3 = (math.degrees(math.acos((pow(femur, 2) + pow (tibia, 2) - pow((math.sqrt(pow (alpha, 2) + pow((math.sqrt(pow(x ,2) + pow(y, 2)) - coxa), 2))), 2))/(2 * femur * tibia)))) - theta3_Zero
    #bagian theta2 perlu dipikirkan lagi
    degree = []
    degree.append(derajat[0] - theta_1 - blabla)
    degree.append(derajat[1] - theta_2)
    degree.append(derajat[2] - theta_3)
    
    degree.append(derajat[3] - theta_1)
    
    return degree

class MyNode(Node):
    def __init__(self):
        super().__init__("olah_node")
        self.gyro_flag = False
        self.cam_flag = False
        self.subscriber_gyro = self.create_subscription(Float32MultiArray, "/gyro_", self.gyro_, 1)
        self.subscriber_cam = self.create_subscription(Float32MultiArray, "/cam_", self.cam_, 1)
        self.publish_data = self.create_publisher(Int32MultiArray, "/state", 1)
        self.timer_ = self.create_timer(0.1, self.send_calculate_message)
        self.cam = [0,0]
        self.gyro = [0,0]
    
    def cam_(self, message = Float32MultiArray):
        self.get_logger().info("Receiving Cam Distance = " + str(message.data[0]) + " cm & Angle = " + str(message.data[1]))
        
        self.cam = [message.data[0], message.data[1]]

        self.cam_flag = True

    def gyro_(self, message = Float32MultiArray):
        self.get_logger().info("Receiving Yaw = " + str(message.data[0])+ " & Pitch = " + str(message.data[1]))
        self.gyro = [message.data[0], message.data[1]]
        self.gyro_flag = True
        
    def send_calculate_message(self):
        if self.cam_flag == True and self.gyro_flag == True:
            #pub = servo_calculation(self.gyro, self.cam))
            #self.publish_data(pub)
            self.get_logger().info("Mengirim Yaw: " + str(self.gyro[0]) + " Pitch: " + str(self.gyro[1]) + " Jarak: " + str(self.cam[0]) + " cm, Sudut: " + str(self.cam[1])) 
            self.cam_flag = False
            self.gyro_flag = False

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()