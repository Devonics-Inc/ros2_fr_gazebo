import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import(
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    ExecuteProcess,
    TimerAction
)
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution,
    PythonExpression
)
from launch.conditions import LaunchConfigurationEquals, LaunchConfigurationNotEquals, IfCondition
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import xacro

"""
THIS CREATES A DIGITAL FAIRINO, DETACHED FROM ANY HARDWARE

USE THE /joint_trajectory TO SEND GOAL STATES (use fairino_gazebo_config/launch/sim_trajectory_pub.py for an example) 

"""

def generate_launch_description():
    pkg_share = get_package_share_directory('fairino_description')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share
    else:
        gazebo_resource_path = pkg_share

    ####################
    # launch arguments #
    ####################

    # Declare root model
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

    moveit = LaunchConfiguration('moveit')
    moveit_arg = DeclareLaunchArgument(
        'moveit',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )
    #######################################
    # Add Nodes and external launch files #
    #######################################
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
        ' control_system:=gazebo'
    ])

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description}],
    )
    # ------------------------
    # Gazebo
    # ------------------------

    # Create an instance of Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ]),
        launch_arguments={'gz_args': [world, ' -r']}.items()
    )
    
    # Spawn the robot into gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            '-topic', 'robot_description'
        ],
    )

    # Robot state publisher
    # Spawn the joint_state_broadcaster for the gazebo robot
    joint_state_broadcaster = TimerAction(
        period=3.0,
        actions=[
            Node(
                package='controller_manager',
                executable='spawner',
                arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
                output='screen'
            )
        ]
    )

    controllers_yaml = os.path.join(pkg_share, 'config', 'ros2_controllers.yaml')

    # FOUND 
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

    # Spawn the fairino_controller for the gazebo robot
    controllers = [
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino3_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino3")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino5_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino5")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino10_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino10")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino16_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino16")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino20_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino20")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino30_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino30")
        )
    ]


    # -------------------- MOVEIT 2 CONTROLLER --------------------
    # Kinematics solver
    kinematics_yaml = PathJoinSubstitution([
        FindPackageShare(PythonExpression([
                "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
            ])),
            'config',
            'kinematics.yaml'
        ])
        

    # Created /tf translation for robot joints
    static_virtual_joint_tfs = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(PythonExpression([
                    "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
                ])),
                'launch',
                'static_virtual_joint_tfs.launch.py'
            ])
        ]),
        condition=IfCondition(LaunchConfiguration('moveit'))
    )


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
        launch_arguments={
            'use_sim_time': 'true'
        }.items(),
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
        moveit_arg,
        world_arg,
        robot_model_arg,
        gazebo,
        static_virtual_joint_tfs,
        rsp,
        move_group,
        controller_manager,
        joint_state_broadcaster,
        *controllers,
        spawn_robot,      
        moveit_obs_gen,
    ])