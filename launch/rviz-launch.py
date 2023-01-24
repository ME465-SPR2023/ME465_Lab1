from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    lab1_share = get_package_share_directory("ME465_Lab1")
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=[
            "-d",
            os.path.join(lab1_share, "lab1.rviz"),
        ],
    )
    return LaunchDescription([
        rviz,
    ])
