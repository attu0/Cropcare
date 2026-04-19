from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    articubot_dir = get_package_share_directory('articubot_one')

    camera_launch = os.path.join(
        articubot_dir,
        'launch',
        'camera.launch.py'
    )

    lidar_launch = os.path.join(
        articubot_dir,
        'launch',
        'rplidar.launch.py'
    )

    return LaunchDescription([

        # Serial rover bridge
        Node(
            package='Cropcare',
            executable='cmd_vel_serial',
            output='screen'
        ),

        # WASD keyboard
        Node(
            package='Cropcare',
            executable='wasd_teleop',
            output='screen'
        ),

        # Joystick
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

        # Camera
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(camera_launch)
        ),

        # Lidar
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(lidar_launch)
        ),
    ])