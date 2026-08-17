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

WORKSPACE_PATH = os.getcwd()

MOVEIT_PKG_MAP = {
    "fairino3":  "fairino3_v6_moveit2_config",
    "fairino5":  "fairino5_v6_moveit2_config",
    "fairino10": "fairino10_v6_moveit2_config",
    "fairino16": "fairino16_v6_moveit2_config",
    "fairino20": "fairino20_v6_moveit2_config",
    "fairino30": "fairino30_v6_moveit2_config",
}


def _flatten(_dict):
    """Flattens nested dicts so existing flat defaults.get('key') calls keep working."""
    items = {}
    for k, v in _dict.items():
        # keep both the plain key (for leaf lookups) and prefixed key
        if isinstance(v, dict):
            items.update(_flatten(v))
        else:
            items[k] = v
    return items

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:  # parent of IOError, OSError *and* WindowsError where available
        return None

# LOADS THE FILE DENOTED BY THE "launch_params.yaml"
def load_rail_config(filename):
    """
    Loads mount/rail_length/rail_width from a rail-config YAML file.
    Returns {} if missing so hardcoded fallbacks still apply.
    """
    config_path = os.path.join(
        get_package_share_directory("fairino_gazebo_config"),
        "config",
        filename,
    )
    try:
        with open(config_path) as f:
            return yaml.safe_load(f) or {}
    except OSError:
        print(f"[INFO] No rail config found at {config_path}, using built-in defaults")
        return {}


def load_launch_defaults():
    config_path = os.path.join(
        get_package_share_directory("fairino_gazebo_config"),
        "config",
        "launch_params.yaml",
    )
    try:
        with open(config_path) as f:
            raw = yaml.safe_load(f) or {}

        return _flatten(raw)
        
    except OSError:
        print(f"[INFO] No launch_params.yaml found at {config_path}, using built-in defaults")
        return {}


def _truthy(value: str) -> bool:
    return value.strip().lower() == "true"


