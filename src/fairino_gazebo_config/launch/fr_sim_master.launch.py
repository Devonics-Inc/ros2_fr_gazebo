import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    ExecuteProcess
)
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution,
    PythonExpression
)
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import LaunchConfigurationEquals, LaunchConfigurationNotEquals, IfCondition
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution, LaunchConfiguration
import xacro

"""
THIS CREATES A DIGITAL FAIRINO, THAT MIRRORS THE ROBOT AT THE IP ADDRESS SET IN /rt_state_data

USE NORMAL CONTROL FOR YOUR ROBOT AND THE GAZEBO BOT WILL FOLLOW

"""

def generate_launch_description():
    # Adds fairino_description to IGN_GAZEBO_RESOURCE_PATH so gazebo can find the models
    pkg_share = get_package_share_directory('fairino_description')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share
    else:
        gazebo_resource_path = pkg_share

    # -------------------- Launch Arguments --------------------

    # Declare default robot model and allow argument for changing it
    robot_model = LaunchConfiguration('robot_model')
    robot_model_arg = DeclareLaunchArgument(
        'robot_model',
        default_value="fairino5",
        description="Name of robot model to spawn (ie. Fairino3)"
    )

    # Declare world file (default to empty)
    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument(
        'world',
        default_value="empty.sdf",
        description="Name of world file to spawn robot into"
    )

    # Uses different joint publishers for SDK and ROS
    control_method = LaunchConfiguration('sdk')
    control_method_arg = DeclareLaunchArgument(
        'sdk',
        default_value="False",
        description="True if using the SDK for robot control, false if using ROS"
    )

    # Allow user to enable moveit controller and obstacle porting from gazebo
    moveit = LaunchConfiguration('moveit')
    moveit_arg = DeclareLaunchArgument(
        'moveit',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )
    
    # Argument to enable Gazebo integration
    useSim = LaunchConfiguration('use_sim')
    useSim_arg = DeclareLaunchArgument(
        'use_sim',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )


    # -------------------- ROBOT DESCRIPTION --------------------
    # PASS PROPER CONTROL ARGUMENT TO XACRO BASED ON ARGS
    control_system_arg = PythonExpression([
        "'control_system:=gazebo' if '", LaunchConfiguration('use_sim'), "' == 'true' else 'control_system:=moveit'"
    ])
    robot_description = Command([
        FindExecutable(name='xacro'),
        ' ',
        PathJoinSubstitution([
            FindPackageShare(PythonExpression([
                "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
            ])),
            'config',
            PythonExpression([
                "'", LaunchConfiguration('robot_model'), "_v6_robot.urdf.xacro'"
            ])
        ]),
        ' ',
        control_system_arg
    ])

    # Spawn static virtual joint tf
    static_virtual_joint_tfs = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(PythonExpression([
                    "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
                ])),
                'launch',
                'static_virtual_joint_tfs.launch.py'
            ])
        ])
    )
    # Spawn robot_state_publisher
    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description}],
    )


    # -------------------- Gazebo --------------------
    # Create an instance of Gazebo with the specified world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ]),
        launch_arguments={
            'gz_args': ['src/fairino_gazebo_config/worlds/low_temp.sdf', ' -r']

        }.items(),
        condition=IfCondition(LaunchConfiguration('use_sim'))
    )
    
    # Spawn the robot into gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=['-topic', 'robot_description', '-x', '0.0', '-y','0.0',  '-z','0.04',  '-R','0.0',  '-P', '0.0', '-Y','0.0'],
        condition=IfCondition(LaunchConfiguration('use_sim')),
    )

    # -------------------- CONTROLLERS --------------------
    # Grab appropriate control yaml 
    controllers_yaml = PathJoinSubstitution([
        FindPackageShare(PythonExpression([
            "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
        ])),
        'config',
        'ros2_controllers.yaml'
    ])
    # Create controller manager
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            {'robot_description': robot_description},
            controllers_yaml
        ],
        remappings=[
            ("/controller_manager/robot_description", "/robot_description"),
        ],
        output='screen'
    )

    # Spawn the joint_state_broadcaster
    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )

    # Spawn the fairino_controller for the gazebo robot
    controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[PythonExpression(["'", LaunchConfiguration('robot_model'), "_controller'"])],
        output="screen",
    )

    # -------------------- MOVEIT 2 CONTROLLER --------------------
    # Move Group parameters for moveit control - NOW WITH KINEMATICS CONFIG
    move_group = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(PythonExpression([
                    "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
                ])),
                'launch',
                'move_group.launch.py'
            ])
        ]),
        launch_arguments={'use_sim_time': 'True'}.items(),
        condition=IfCondition(LaunchConfiguration('moveit'))
    )

    # World file -> MoveIt collision parser
    moveit_obs_gen = Node(
        package="fairino_gazebo_config",
        executable="gazebo_world_to_moveit.py",
        arguments=[world],
        condition=IfCondition(LaunchConfiguration('moveit')),
        parameters=[{"use_sim_time": True}]
    )

    
    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        robot_model_arg,
        world_arg,
        control_method_arg,
        moveit_arg,
        useSim_arg,
        static_virtual_joint_tfs,
        rsp,
        controller_manager,
        joint_state_broadcaster,
        controller,
        spawn_robot,
        gazebo,
        move_group,
        moveit_obs_gen
    ])
