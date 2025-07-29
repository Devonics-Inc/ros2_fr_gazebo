import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_share = get_package_share_directory('fairino_description')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + pkg_share
    else:
        gazebo_resource_path = pkg_share
    # gazebo_resource_path = os.pathsep + get_package_share_directory('fairino_description')

    # # if 'IGN_GAZEBO_RESOURCE_PATH' in os.environ:
    # os.environ['IGN_GAZEBO_RESOURCE_PATH'] = os.path.join(gazebo_resource_path)
    # print(gazebo_resource_path)

    nonrt_state_data_node = Node(
        package="fairino_hardware",
        executable="ros2_cmd_server",
    )
    
    joint_state_pub = Node(
        package="fairino3_v6_moveit2_config",
        executable="SimJointPublisher.py"
    )

    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('fairino3_v6_moveit2_config'),
                            'launch', 'rsp.launch.py')),
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ros_gz_sim'),
                            'launch', 'gz_sim.launch.py')),
    )
    
    
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=['-topic', 'robot_description'],
    )

    joint_state_broadcaster = ExecuteProcess(
        cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'joint_state_broadcaster'],
        output="screen"

    )

    fairino3_controller = ExecuteProcess(
        cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino3_controller'],
        output="screen"
    )

    
    # print(os.environ)

    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        nonrt_state_data_node,
        joint_state_pub,
        rsp,
        gazebo,
        spawn_robot,
        joint_state_broadcaster,
        fairino3_controller
    ])


