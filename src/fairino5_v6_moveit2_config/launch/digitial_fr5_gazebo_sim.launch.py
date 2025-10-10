# import os
# from ament_index_python.packages import get_package_share_directory, get_package_prefix
# from launch import LaunchDescription, LaunchContext
# from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable, ExecuteProcess, TimerAction
# from launch.substitutions import (
#     Command,
#     FindExecutable,
#     LaunchConfiguration,
#     PathJoinSubstitution,
#     TextSubstitution
# )
# from launch.conditions import IfCondition
# from launch_ros.actions import Node
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch_ros.substitutions import FindPackageShare
# import xacro

# """
# THIS CREATES A DIGITAL FAIRINO, DETACHED FROM ANY HARDWARE

# USE THE /joint_trajectory TO SEND GOAL STATES (use fairino_gazebo_config/launch/sim_trajectory_pub.py for an example) 

# """

# def generate_launch_description():
#     pkg_share = get_package_share_directory('fairino5_v6_moveit2_config')
#     if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
#         gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share
#     else:
#         gazebo_resource_path = pkg_share

#     ####################
#     # launch arguments #
#     ####################

#     # Declare world file (default to empty)
#     world = LaunchConfiguration('world')
#     world_arg = DeclareLaunchArgument(
#         'world',
#         default_value="empty.sdf",
#         description="Name of world file to spawn robot into"
#     )

#     # Declare robot model; Currently does nothing, can be used in the future for allowing multi-robot model functionality
#     robot_model_arg = DeclareLaunchArgument(
#         'robot_model',
#         default_value="fairino5",
#         description="Name of robot model to spawn (ie. Fairino3)")

#     moveit = LaunchConfiguration('moveit')
#     moveit_arg = DeclareLaunchArgument(
#         'moveit',
#         default_value="false",
#         description="Set to true to use moveit controller and obscicle porting from gazebo"
#     )

#     ################
#     # Add programs #
#     ################

#     # RSP v2
#     file_subpath = 'config/fairino5_v6_robot.urdf.xacro'
#     # Use xacro to process the file
#     xacro_file = os.path.join(get_package_share_directory('fairino5_v6_moveit2_config'),file_subpath)
#     robot_description_raw = xacro.process_file(
#         xacro_file,
#         mappings={
#             'control_system': 'gazebo'
#     }).toxml()

#     # Create an instance of Gazebo
#     gazebo = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource([
#             os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
#         ]),
#         #launch_arguments={'gz_args': [ ' -r']}.items()
#         launch_arguments={'gz_args': [world, ' -r']}.items()
#     )
    
#     # Spawn the robot into gazebo
#     spawn_robot = Node(
#         package="ros_gz_sim",
#         executable="create",
#         arguments=['-topic', 'robot_description'],
#     )

#     rsp = Node(
#         package="robot_state_publisher",
#         executable="robot_state_publisher",
#         respawn=True,
#         output="screen",
#         parameters=[
#             {"robot_description": robot_description_raw},
#             {"use_sim_time": True},
#             {"publish_frequency": 15.0}
#         ],
#     )

#     # Spawn the joint_state_broadcaster for the gazebo robot
#     joint_state_broadcaster = TimerAction(
#         period=3.0,
#         actions=[
#             Node(
#                 package='controller_manager',
#                 executable='spawner',
#                 arguments=['joint_state_broadcaster', '--controller-manager', '/controller_manager'],
#                 output='screen'
#             )
#         ]
#     )

#     controllers_yaml = os.path.join(pkg_share, 'config', 'ros2_controllers.yaml')

#     # FOUND 
#     controller_manager = Node(
#             package='controller_manager',
#             executable='ros2_control_node',
#             parameters=[
#                 {'robot_description': robot_description_raw},
#                 controllers_yaml
#             ],
#             remappings=[
#                 ("/controller_manager/robot_description", "/robot_description"),
#             ],
#             output='screen'
#         )

#     # Spawn the fairino5_controller for the gazebo robot
#     fairino5_controller = TimerAction(
#         period=5.0,
#         actions=[
#             Node(
#                 package='controller_manager',
#                 executable='spawner',
#                 arguments=['fairino5_controller', '--controller-manager', '/controller_manager'],
#                 output='screen'
#             )
#         ]
#     )
#     spawn_controllers = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource([
#             PathJoinSubstitution([
#                 FindPackageShare('fairino5_v6_moveit2_config'),
#                 'launch',
#                 'spawn_controllers.launch.py'
#             ])
#         ]),
#         condition=IfCondition(LaunchConfiguration('moveit'))
#     )


#      # -------------------- MOVEIT 2 CONTROLLER --------------------
#     kinematics_yaml = os.path.join(
#         get_package_share_directory('fairino5_v6_moveit2_config'),
#         'config',
#         'kinematics.yaml'
#     )

#     static_virtual_joint_tfs = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource([
#             PathJoinSubstitution([
#                 FindPackageShare('fairino5_v6_moveit2_config'),
#                 'launch',
#                 'static_virtual_joint_tfs.launch.py'
#             ])
#         ]),
#         condition=IfCondition(LaunchConfiguration('moveit'))
#     )



