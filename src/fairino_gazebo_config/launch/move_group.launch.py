from moveit_configs_utils import MoveItConfigsBuilder
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import os
from ament_index_python.packages import get_package_share_directory
import yaml
import sys

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


def deep_merge(files):
    merged = {"moveit_controller_manager": "moveit_simple_controller_manager/MoveItSimpleControllerManager",
              "moveit_simple_controller_manager": {"controller_names": []}}
    for f in files:
        data = load_yaml(*f)
        scm = data.get("moveit_simple_controller_manager", {})
        merged["moveit_simple_controller_manager"]["controller_names"] += scm.get("controller_names", [])
        for k, v in scm.items():
            if k != "controller_names":
                merged["moveit_simple_controller_manager"][k] = v
    return merged


def generate_launch_description():
    pkg_share = get_package_share_directory('fairino_description')
    rail_pkg_share = get_package_share_directory('rail_description')
    gripper_pkg_share = get_package_share_directory("gripper_description")

    # GET DEFAULTS
    defaults = load_launch_defaults()
    rail_config_filename = str(defaults.get("rail_geometric_config", "rail_default.yaml"))
    rail_defaults = load_rail_config(rail_config_filename)

    mount = str(rail_defaults.get("mount", defaults.get("mount", "world")))
    gripper = str(defaults.get("gripper", "none"))

    ####################
    # launch arguments #
    ####################

    # MAIN DEFAULTS
    robot_model = str(defaults.get("robot_model", "fairino5"))
    gazebo = str(defaults.get("gazebo_simulated_hardware", "false"))
    use_sim_time = _truthy(gazebo)
    robot_hardware_connected = str(defaults.get("robot_hardware_connected", "fairino5"))

    mount = str(rail_defaults.get("mount", defaults.get("mount", "world")))

    moveit_pkg = MOVEIT_PKG_MAP.get(robot_model, f"{robot_model}_v6_moveit2_config")

    control_system = "moveit"
    if(_truthy(robot_hardware_connected)):
        control_system = "hardware"
    elif(_truthy(gazebo)):
        control_system = "gazebo"
    else:
        control_system = "moveit"

    # Find the path to the description package
    description_pkg_share = get_package_share_directory('fairino_description')
    controller_pkg_share = get_package_share_directory('controllers')
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
                "robot_mount": mount,
                "control_system": control_system,
            }
        )
        .robot_description_semantic(
            file_path=f"config/{robot_model}_v6_robot.srdf.xacro",
            mappings={
                "mount": mount
            }
        )
        .trajectory_execution(file_path=os.path.join(controller_pkg_share, "fairino_controllers/fairino_moveit_controller.yaml"))
        .planning_pipelines(pipelines=["ompl"])
        .to_moveit_configs()
    )


    trajectory_files = [(controller_pkg_share, "fairino_controllers", "arm_moveit_controller.yaml")]
    if 'rail' in mount:
        trajectory_files.append((controller_pkg_share, "ext_axis_controllers", f"{mount}_moveit_controller.yaml"))
    if gripper != 'none':
        trajectory_files.append((controller_pkg_share, "gripper_controllers", "gripper_moveit_controller.yaml"))

    # merged_traj = deep_merge(trajectory_files)

    # moveit_config.trajectory_execution = merged_traj
    
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
    
    return LaunchDescription([move_group_node])