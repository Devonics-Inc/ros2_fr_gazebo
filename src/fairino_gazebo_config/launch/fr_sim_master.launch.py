import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import (
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
    pkg_share = get_package_share_directory('fairino_description')
    rail_pkg_share = get_package_share_directory('fairino_description')
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
    
    useSim = LaunchConfiguration('use_sim')
    useSim_arg = DeclareLaunchArgument(
        'use_sim',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )

    # PASS PROPER CONTROL ARGUMENT BASED ON CLI ARGS
    control_system_arg = PythonExpression([
        "'control_system:=gazebo' if '", LaunchConfiguration('use_sim'), "' == 'true' else 'control_system:=moveit'"
    ])
    robot_mount_arg = PythonExpression([
        "' robot_mount:=", LaunchConfiguration('mount'), "'"
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
        control_system_arg,
        robot_mount_arg
    ])
    

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        respawn=True,
        output="screen",
        parameters=[{"robot_description": robot_description}, {"use_sim_time":True}],
    )

    ##########################################################

    # ------------------------
    # Gazebo
    # ------------------------
    # Create an instance of Gazebo
    world_string = PythonExpression([
        "'src/fairino_gazebo_config/worlds/", LaunchConfiguration('world'), "'"
    ])
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ]),
        launch_arguments={
            'gz_args': [world_string, ' -r']

        }.items(),
        condition=IfCondition(LaunchConfiguration('use_sim'))
    )
    
    # Spawn the robot into gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=['-topic', 'robot_description', '-x', '0.0', '-y','0.0',  '-z','0.0',  '-R','0.0',  '-P', '0.0', '-Y','0.0'],
        condition=IfCondition(LaunchConfiguration('use_sim')),
    )

    # Spawn the fairino_controller for the gazebo robot
    rail_controller_arg = PythonExpression([
        "'", LaunchConfiguration('robot_model'), "_controller'"
    ])
    rail_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[rail_controller_arg],
        output="screen",
    )
    # Rail controller
    # rail_controller_arg = PythonExpression([
    #     "'", LaunchConfiguration('mount'), "_controller'"
    # ])
    # rail_controller = Node(
    #     package="controller_manager",
    #     executable="spawner",
    #     arguments=[rail_controller_arg],
    #     output="screen",
    #     condition=LaunchConfigurationNotEquals('mount', 'world')
    # )

    rail_controllers = PathJoinSubstitution([
        FindPackageShare("rail_description"),
        'config',
        PythonExpression(["'", mount, "_controllers.yaml'"])
    ])

    arm_controllers = PathJoinSubstitution([
        FindPackageShare(PythonExpression(["'", robot_model, "_v6_moveit2_config'"])),
        'config',
        'ros2_controllers.yaml'
    ])

    controllers_to_load = PythonExpression([
        "[ '", arm_controllers, "' ] if '", mount, "' == 'world' else [ '", arm_controllers, "', '", rail_controllers, "' ]"
    ])

    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=[
            {'robot_description': robot_description},
            {'use_sim_time': True},
            controllers_to_load # It will look for this file if mount != world
        ],
        remappings=[("/controller_manager/robot_description", "/robot_description")],
        output='screen'
    )
    # ... rest of your node config
    spawn_rail_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[PythonExpression(["'", mount, "_controller'"])],
        output="screen",
        condition=LaunchConfigurationNotEquals('mount', 'world')
    )



    # Spawn the joint_state_broadcaster for the gazebo robot
    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
    )


    # -------------------- MOVEIT 2 CONTROLLER --------------------
    controllers_yaml = os.path.join(get_package_share_directory('fairino5_v6_moveit2_config'), 'config', 'ros2_controllers.yaml')
    # controller_manager = Node(
    #     package='controller_manager',
    #     executable='ros2_control_node',
    #     parameters=[
    #         {'robot_description': robot_description},   # add this
    #         controllers_yaml
    #     ],
    #     remappings=[
    #         ("/controller_manager/robot_description", "/robot_description"),
    #     ],
    #     output='screen'
    # )
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
        arguments=[world_string],
        condition=IfCondition(LaunchConfiguration('moveit')),
        parameters=[{"use_sim_time": True}]
    )
    
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
        parameters=[{"use_sim_time": True}]
    )
        
    
    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        world_arg,
        mount_arg,
        robot_model_arg,
        useSim_arg,
        moveit_arg,
        static_virtual_joint_tfs,
        rsp,
        spawn_robot,
        controller_manager,
        joint_state_broadcaster,
        rail_controller,
        spawn_rail_controller,
        gazebo,
        rviz,
        move_group,
        moveit_obs_gen,
    ])
    
#    
#    Includes
#     * static_virtual_joint_tfs
#     * robot_state_publisher
#     * move_group
#     * moveit_rviz
#     * warehouse_db (optional)
#     * ros2_control_node + controller spawners

