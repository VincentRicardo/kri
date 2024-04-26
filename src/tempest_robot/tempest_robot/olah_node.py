import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Float32MultiArray

def servo_calculation(gyro, cam):
    return 2

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
            #self.publish_data(servo_calculation(self.gyro, self.cam))
            self.get_logger().info("Mengirim Yaw: " + str(self.gyro[0]) + " Pitch: " + str(self.gyro[1]) + " Jarak: " + str(self.cam[0]) + " cm, Sudut: " + str(self.cam[1])) #servo_calculation(self.gyro, self.cam))
            self.cam_flag = False
            self.gyro_flag = False

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()