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
        if isinstance(v, dict):
            items.update(_flatten(v))
        else:
            items[k] = v
    return items

def load_yaml(package_name, file_path):
    """Load a yaml file given a ROS package NAME (resolves its share dir internally)."""
    package_path = get_package_share_directory(package_name)
    absolute_file_path = os.path.join(package_path, file_path)

    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:
        return None

def load_yaml_from_path(*path_parts):
    """Load a yaml file from an already-resolved absolute path (no package-name lookup)."""
    absolute_file_path = os.path.join(*path_parts)
    try:
        with open(absolute_file_path) as file:
            return yaml.safe_load(file)
    except OSError:
        print(f"[INFO] No file found at {absolute_file_path}, skipping")
        return None

# LOADS THE FILE DENOTED BY THE "launch_params.yaml"
def load_rail_config(filename):
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


def deep_merge(files, joints_map=None):
    """
    Merge multiple moveit_simple_controller_manager yaml fragments into one dict,
    then inject dynamic joint lists per-controller from joints_map.

    files: list of (path_part1, path_part2, ...) tuples, joined via os.path.join
           and loaded from an already-resolved absolute path (NOT a package name).
    joints_map: {controller_name: [joint, ...]} — overrides that controller's
                'joints' key after merging.
    """
    joints_map = joints_map or {}
    merged = {
        "moveit_controller_manager": "moveit_simple_controller_manager/MoveItSimpleControllerManager",
        "moveit_simple_controller_manager": {"controller_names": []}
    }

    for f in files:
        data = load_yaml_from_path(*f)
        if not data:
            continue
        scm = data.get("moveit_simple_controller_manager", {})
        merged["moveit_simple_controller_manager"]["controller_names"] += scm.get("controller_names", [])
        for k, v in scm.items():
            if k != "controller_names":
                merged["moveit_simple_controller_manager"][k] = v

    scm = merged["moveit_simple_controller_manager"]
    for controller_name, joints in joints_map.items():
        if controller_name in scm:
            scm[controller_name]["joints"] = joints
        else:
            print(f"[WARN] joints_map has '{controller_name}' but it wasn't found in any loaded trajectory file")

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

    description_pkg_share = get_package_share_directory('fairino_description')
    controller_pkg_share = get_package_share_directory('controllers')

    # --- Dynamic joint lists (mirrors the ros2_control launch file) ---
    arm_joints = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']
    rail_joints = []
    num_axes = 0
    if(mount == "test_rail"):
        num_axes = len(str(rail_defaults.get("axes", "")))
        print("Num axes: ", num_axes)
        for i in range(num_axes):
            rail_joints.append(f"{mount}_joint_{i}")
            # rail_joints = [f"{mount}_joint"] if 'rail' in mount else []
    gripper_joints = [f"{gripper}_joint"] if gripper != "none" else []

    joints_map = {"fairino_controller": arm_joints}
    if rail_joints:
        joints_map[f"{mount}_controller"] = rail_joints
    if gripper_joints:
        joints_map["gripper_controller"] = gripper_joints

    # Build MoveIt configuration — trajectory_execution intentionally NOT set
    # here; it's assigned post-hoc below from the merged per-controller files.
    moveit_config = (
        MoveItConfigsBuilder(f"{robot_model}_v6_robot", package_name=moveit_pkg)
        .robot_description(
            file_path=os.path.join(description_pkg_share, 'robots', 'test_fairino.urdf.xacro'),
            mappings={
                "robot_model": robot_model,
                "robot_mount": mount,
                "control_system": control_system,
                "axes_count": str(num_axes)
            }
        )
        .robot_description_semantic(
            file_path=os.path.join(description_pkg_share, 'robots', 'fairino_robot.srdf.xacro'),
            mappings={
                "mount": mount,
                "gripper": gripper,
                "axes": str(num_axes)
            }
        )
        .planning_pipelines(pipelines=["ompl"])
        .to_moveit_configs()
    )

    # --- Assemble per-controller trajectory files, only including what's active ---
    trajectory_files = [(controller_pkg_share, "fairino_controllers", "fairino_moveit_controller.yaml")]
    if rail_joints:
        trajectory_files.append((controller_pkg_share, "ext_axis_controllers", f"{mount}_moveit_controller.yaml"))
    if gripper_joints:
        trajectory_files.append((controller_pkg_share, "gripper_controllers", "gripper_moveit_controller.yaml"))

    moveit_config.trajectory_execution = deep_merge(trajectory_files, joints_map)

    # Explicitly load kinematics
    kinematics_yaml = load_yaml(
        moveit_pkg,
        'config/kinematics.yaml'
    )

    planning_scene_monitor_parameters = {
        "publish_planning_scene": True,
        "publish_geometry_updates": True,
        "publish_state_updates": True,
        "publish_transforms_updates": True,
        "publish_robot_description": True,
        "publish_robot_description_semantic": True,
    }

    move_group_parameters = [
        moveit_config.to_dict(),
        {"use_sim_time": use_sim_time},
        planning_scene_monitor_parameters,
    ]

    if kinematics_yaml:
        move_group_parameters.append(
            {"robot_description_kinematics": kinematics_yaml}
        )

    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=move_group_parameters,
    )

    return LaunchDescription([move_group_node])