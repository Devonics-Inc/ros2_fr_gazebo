import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable, ExecuteProcess
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution
)
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import xacro

"""

DEPRECIATED!

"""



def generate_launch_description():
    pkg_share = get_package_share_directory('fairino_description')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share
    else:
        gazebo_resource_path = pkg_share

   
    # Declare world file (default to empty)
    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument(
        'world',
        default_value="empty.sdf",
        description="Name of world file to spawn robot into"
    )
    
    # control_system_arg = DeclareLaunchArgument(
    #     'control_system',
    #     default_value='gazebo',
    #     description='Specify which control system to use (moveit or gazebo mirroring)'
    # )

    # Declare root model; Currently does nothing, can be used in the future for allowing multi-robot model functionality
    robot_model_arg = DeclareLaunchArgument(
        'robot_model',
        default_value="fairino5",
        description="Name of robot model to spawn (ie. Fairino3)")

    gripper_arg = DeclareLaunchArgument(
        'gripper',
        default_value='None',
        description='Type of gripper to attach to wrist3_link'
    )

    mount_arg = DeclareLaunchArgument(
        'mount',
        default_value='None',
        description='Type of mount object to attach under base_link'
    )


    # Connect the ros2_cmd_server for publishing the /nonrt_state_data of the robot
    nonrt_state_data_node = Node(
        package="fairino_hardware",
        executable="ros2_cmd_server",
    )
    
    # Translate the /nonnrt_state_data for the /joint_states topic
    """     USING /non_rt_state_data (DEPRECIATED)   """
    # joint_state_pub = Node(
    #     package="fairino_gazebo_config",
    #     executable="SimJointPublisher.py",
    #     parameters=[{'robot_model': LaunchConfiguration("robot_model")}]
    # )

    """     USING ROBOT_STATE_PKG SOCKET    """
    joint_state_pub = Node(
        package="fairino_gazebo_config",
        executable="rt_state_data.py",
        parameters=[{'robot_model': LaunchConfiguration("robot_model")}]
    )

    # RSP v2
    file_subpath = 'config/fairino5_v6_robot.urdf.xacro'
    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory('fairino5_v6_moveit2_config'),file_subpath)
    robot_description_raw = xacro.process_file(
        xacro_file,
        mappings={
            'control_system': 'gazebo'
    }).toxml()

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description_raw}],
    )

    # Create an instance of Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ]),
        #launch_arguments={'gz_args': [ ' -r']}.items()
        launch_arguments={'gz_args': [world, ' -r']}.items()
    )
    
    # Spawn the robot into gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=['-topic', 'robot_description'],
    )

    # Spawn the joint_state_broadcaster for the gazebo robot
    joint_state_broadcaster = ExecuteProcess(
        cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'joint_state_broadcaster'],
        output="screen"
    )

    # Spawn the fairino5_controller for the gazebo robot
    fairino5_controller = ExecuteProcess(
        cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino5_controller'],
        output="screen"
    )

    
    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        world_arg,
        # mount_arg,
        # gripper_arg,
        robot_model_arg,
        nonrt_state_data_node,
        joint_state_pub,
        rsp,
        joint_state_broadcaster,
        fairino5_controller,
        gazebo,
        spawn_robot
    ])
