from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lawn_mower',
            #namespace='turtlesim1',
            executable='lawn_mower_node',
            #name='sim'
        ),
    ])