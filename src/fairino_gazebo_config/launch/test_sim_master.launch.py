import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    ExecuteProcess,
    TimerAction,
    LogInfo
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
import yaml
import sys
"""
THIS CREATES A DIGITAL FAIRINO, THAT MIRRORS THE ROBOT AT THE IP ADDRESS SET IN /rt_state_data

USE NORMAL CONTROL FOR YOUR ROBOT AND THE GAZEBO BOT WILL FOLLOW

"""

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:  # parent of IOError, OSError *and* WindowsError where available
        return None


def generate_launch_description():
    pkg_share = get_package_share_directory('fairino_description')
    rail_pkg_share = get_package_share_directory('rail_description')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share + ':' + rail_pkg_share
    else:
        gazebo_resource_path = pkg_share + ':' + rail_pkg_share

    ####################
    # launch arguments #
    ####################
    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument(
        'world',
        default_value="empty.sdf",
        description="Name of world file to spawn robot into"
    )
    # Declare robot model
    robot_model = LaunchConfiguration('robot_model')
    robot_model_arg = DeclareLaunchArgument(
        'robot_model',
        default_value="fairino5",
        description="Name of robot model to spawn (ie. Fairino3)",
        choices=[
            'fairino3',
            'fairino5',
            'fairino10',
            'fairino16',
            'fairino20',
            'fairino30',
        ]
    )
    # Declare robot mount
    mount = LaunchConfiguration('mount')
    mount_arg = DeclareLaunchArgument(
        'mount',
        default_value="world",
        description="Name of object to mount robot to (ie. world or rail_carriage)"
    )


    moveit = LaunchConfiguration('moveit')
    moveit_arg = DeclareLaunchArgument(
        'moveit',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )
    
    useSim = LaunchConfiguration('gazebo')
    useSim_arg = DeclareLaunchArgument(
        'gazebo',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )

    # PASS PROPER CONTROL ARGUMENT BASED ON CLI ARGS
    control_system_arg = PythonExpression([
        "'control_system:=gazebo' if '", LaunchConfiguration('gazebo'), "' == 'true' else 'control_system:=moveit'"
    ])


    robot_model_str = "fairino5"  # default
    for arg in sys.argv:
        if arg.startswith("robot_model:="):
            print("\n\n\n\n" , arg, "\n\n\n")
            robot_model_str = arg.split(":=")[1]
            print("\n\n\n\n" , robot_model_str, "\n\n\n")

    moveit_pkg_map = {
        "fairino3":  "fairino3_v6_moveit2_config",
        "fairino5":  "fairino5_v6_moveit2_config",
        "fairino10": "fairino10_v6_moveit2_config",
        "fairino16": "fairino16_v6_moveit2_config",
        "fairino20": "fairino20_v6_moveit2_config",
        "fairino30": "fairino30_v6_moveit2_config",
    }

    robot_description = Command([
        FindExecutable(name='xacro'),
        ' ',
        PathJoinSubstitution([
            FindPackageShare('fairino_description'),
            'robots',
            "test_fairino.urdf.xacro"
        ]),
        ' ',
        "robot_model:=", robot_model_str,
        ' ',
        "robot_mount:=", LaunchConfiguration('mount'),
        ' ',
        control_system_arg,
        ' ',
    ])

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        respawn=True,
        output="screen",
        parameters=[{"robot_description": robot_description}, {"use_sim_time":False}],
    )

    ##########################################################
    # ------------------------
    # Gazebo
    # ------------------------
    # Create an instance of Gazebo
    
    
    moveit_pkg = moveit_pkg_map.get(robot_model_str, "fairino5_v6_moveit2_config")

    controllers_yaml_path = os.path.join(
        get_package_share_directory(moveit_pkg),
        "config",
        "ros2_controllers.yaml"
    )


    # Load controllers into controller manager
    controllers_yaml = load_yaml(moveit_pkg, "config/ros2_controllers.yaml")
    controllers_yaml_path = os.path.join(
        get_package_share_directory(moveit_pkg),
        "config",
        "ros2_controllers.yaml"
    )
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            # {'use_sim_time': False},
            controllers_yaml_path
        ],
        remappings=[
            ("/controller_manager/robot_description", "/robot_description")
        ],
        output='screen',
    )

    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            {'use_sim_time': False},
            controllers_yaml_path,   # ← file path string, not parsed dict
        ],
        remappings=[
            ("/controller_manager/robot_description", "/robot_description")
        ],
        output='screen',
    )


    # Spawn the joint_state_broadcaster for the gazebo robot
    joint_state_broadcaster = TimerAction(
        period=1.0,
        actions=[
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=[
                    "joint_state_broadcaster",
                    "-c", "/controller_manager",
                    "--param-file", controllers_yaml_path,  # ← add this
                ],
                output="screen",
            )
        ]
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
        launch_arguments={
            'use_sim_time': LaunchConfiguration('gazebo'),
            'robot_model': robot_model,
            'robot_mount': LaunchConfiguration('mount'),
            'gazebo': LaunchConfiguration('gazebo'),
        
        }.items(),
        condition=IfCondition(LaunchConfiguration('moveit'))
    )

    static_tfs = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(PythonExpression([
                    "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
                ])),
                'launch',
                'static_virtual_joint_tfs.launch.py'
            ])
        ]),
        condition=LaunchConfigurationNotEquals('gazebo', 'true')
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', PathJoinSubstitution([
            FindPackageShare(PythonExpression([
                "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
            ])),
            'config',
            'moveit.rviz'
        ])],
        condition=IfCondition(LaunchConfiguration('moveit')),
        parameters=[{"use_sim_time": False}]
    )


    # Grab controllers to load
    fairino_controller_name = [PythonExpression([
        "'", LaunchConfiguration('robot_model'), "_controller'"
    ])]
    
    mount_controller = [PythonExpression([
        "'", LaunchConfiguration('mount'), "_controller'"
    ])]

        
    # Pass controllers into controller spawner
    fairino_controller = TimerAction(
        period=1.0,
        actions=[
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=[
                    fairino_controller_name,
                    "-c", "/controller_manager",
                    "--controller-manager-timeout", "10",
                    "--param-file", controllers_yaml_path,  # ← add this
                ],
                output="screen",
            ),
        ],
    )

    rail_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[mount_controller,
                   "-c", "/controller_manager",
                   "-t", "joint_trajectory_controller/JointTrajectoryController"
        ],
        condition=LaunchConfigurationNotEquals('mount', 'world'),
        respawn=True,
        output="screen",
    )

    # Spawn gazebo
    world_string = PythonExpression([
        "'src/fairino_gazebo_config/worlds/", LaunchConfiguration('world'), "'"
    ])
    gazebo = TimerAction(
        period=2.0,
        actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
                ]),
                launch_arguments={
                    'gz_args': [world_string, ' -r']

                }.items(),
                condition=LaunchConfigurationEquals('gazebo', 'true')
            )
        ]
    )

    # Create robot in robot from robot_description
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=['-topic', 'robot_description', '-x', '0.0', '-y','0.0',  '-z','0.0',  '-R','0.0',  '-P', '0.0', '-Y','0.0'],
        condition=LaunchConfigurationEquals('gazebo', 'true'),
    )

    # World file -> MoveIt collision parser
    moveit_obs_gen = Node(
        package="fairino_gazebo_config",
        executable="gazebo_world_to_moveit.py",
        arguments=[world_string],
        condition=IfCondition(LaunchConfiguration('moveit')),
        parameters=[{"use_sim_time": False}]
    )

    
    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        world_arg,
        mount_arg,
        robot_model_arg,
        useSim_arg,
        moveit_arg,
        rsp,
        spawn_robot,
        # static_tfs,
        controller_manager,
        joint_state_broadcaster,
        fairino_controller,
        rail_controller,
        gazebo,
        rviz,
        move_group,
        moveit_obs_gen,
    ])
