# from moveit_configs_utils import MoveItConfigsBuilder
# from moveit_configs_utils.launches import generate_move_group_launch


# def generate_launch_description():
#     moveit_config = MoveItConfigsBuilder("fairino5_v6_robot", package_name="fairino5_v6_moveit2_config").to_moveit_configs()
#     return generate_move_group_launch(moveit_config)


from moveit_configs_utils import MoveItConfigsBuilder
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
import yaml

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
    
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        )
    )
    
    # Build MoveIt configuration
    moveit_config = (
        MoveItConfigsBuilder("fairino5_v6_robot", package_name="fairino5_v6_moveit2_config")
        .robot_description(file_path="config/fairino5_v6_robot.urdf.xacro")
        .robot_description_semantic(file_path="config/fairino5_v6_robot.srdf")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .planning_pipelines(pipelines=["ompl"])
        .to_moveit_configs()
    )
    
    # Explicitly load kinematics
    kinematics_yaml = load_yaml(
        'fairino5_v6_moveit2_config', 
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