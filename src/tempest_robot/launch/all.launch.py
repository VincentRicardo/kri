from launch import LaunchDescription
import launch_ros.actions
from getkey import getkey, keys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.BUTTON = 21
GPIO.LED = 16

GPIO.setup(GPIO.BUTTON, GPIO.IN)
GPIO.setup(GPIO.LED, GPIO.OUT)
GPIO.output(GPIO.LED, GPIO.LOW)

def generate_launch_description():
    print("Menunggu button")
    GPIO.output(GPIO.LED, GPIO.HIGH)
    while True:
        if GPIO.input(GPIO.BUTTON)==1:
            print("Sistem Aktif")
            GPIO.output(GPIO.LED, GPIO.LOW)
            return LaunchDescription([
                launch_ros.actions.Node(
                    package = 'tempest_robot', executable= 'nano0_server'),
                launch_ros.actions.Node(
                     package = 'tempest_robot', executable = 'nano1_server'),
                launch_ros.actions.Node(
                    package = 'tempest_robot', executable = 'sending_angle'),
                #launch_ros.actions.Node(
                    #package = 'tempest_robot', executable = 'gyro_node'),
                #launch_ros.actions.Node(
                    #package = 'tempest_robot', executable = 'camera_node'),
                #launch_ros.actions.Node(
                    #package = 'tempest_robot', executable = 'olah_node'
                
            ])
            break
    # return LaunchDescription([
    #     launch_ros.actions.Node(
    #         package = 'tempest_robot', executable= 'nano0_server'),
    #     launch_ros.actions.Node(
    #         package = 'tempest_robot', executable = 'nano1_server'),
    #     launch_ros.actions.Node(
    #         package = 'tempest_robot', executable = 'sending_angle'),
    # ])
