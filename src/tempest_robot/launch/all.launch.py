from launch import LaunchDescription
import launch_ros.actions
from getkey import getkey, keys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.BUTTON = 21

GPIO.setup(GPIO.BUTTON, GPIO.IN)

def generate_launch_description():
    # while True:
    #     if GPIO.input(GPIO.BUTTON)==1:
    #         print("Sistem Aktif")
    #         return LaunchDescription([
    #             launch_ros.actions.Node(
    #                 package='tempest_robot', executable = 'teleop_key_servo')
    #         ])
    #         break
    return LaunchDescription([
        launch_ros.actions.Node(
            package = 'tempest_robot', executable= 'nano_usb0'),
        launch_ros.actions.Node(
            package = 'tempest_robot', executable = 'service0_node')
    ])