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
import yaml
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

    robot_description_content = Command([
        FindExecutable(name='xacro'),
        ' ',
        PathJoinSubstitution([
            FindPackageShare('fairino_description'),
            'robots',
            "test_fairino.urdf.xacro"
        ]),
        ' ',
        "robot_model:=", LaunchConfiguration('robot_model'),
        ' ',
        "robot_mount:=", LaunchConfiguration('mount'),
        ' ',
        "control_system:=gazebo",
        ' ',
    ])

    robot_description = {'robot_description': robot_description_content}

    robot_description_semantic_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("fairino5_v6_moveit2_config"),
                    "config",
                    "fairino5_v6_robot.srdf.xacro",
                ]
            ),

        ]
    )

    robot_description_semantic = {"robot_description_semantic": robot_description_semantic_content}
    
    


    kinematics_yaml = load_yaml("fairino5_v6_moveit2_config", "config/kinematics.yaml")
    robot_description_kinematics = {"robot_description_kinematics": kinematics_yaml}

    trajectory_execution = {
        "moveit_manage_controllers": False,
        "trajectory_execution.allowed_execution_duration_scaling": 1.2,
        "trajectory_execution.allowed_goal_duration_margin": 0.5,
        "trajectory_execution.allowed_start_tolerance": 0.01,
    }

    planning_scene_monitor_parameters = {
        "publish_planning_scene": True,
        "publish_geometry_updates": True,
        "publish_state_updates": True,
        "publish_transforms_updates": True,
        "planning_scene_monitor_options": {
            "name": "planning_scene_monitor",
            "robot_description": "robot_description",
            "joint_state_topic": "/joint_states",
            "attached_collision_object_topic": "/move_group/planning_scene_monitor",
            "publish_planning_scene_topic": "/move_group/publish_planning_scene",
            "monitored_planning_scene_topic": "/move_group/monitored_planning_scene",
            "wait_for_initial_state_timeout": 10.0,
        },
    }
    controllers_yaml = load_yaml('fairino5_v6_moveit2_config', 'config/fairino5_test_rail_ros2_controllers.yaml')

    moveit_controllers = {
        "moveit_simple_controller_manager": controllers_yaml,
        "moveit_controller_manager": "moveit_simple_controller_manager/MoveItSimpleControllerManager",
    }

    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            robot_description,
            robot_description_semantic,
            robot_description_kinematics,
            trajectory_execution,
            moveit_controllers,
            planning_scene_monitor_parameters,
        ],
    )

    # rviz_config_file = PathJoinSubstitution(
    #     [FindPackageShare("fairino5_v6_moveit2_config"), "rviz", "moveit.rviz"]
    # )

    # rviz_node = Node(
    #     package="rviz2",
    #     executable="rviz2",
    #     name="rviz2_moveit",
    #     output="log",
    #     arguments=["-d", rviz_config_file],
    #     parameters=[
    #         robot_description,
    #         robot_description_semantic,
    #         robot_description_kinematics,
    #     ],
    # )
    


    # rsp = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     respawn=True,
    #     output="screen",
    #     parameters=[{"robot_description": robot_description}, {"use_sim_time":True}],
    # )

    ##########################################################

    # ------------------------
    # Gazebo
    # ------------------------
    # Create an instance of Gazebo
    # world_string = PythonExpression([
    #     "'src/fairino_gazebo_config/worlds/", LaunchConfiguration('world'), "'"
    # ])
    # # Spawn the fairino_controller for the gazebo robot
    # rail_controller_arg = PythonExpression([
    #     "'", LaunchConfiguration('robot_model'), "_controller'"
    # ])

    # rail_controller = TimerAction(
    #     period=3.0,
    #     actions=[Node(
    #         package="controller_manager",
    #         executable="spawner",
    #         arguments=[rail_controller_arg],
    #         output="screen",
    #         condition=LaunchConfigurationNotEquals('mount', 'world')
    #     )]
    # )

    
    # controller_manager = Node(
    #     package='controller_manager',
    #     executable='ros2_control_node',
    #     parameters=[
    #         {'robot_description': robot_description},
    #         {'use_sim_time': True},
    #         controllers_yaml # It will look for this file if mount != world
    #     ],
    #     remappings=[("/controller_manager/robot_description", "/robot_description")],
    #     output='screen'
    # )




    # # Spawn the joint_state_broadcaster for the gazebo robot
    # joint_state_broadcaster = TimerAction(
    #     period=3.0,
    #     actions=[
    #         Node(
    #         package="controller_manager",
    #         executable="spawner",
    #         arguments=["joint_state_broadcaster"],
    #         output="screen",
    #     )]
    # )


    # # -------------------- MOVEIT 2 CONTROLLER --------------------

    # # Move Group parameters for moveit control - NOW WITH KINEMATICS CONFIG
    # move_group = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         PathJoinSubstitution([
    #             FindPackageShare(PythonExpression([
    #                 "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
    #             ])),
    #             'launch',
    #             'move_group.launch.py'
    #         ])
    #     ]),
    #     launch_arguments={'use_sim_time': 'True',}.items(),
    #     condition=IfCondition(LaunchConfiguration('moveit'))
    # )

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
    
    # arm_controller_arg = PythonExpression([
    #     "'", LaunchConfiguration('robot_model'), "_controller'"
    # ])
    # controller = TimerAction(
    #     period=3.0,
    #     actions=[
    #         Node(
    #             package="controller_manager",
    #             executable="spawner",
    #             # arguments=[arm_controller_arg, "test_rail_controller"],
    #             arguments=['fairino5_controller'],
    #             output="screen",
    #         )
    #     ]
    # )
            
    
    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        world_arg,
        mount_arg,
        robot_model_arg,
        useSim_arg,
        moveit_arg,
        move_group_node,
        rviz
        # static_virtual_joint_tfs,
        # rsp,
        # # spawn_robot,
        # controller_manager,
        # joint_state_broadcaster,
        # # rail_controller,
        # # arm_controller,
        # # spawn_rail_controller,
        # controller,
        # # gazebo,
        # rviz,
        # # joint_state_publisher_gui,
        # move_group,
        # moveit_obs_gen,
    ])
    
#    
#    Includes
#     * static_virtual_joint_tfs
#     * robot_state_publisher
#     * move_group
#     * moveit_rviz
#     * warehouse_db (optional)
#     * ros2_control_node + controller spawners

