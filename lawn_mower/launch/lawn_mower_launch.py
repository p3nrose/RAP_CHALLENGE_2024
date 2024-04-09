import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction, OpaqueFunction
from launch.substitutions import LaunchConfiguration, Command, FindExecutable, PathJoinSubstitution
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lawn_mower',
            #namespace='turtlesim1',
            executable='lawn_mower_node',
            #name='sim'
        ),
        # Arguments
        DeclareLaunchArgument(
            'model',
            default_value=LaunchConfiguration('model', default='waffle'),
            description='model type [burger, waffle, waffle_pi]'
        ),
        DeclareLaunchArgument(
            'map_file',
            default_value=os.path.join(get_package_share_directory('lawn_mower'), 'maps', 'turtlebot3_world.yml'), #nav2 bringup launch.py
            description='Full path to the map file to load'
        ),
        DeclareLaunchArgument(
            'open_rviz',
            default_value='true',
            description='Launch RViz?'
        ),
        DeclareLaunchArgument(
            'move_forward_only',
            default_value='false',
            description='Robot moves forward only?'
        ),

        # Turtlebot3
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindExecutable(name='turtlebot3_bringup'), 'launch', 'turtlebot3_remote.launch.py'
                ])
            ]),
            launch_arguments={'model': LaunchConfiguration('model')}.items(),
        ),

        # RViz
        GroupAction(
            actions=[
                Node(
                    package='rviz',
                    executable='rviz',
                    name='rviz',
                    output='screen',
                    arguments=[
                        '-d', PathJoinSubstitution([
                            FindExecutable(name='turtlebot3_navigation'), 'rviz', 'turtlebot3_navigation.rviz'
                        ])
                    ],
                    condition=IfCondition(LaunchConfiguration('open_rviz'))
                )
            ],
            condition=IfCondition(LaunchConfiguration('open_rviz'))
        ),
    ])