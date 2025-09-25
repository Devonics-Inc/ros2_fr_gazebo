from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='fairino_gazebo_config',
            executable='sim_trajectory_pub',
            name='trajectory_sender',
            output='screen'
        )
    ])