#     # MoveIt parameters
#     # move_group = IncludeLaunchDescription(
#     #     PythonLaunchDescriptionSource([
#     #         PathJoinSubstitution([
#     #             FindPackageShare('fairino5_v6_moveit2_config'),
#     #             'launch',
#     #             'move_group.launch.py'
#     #         ])
#     #     ]),
#     #     condition=IfCondition(LaunchConfiguration('moveit'))
#     # )
#     # In move_group.launch.py
#     kinematics_yaml = load_yaml(
#         'fairino5_v6_moveit2_config', 'config/kinematics.yaml'
#     )

#     move_group_node = Node(
#         package='moveit_ros_move_group',
#         executable='move_group',
#         output='screen',
#         parameters=[
#             robot_description,
#             robot_description_semantic,
#             kinematics_yaml,  # THIS IS CRITICAL
#             trajectory_execution,
#             planning_pipelines,
#             {'use_sim_time': use_sim_time}
#         ],
#     )



#     moveit_obs_gen = Node(
#         package="fairino_gazebo_config",
#         executable="gazebo_world_to_moveit.py",
#         arguments=[world],
#         condition=IfCondition(LaunchConfiguration('moveit')),
#         parameters=[{"use_sim_time": True}]
#     )

    
#     return LaunchDescription([
#         SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
#         moveit_arg,
#         world_arg,
#         robot_model_arg,
#         gazebo,
        
        
#         static_virtual_joint_tfs,
#         rsp,
#         move_group,
        
#         controller_manager,
#         spawn_controllers,
#         #joint_state_broadcaster,
        
#         fairino5_controller,
        
#         moveit_obs_gen,
#         spawn_robot,
#     ])

import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable, ExecuteProcess, TimerAction
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution
)
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
import xacro

"""
THIS CREATES A DIGITAL FAIRINO, DETACHED FROM ANY HARDWARE

USE THE /joint_trajectory TO SEND GOAL STATES (use fairino_gazebo_config/launch/sim_trajectory_pub.py for an example) 

"""

def generate_launch_description():
    pkg_share = get_package_share_directory('fairino5_v6_moveit2_config')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share
    else:
        gazebo_resource_path = pkg_share

    ####################
    # launch arguments #
    ####################

    # Declare world file (default to empty)
    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument(
        'world',
        default_value="empty.sdf",
        description="Name of world file to spawn robot into"
    )

    # Declare robot model; Currently does nothing, can be used in the future for allowing multi-robot model functionality
    robot_model_arg = DeclareLaunchArgument(
        'robot_model',
        default_value="fairino5",
        description="Name of robot model to spawn (ie. Fairino3)")

    moveit = LaunchConfiguration('moveit')
    moveit_arg = DeclareLaunchArgument(
        'moveit',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )

    ################
    # Add programs #
    ################

    # RSP v2
    file_subpath = 'config/fairino5_v6_robot.urdf.xacro'
    # Use xacro to process the file
    xacro_file = os.path.join(get_package_share_directory('fairino5_v6_moveit2_config'),file_subpath)
    robot_description_raw = xacro.process_file(
        xacro_file,
        mappings={
            'control_system': 'gazebo'
    }).toxml()

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

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        respawn=True,
        output="screen",
        parameters=[
            {"robot_description": robot_description_raw},
            {"use_sim_time": True},
            {"publish_frequency": 15.0}
        ],
    )

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
                {'robot_description': robot_description_raw},
                controllers_yaml
            ],
            remappings=[
                ("/controller_manager/robot_description", "/robot_description"),
            ],
            output='screen'
        )

    # Spawn the fairino5_controller for the gazebo robot
    fairino5_controller = TimerAction(
        period=5.0,
        actions=[
            Node(
                package='controller_manager',
                executable='spawner',
                arguments=['fairino5_controller', '--controller-manager', '/controller_manager'],
                output='screen'
            )
        ]
    )
    # spawn_controllers = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         PathJoinSubstitution([
    #             FindPackageShare('fairino5_v6_moveit2_config'),
    #             'launch',
    #             'spawn_controllers.launch.py'
    #         ])
    #     ]),
    #     condition=IfCondition(LaunchConfiguration('moveit'))
    # )


     # -------------------- MOVEIT 2 CONTROLLER --------------------
    kinematics_yaml = os.path.join(
        get_package_share_directory('fairino5_v6_moveit2_config'),
        'config',
        'kinematics.yaml'
    )

    static_virtual_joint_tfs = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('fairino5_v6_moveit2_config'),
                'launch',
                'static_virtual_joint_tfs.launch.py'
            ])
        ]),
        condition=IfCondition(LaunchConfiguration('moveit'))
    )



    # MoveIt parameters - NOW WITH KINEMATICS CONFIG
    move_group = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('fairino5_v6_moveit2_config'),
                'launch',
                'move_group.launch.py'
            ])
        ]),
        launch_arguments={
            'use_sim_time': 'true'
        }.items(),
        condition=IfCondition(LaunchConfiguration('moveit'))
    )



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
        # spawn_controllers,
        #joint_state_broadcaster,
        
        fairino5_controller,
        
        # moveit_obs_gen,
        spawn_robot,
    ])