from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        Node(
            package='Cropcare',
            executable='cmd_vel_serial',
            output='screen'
        ),

        Node(
            package='Cropcare',
            executable='wasd_teleop',
            output='screen'
        ),

        Node(
            package='joy',
            executable='joy_node',
            output='screen'
        ),

        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            output='screen'
        ),
    ])