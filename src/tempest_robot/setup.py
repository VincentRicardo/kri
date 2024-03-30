import os
from glob import glob
from setuptools import find_packages, setup


package_name = 'tempest_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]), 
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tempest',
    maintainer_email='tempest@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "teleop_key_servo = tempest_robot.teleop_key_servo:main",
            "service0_node = tempest_robot.service0_node:main",
            "nano_usb0 = tempest_robot.nano_usb0:main"
        ],
    },
)