def generate_launch_description():
    # GET PACKAGE PATHS
    pkg_share = get_package_share_directory('fairino_description')
    rail_pkg_share = get_package_share_directory('rail_description')
    gripper_pkg_share = get_package_share_directory("gripper_description")

    # GET DEFAULTS
    defaults = load_launch_defaults()
    rail_config_filename = str(defaults.get("rail_geometric_config", "rail_default.yaml"))
    rail_defaults = load_rail_config(rail_config_filename)

    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share + ':' + rail_pkg_share
    else:
        gazebo_resource_path = pkg_share + ':' + rail_pkg_share

    ####################
    # launch arguments #
    ####################

    # MAIN DEFAULTS
    world = str(defaults.get("world", "empty"))
    robot_model = str(defaults.get("robot_model", "fairino5"))
    moveit = str(defaults.get("moveit", "false"))
    gazebo = str(defaults.get("gazebo_simulated_hardware", "false"))
    robot_hardware_connected = str(defaults.get("robot_hardware_connected", "fairino5"))
    rviz = str(defaults.get("rviz_enabled", "true"))
    moveit_pkg = MOVEIT_PKG_MAP.get(robot_model, f"{robot_model}_v6_moveit2_config")
    

    # GRIPPER DEFAULTS
    gripper = str(defaults.get("gripper", "none"))
    gripper_hardware_connected = str(defaults.get("gripper_hardware_connected", "false"))
    gripper_controller = str(defaults.get("gripper_controller", "gripper_config.yaml"))
    gripper_hardware_plugin = str(defaults.get("gripper_hardware_plugin", "mock_components/GenericSystem"))

    # RAIL DEFAULTS
    rail_controller = str(defaults.get("rail_controller", "base_config.yaml"))
    rail_width = str(rail_defaults.get("rail_width", defaults.get("rail_width", "0.2")))
    rail_length = str(rail_defaults.get("rail_length", defaults.get("rail_length", "0.2")))
    mount = str(rail_defaults.get("mount", defaults.get("mount", "world")))

    # Spawn gazebo
    world_string = f"src/fairino_gazebo_config/worlds/{world}.sdf"


    control_system = "moveit"
    if(_truthy(robot_hardware_connected)):
        control_system = "hardware"
    elif(_truthy(gazebo)):
        control_system = "gazebo"
    else:
        control_system = "moveit"


    robot_description = Command([
        FindExecutable(name='xacro'),
        ' ',
        PathJoinSubstitution([
            FindPackageShare('fairino_description'),
            'robots',
            "test_fairino.urdf.xacro"
        ]),
        ' ',
        "robot_model:=", robot_model,
        ' ',
        "robot_mount:=", mount,
        ' ',
        "control_system:=", control_system,
        ' ',
    ])


    # CREATE LAUNCH ARGUMENT LIST
    ld = [SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path)]

    ld.append(
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            respawn=True,
            output="screen",
            parameters=[{"robot_description": robot_description}, {"use_sim_time":False}],
        )
    )
    

    # Load controllers into controller manager
    controllers_yaml = load_yaml(moveit_pkg, "config/ros2_controllers.yaml")
    controllers_yaml_path = os.path.join(
        get_package_share_directory(moveit_pkg),
        "config",
        "ros2_controllers.yaml"
    )

    ld.append(
        Node(
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
    )

    # Spawn the joint_state_broadcaster for the gazebo robot
    ld.append(
        TimerAction(
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
    )


    # Grab controllers to load
    fairino_controller_name = [f"{robot_model}_controller"]
    mount_controller = [f"{mount}_controller"]

        
    # Pass controllers into controller spawner
    ld.append(
        TimerAction(
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
    )


    # -------------------- MOVEIT 2 CONTROLLER --------------------

    if(_truthy(moveit)):
        # Move Group parameters for moveit control - NOW WITH KINEMATICS CONFIG
        ld.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    PathJoinSubstitution([
                        FindPackageShare("fairino_gazebo_config"),
                        'launch',
                        'move_group.launch.py'
                    ])
                ]),
                launch_arguments={
                    'use_sim_time': gazebo,
                    'robot_model': robot_model,
                    'robot_mount': mount,
                    'control_system': control_system,
                    'moveit_pkg': moveit_pkg,
                
                }.items()
            )
        )

    # IF RVIZ IS ENABLED
    if(_truthy(rviz)):
        ld.append(
            Node(
                package="rviz2",
                executable="rviz2",
                arguments=['-d', PathJoinSubstitution([
                    FindPackageShare(f"{robot_model}_v6_moveit2_config"),
                    'config',
                    'moveit.rviz'
                ])],
                parameters=[{"use_sim_time": False}]
            )
        )

        # ld.append(
        #     Node(
        #         package="fairino_gazebo_config",
        #         executable="gazebo_world_to_moveit.py",
        #         arguments=[world_string],
        #         condition=IfCondition(LaunchConfiguration('moveit')),
        #         parameters=[{"use_sim_time": False}]
        #     )
        # )



    if(mount != "world"):
        ld.append(
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=[mount_controller,
                        "-c", "/controller_manager",
                        "-t", "joint_trajectory_controller/JointTrajectoryController"
                ],
                output="screen",
            )
        )

    

    if(_truthy(gazebo)):
        ld.append(
            TimerAction(
                period=2.0,
                actions=[
                    IncludeLaunchDescription(
                        PythonLaunchDescriptionSource([
                            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
                        ]),
                        launch_arguments={
                            'gz_args': [world_string, ' -r']

                        }.items()
                    )
                ]
            )
        )

        # Create robot in robot from robot_description in gazebo
        ld.append(
            Node(
                package="ros_gz_sim",
                executable="create",
                arguments=['-topic', 'robot_description'], # To pass spawn location args: ['-x', '0.0', '-y','0.0',  '-z','0.0',  '-R','0.0',  '-P', '0.0', '-Y','0.0'
            )
        )
        

    
    return LaunchDescription(ld)
