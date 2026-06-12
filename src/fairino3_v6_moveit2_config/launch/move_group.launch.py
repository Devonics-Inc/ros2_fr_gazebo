from moveit_configs_utils import MoveItConfigsBuilder
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution,
    PythonExpression
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory
import yaml
import sys

def load_yaml(package_name, file_path):
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)
    
    try:
        with open(absolute_file_path, 'r') as file:
            return yaml.safe_load(file)
    except EnvironmentError:
        return None

def generate_launch_description():
    # Declare arguments
    use_sim_time = LaunchConfiguration('use_sim_time')
    robot_model = LaunchConfiguration('robot_model')
    robot_mount = LaunchConfiguration('robot_mount')
    control_system = LaunchConfiguration('control_system')
    moveit_pkg = LaunchConfiguration('moveit_pkg')
    
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'control_system',
            default_value="moveit",
            description="Control system to use"
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            'robot_model',
            default_value="fairino3",
            description="Robot model to use"
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'robot_mount',
            default_value="world",
            description="Robot mount type"
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'moveit',
            default_value='true',
            description='Whether to launch MoveIt'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'gazebo',
            default_value='false',
            description='Whether to launch Gazebo'
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            'moveit_pkg',
            default_value='fairino3_v6_robot',
            description='Which moveit pkg to pull data from'
        )
    )

    moveit_pkg_map = {
        "fairino3":  "fairino3_v6_moveit2_config",
        "fairino5":  "fairino5_v6_moveit2_config",
        "fairino10": "fairino10_v6_moveit2_config",
        "fairino16": "fairino16_v6_moveit2_config",
        "fairino20": "fairino20_v6_moveit2_config",
        "fairino30": "fairino30_v6_moveit2_config",
    }

    robot_model_str = "fairino3"  # default
    moveit_pkg = "fairino3_v6_moveit2_config"
    for arg in sys.argv:
        if arg.startswith("robot_model:="):
            robot_model_str = arg.split(":=")[1]
            moveit_pkg = moveit_pkg_map.get(robot_model_str, f"{robot_model_str}_v6_moveit2_config")

    # Find the path to the description package
    description_pkg_share = get_package_share_directory('fairino_description')
    # control_system_arg = PythonExpression([
    #     "'gazebo' if '", LaunchConfiguration('gazebo'), "' == 'true' else 'moveit'"
    # ])
    # Build MoveIt configuration
    moveit_config = (
        MoveItConfigsBuilder(f"{robot_model}_v6_robot", package_name=moveit_pkg)
        .robot_description(
            # Use a standard string path instead of a Substitution
            file_path=os.path.join(description_pkg_share, 'robots', 'test_fairino.urdf.xacro'),
            mappings={
                "robot_model": robot_model,
                "robot_mount": robot_mount,
                "control_system": control_system,
            }
        )
        .robot_description_semantic(
            file_path=f"config/{robot_model}_v6_robot.srdf.xacro",
            mappings={
                "mount": robot_mount
            }
        )
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .planning_pipelines(pipelines=["ompl"])
        .to_moveit_configs()
    )
    
    # Explicitly load kinematics
    kinematics_yaml = load_yaml(
        moveit_pkg, 
        'config/kinematics.yaml'
    )
    
    # Get planning scene monitor parameters
    planning_scene_monitor_parameters = {
        "publish_planning_scene": True,
        "publish_geometry_updates": True,
        "publish_state_updates": True,
        "publish_transforms_updates": True,
        "publish_robot_description": True,
        "publish_robot_description_semantic": True,
    }
    
    
    # Build the complete parameters list
    move_group_parameters = [
        moveit_config.to_dict(),
        {"use_sim_time": use_sim_time},
        planning_scene_monitor_parameters,
    ]
    
    # Add kinematics if it was loaded successfully
    if kinematics_yaml:
        move_group_parameters.append(
            {"robot_description_kinematics": kinematics_yaml}
        )
    
    # Create move_group node with all parameters at once
    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=move_group_parameters,
    )
    
    return LaunchDescription(
        declared_arguments + [move_group_node]
    )