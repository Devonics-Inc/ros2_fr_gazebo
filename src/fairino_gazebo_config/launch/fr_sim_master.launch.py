"""
Fairino robotic arm bring-up launch file.

Parses launch arguments and starts:
  - robot_state_publisher (from an xacro-generated URDF)
  - ros2_control controller_manager + spawners (arm, mount rail, gripper)
  - Ignition Gazebo (optional, --gazebo:=true)
  - MoveIt 2 move_group + RViz (optional, --moveit:=true)

Digital-twin mode: run with hardware:=true and moveit:=true to mirror a
physical Fairino arm in RViz/Gazebo while driving it normally.
"""

import os
import re
import xacro
import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    ExecuteProcess,
    IncludeLaunchDescription,
    LogInfo,
    OpaqueFunction,
    RegisterEventHandler,
    SetEnvironmentVariable,
    TimerAction,
)
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import subprocess



# Maps a robot_model argument to its corresponding MoveIt 2 config package.
# Centralised here so every part of the launch file agrees on the package name
MOVEIT_PKG_MAP = {
    "fairino3": "fairino3_v6_moveit2_config",
    "fairino5": "fairino5_v6_moveit2_config",
    "fairino10": "fairino10_v6_moveit2_config",
    "fairino16": "fairino16_v6_moveit2_config",
    "fairino20": "fairino20_v6_moveit2_config",
    "fairino30": "fairino30_v6_moveit2_config",
}

def _flatten(d, parent_key="", sep="_"):
    """Flattens nested dicts so existing flat defaults.get('key') calls keep working."""
    items = {}
    for k, v in d.items():
        # keep both the plain key (for leaf lookups) and prefixed key
        if isinstance(v, dict):
            items.update(_flatten(v, k, sep=sep))
        else:
            items[k] = v
    return items


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


# loads yaml file from a package's share directory, returns None if the file doesn't exist
def load_yaml(package_name, relative_path):
    """
    Loads a YAML file from a ROS package's share directory.

    Args:
        package_name (str): Name of the ROS package.
        relative_path (str): Relative path to the YAML file within the package's share directory.

    Returns:
        dict | list | None: Parsed YAML content if the file is successfully loaded,
        otherwise None if the file cannot be found or opened.
    """
    
    absolute_path = os.path.join(get_package_share_directory(package_name), relative_path)
    try:
        with open(absolute_path) as f:
            return yaml.safe_load(f)
    except OSError:
        return None


def _truthy(value: str) -> bool:
    return value.strip().lower() == "true"



def launch_setup(context, *args, **kwargs):

    # -------------------------------------------------------------------------
    # 1. Extract launch arguments  | Configuration from CLI 
    # -------------------------------------------------------------------------

    world_name = LaunchConfiguration("world").perform(context)

    # The 'context' parameter is a LaunchContext object created and passed by
    # the ROS 2 launch system when this function is executed.
    #
    # Conceptually, the LaunchContext contains the current state of the launch,
    # including:
    #
    # LaunchContext
    # │
    # ├── Launch arguments
    # │      robot = "fr5"
    # │      gripper = "dh_ag95"
    # │
    # ├── Environment variables
    # │      HOME=/home/hady
    # │      ROS_DOMAIN_ID=0
    # │
    # ├── Local variables
    # │
    # ├── Namespaces
    # │
    # └── Other runtime information
    #
    # Launch arguments are represented by substitution objects. A substitution
    # does not store the final value directly because the value may not be known
    # when the launch file is first parsed.
    #
    # For example:
    #
    #     world = LaunchConfiguration("world")
    #
    # does NOT store the actual value of the 'world' argument. Instead, it
    # stores the instructions needed to retrieve that value later.
    #
    # When we call:
    #
    #     world_name = world.perform(context)
    #
    # the substitution resolves itself by looking inside the LaunchContext,
    # finding the launch argument named "world", and returning its value as a
    # regular Python string.

    robot_model = LaunchConfiguration("robot_model").perform(context)
    mount = LaunchConfiguration("mount").perform(context)
    gripper = LaunchConfiguration("gripper").perform(context)

    # extract the launch argument and turn it to boolean using the _truthy function
    moveit_enabled = _truthy(LaunchConfiguration("moveit").perform(context))
    gazebo_enabled = _truthy(LaunchConfiguration("gazebo_simulated_hardware").perform(context))
    hardware_enabled = _truthy(LaunchConfiguration("robot_hardware_connected").perform(context))
    rail_length = LaunchConfiguration("rail_length").perform(context)
    rail_width = LaunchConfiguration("rail_width").perform(context)
    env_config = LaunchConfiguration("env_config").perform(context)
    rviz_enabled = _truthy(LaunchConfiguration("rviz_enabled").perform(context))
    gripper_hardware_connected = LaunchConfiguration("gripper_hardware_connected").perform(context)
    base_controller_filename = LaunchConfiguration("rail_controller").perform(context)
    gripper_controller_filename = LaunchConfiguration("gripper_controller").perform(context)
    gripper_hardware_plugin = LaunchConfiguration("gripper_hardware_plugin").perform(context)




    # --- TEMP DEBUG ---
    print(f"[DEBUG] gripper_hardware_connected = {gripper_hardware_connected!r}")
    print(f"[DEBUG] gripper_hardware_plugin = {gripper_hardware_plugin!r}")



    # hardware takes priority over gazebo if both are requested
    if hardware_enabled:
        control_system = "hardware"
        if gazebo_enabled:
            print("\n[INFO] Both 'gazebo' and 'hardware' requested; using hardware.\n")
    elif gazebo_enabled:
        control_system = "gazebo"
    else:
        control_system = "moveit"



    # look for the robot_model inside MOVEIT_PKG_MAP dicitionary and falls safely to robot_model_v6_moveit2_config
    moveit_pkg = MOVEIT_PKG_MAP.get(robot_model, f"{robot_model}_v6_moveit2_config")
    
    # ideally this should return  moveit_pkg fairino5_v6_moveit2_config




    # -------------------------------------------------------------------------
    # 2. Build the list of actions to be executed 
    # -------------------------------------------------------------------------



    # -------------------------------------------------------------------------
    # 2.1 action 1 => log the current configuration that user have chosen 
    # -------------------------------------------------------------------------
    # create actions list to hold the steps of the launch file
    # this is done because we are not writing the node itself in the launch file
    # since we dont write the node it self in launch, array of actions is created to carry steps sequentially
    # in this case the first action is to log the configurations
    # after parsing them from the cli
    actions = [
        LogInfo(msg=f"Robot model: {robot_model} | control system: {control_system} | "
                    f"gripper: {gripper} | moveit_pkg: {moveit_pkg} ")
    ]

    # -------------------------------------------------------------------------
    # 2.2 clean start Implementaiton => clean any simulation server that has been running in the background
    # -------------------------------------------------------------------------
    #
    # If a previous simulation did not shut down cleanly, some Gazebo or ROS 2
    # processes may still be running in the background. Launching a new
    # simulation while these processes are alive can lead to unexpected
    # behavior, such as models or controllers from the previous simulation
    # interfering with the new one.
    #
    # For example:
    #
    #   1. Launch a simulation with an FR5 robot.
    #   2. Terminate the launch without properly shutting down Gazebo.
    #   3. Start a new simulation with an FR10.
    #
    # In some cases, Gazebo may still contain resources from the previous
    # session, resulting in stale models, duplicate controllers, or other
    # unexpected artifacts appearing in the new simulation.
    #
    # When 'clean_start_enabled' is True, the launch file first terminates any
    # leftover Gazebo, MoveIt, robot_state_publisher, and ros2_control
    # processes before launching the new simulation.
    #
    # This is achieved using Linux's 'pkill -f', which searches for matching
    # process command lines and forcefully terminates them.
    #
    # NOTE:
    # The process patterns use the classic "[x]xxx" trick (for example,
    # '[g]z sim' instead of 'gz sim').
    #
    # This prevents the pkill command from matching its own shell script.
    # Without this trick, the shell executing the command would itself contain
    # the string "gz sim" in its command line, causing pkill to terminate the
    # script before it finishes killing the intended processes.
    #
    # After sending the kill signals, the launch waits briefly to allow the
    # operating system to fully clean up the terminated processes before
    # starting a fresh simulation.


    # the detault start up delay is 0, however if we aim to run a clean start we set it to 1.5 seconds giving 
    # operating system enough time to klean the processes 
    startup_delay = 0.0


    # everything below this point is deferred behind startup_delay (if clean_start
    # was requested) so the old processes are dead before we spawn new ones.
    remaining_actions = []


    # -------------------------------------------------------------------------
    # 2.3 launch the robot_state_publisher => return to notion for more details
    # 
    # responsible for publishing the current trasnformations tf/tf_static as well as the 
    # description of the robot, uses jointstates to figure out tf/tf_static
    # -------------------------------------------------------------------------
    #

    # get the xacro path for test_fairino.urdf.xacro file from the fairino_description package
    xacro_path = os.path.join(
        get_package_share_directory("fairino_description"),
        "robots",
        "test_fairino.urdf.xacro",
    )

    # process the robot_description to xml using xacro module
    # pass the robot_model, mount, control_system and gripper as mappings to the xacro file
    robot_description_xml = xacro.process_file(
        xacro_path,
        mappings={
            "robot_model": robot_model,
            "robot_mount": mount,
            "control_system": control_system,
            "gripper": gripper,
            "rail_length": rail_length,
            "rail_width": rail_width,
            "gripper_hardware_connected": gripper_hardware_connected, 
            "gripper_hardware_plugin": gripper_hardware_plugin,
        },
    ).toxml()
    robot_description = {"robot_description": robot_description_xml}


    # 2- load the robot state publisher node with the robot_description parameter and use_sim_time set to false
    remaining_actions.append(
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            respawn=True,
            output="screen",
            parameters=[robot_description, {"use_sim_time": False}],
        )
    )




    # -------------------------------------------------------------------------
    # 2.4 launch the controller manager & resource manager
    # 
    # responsible for publishing the joint states that get utilized by the 
    # robot_state_publisehr 
    # -------------------------------------------------------------------------
    #
    # ------------------------------------------------------------------
    # controller_manager
    # ------------------------------------------------------------------

    # get the path for the controller manager yaml file
    # and the gripper controller yaml file from the moveit_pkg package
    

    # rail/base and gripper controller yamls now come from fairino_gazebo_config/config,
    # with filenames chosen via launch_params.yaml (base_controller / gripper_controller)
    fairino_gazebo_config_config_dir = os.path.join(
        get_package_share_directory("fairino_gazebo_config"), "config"
    )
    rail_yaml_path = os.path.join(fairino_gazebo_config_config_dir, base_controller_filename)
    gripper_yaml_path = os.path.join(fairino_gazebo_config_config_dir, gripper_controller_filename)

    controllers_yaml = os.path.join(
        get_package_share_directory("controllers"),
        "fairino_controllers",
        "fairino_ros2_controller.yaml"
    )

    with open(controllers_yaml, 'r') as f:
        controller_params = yaml.safe_load(f)

    
    dynamic_joints = ['j1', 'j2', 'j3', 'j4', 'j5', 'j6']

    # 4. Inject the joints for rail and gripper to controller
    if gripper != "none" and os.path.exists(gripper_yaml_path):
        dynamic_joints.append(f'{gripper}_joint')
    else:
        print(f"[INFO] Skipping gripper_controllers.yaml (gripper='{gripper}')")

    if('rail' in mount):
        dynamic_joints.append(f"{mount}_joint")

    controller_params['fairino_controller']['ros__parameters']['joints'] = dynamic_joints

    # In gazebo mode, the gz_ros2_control Gazebo plugin (declared in the xacro's
    # <gazebo><plugin> block) spins up its own controller_manager node internally.
    # Starting a second, standalone ros2_control_node here would create a duplicate
    # node named /controller_manager and cause flaky switch_controller/activation
    # behaviour. Only start the standalone node for moveit (mock hardware) and
    # hardware (real robot) modes, where nothing else provides a controller_manager.
    if control_system != "gazebo":
        remaining_actions.append(
            Node(
                package="controller_manager",
                executable="ros2_control_node",
                parameters=[controller_params, {"use_sim_time": gazebo_enabled}],
                remappings=[("/controller_manager/robot_description", "/robot_description")],
                output="screen",
            )
        )
    else:
        print(
            "[INFO] control_system='gazebo': skipping standalone ros2_control_node "
            "(controller_manager is provided by the gz_ros2_control Gazebo plugin)"
        )

    # joint_state_broadcaster + arm controller spawner.
    # Kept as a named variable (rather than inline inside the TimerAction) so
    # it can be used as the target_action for an OnProcessExit event handler
    # below -- that spawner exiting is our real "controller_manager is up and
    # the arm broadcaster is active" signal, more reliable than a fixed delay.
    arm_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            f"{robot_model}_controller",
            "-c", "/controller_manager",
            "--controller-manager-timeout", "10",
            "--param-file", controllers_yaml,
        ],
        output="screen",
    )
    remaining_actions.append(TimerAction(period=1.0, actions=[arm_broadcaster_spawner]))

# Rail / mount controller (only if the robot isn't mounted directly to 'world')
    if mount != "world":
        rail_spawner_args = [
            f"{mount}_controller",
            "-c", "/controller_manager",
            "-t", "joint_trajectory_controller/JointTrajectoryController",
        ]
        if os.path.exists(rail_yaml_path):
            rail_spawner_args += ["--param-file", rail_yaml_path]
        else:
            print(f"[WARN] {rail_yaml_path} not found, spawning {mount}_controller without a param file")

        remaining_actions.append(
            TimerAction(
                period=2.0,
                actions=[
                    Node(
                        package="controller_manager",
                        executable="spawner",
                        arguments=rail_spawner_args,
                        output="screen",
                    )
                ],
            )
        )

    # Gripper controller spawner
    # if gripper != "none":
    #     if gripper not in GRIPPER_JOINT_MAP:
    #         print(f"[WARN] Unknown gripper '{gripper}', skipping gripper controller spawn.")
    #     elif not os.path.exists(gripper_yaml_path):
    #         print(f"[WARN] {gripper_yaml_path} not found, skipping gripper controller spawn.")
    #     else:
    #         active_controller_name = GRIPPER_CONTROLLER_NAME_MAP.get(gripper, "gripper_controller")
    #         remaining_actions.append(
    #             TimerAction(
    #                 period=3.0,
    #                 actions=[
    #                     Node(
    #                         package="controller_manager",
    #                         executable="spawner",
    #                         arguments=[
    #                             active_controller_name,
    #                             "--param-file", gripper_yaml_path,
    #                             "-c", "/controller_manager",
    #                         ],
    #                         output="screen",
    #                     )
    #                 ],
    #             )
    #         )

    # ------------------------------------------------------------------
    # Gazebo (optional)
    # ------------------------------------------------------------------
    if gazebo_enabled:
        world_sdf_path = os.path.join(
            get_package_share_directory("fairino_gazebo_config"), "worlds", f"{world_name}.sdf"
        )
        remaining_actions.append(
            TimerAction(
                period=2.0,
                actions=[
                    IncludeLaunchDescription(
                        PythonLaunchDescriptionSource(
                            os.path.join(
                                get_package_share_directory("ros_gz_sim"),
                                "launch",
                                "gz_sim.launch.py",
                            )
                        ),
                        launch_arguments={"gz_args": f"{world_sdf_path} -r"}.items(),
                    )
                ],
            )
        )
        remaining_actions.append(
            Node(
                package="ros_gz_sim",
                executable="create",
                arguments=["-topic", "robot_description"],
            )
        )
    else:
        world_sdf_path = None

    # ------------------------------------------------------------------
    # MoveIt 2 (optional)
    # ------------------------------F------------------------------------
    if moveit_enabled:
        remaining_actions.append(
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        get_package_share_directory("fairino_gazebo_config"),
                        "launch",
                        "move_group.launch.py",
                    )
                ),
                launch_arguments={
                    "use_sim_time": str(gazebo_enabled),
                    "robot_model": robot_model,
                    "robot_mount": mount,
                    "control_system": control_system,
                    "moveit_pkg": moveit_pkg,
                    "gripper": gripper,
                    "env_config": env_config,      # <-- ADD THIS
                }.items(),
            )
        )


        kinematics_yaml = load_yaml(moveit_pkg, "config/kinematics.yaml")
        if rviz_enabled:
            remaining_actions.append(
                Node(
                    package="rviz2",
                    executable="rviz2",
                    arguments=[
                        "-d",
                        os.path.join(get_package_share_directory(moveit_pkg), "config", "moveit.rviz"),
                    ],
                    parameters=[
                        {"use_sim_time": False},
                        {"robot_description_kinematics": kinematics_yaml},
                    ],
                )
            )

        remaining_actions.append(
            Node(
                package="fairino_gazebo_config",
                executable="gazebo_world_to_moveit.py",
                arguments=[world_sdf_path or ""],
                parameters=[{"use_sim_time": False}],
            )
        )

    # Static virtual-joint TFs, published from the resolved MoveIt package.
    # Disabled by default (kept from the original file) -- uncomment if your
    # setup needs it when not using Gazebo.
    # if control_system != "gazebo":
    #     remaining_actions.append(
    #         IncludeLaunchDescription(
    #             PythonLaunchDescriptionSource(
    #                 os.path.join(
    #                     get_package_share_directory(moveit_pkg),
    #                     "launch",
    #                     "static_virtual_joint_tfs.launch.py",
    #                 )
    #             )
    #         )
    #     )

    if startup_delay > 0.0:
        actions.append(TimerAction(period=startup_delay, actions=remaining_actions))
    else:
        actions.extend(remaining_actions)

    return actions


def generate_launch_description():
    pkg_share = get_package_share_directory("fairino_description")
    rail_pkg_share = get_package_share_directory("rail_description")
    gripper_pkg_share = get_package_share_directory("gripper_description")

    defaults = load_launch_defaults()
    rail_config_filename = str(defaults.get("rail_geometric_config", "rail_default.yaml"))
    rail_defaults = load_rail_config(rail_config_filename)

    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share + ':' + rail_pkg_share
    else:
        gazebo_resource_path = pkg_share + ':' + rail_pkg_share

    declared_arguments = [
        SetEnvironmentVariable(
            name="IGN_GAZEBO_RESOURCE_PATH",
            value=gazebo_resource_path
        ),
        DeclareLaunchArgument(
            "world",
            default_value=str(defaults.get("world", "empty")),
            description="Name of world file to spawn robot into",
        ),
        DeclareLaunchArgument(
            "robot_model",
            default_value=str(defaults.get("robot_model", "fairino5")),
            description="Name of robot model to spawn (e.g. fairino5)",
            choices=list(MOVEIT_PKG_MAP.keys()),
        ),
        DeclareLaunchArgument(
            "gripper",
            default_value=str(defaults.get("gripper", "none")),
            description="Gripper to attach (e.g. dh_ag95, none)",
        ),
        DeclareLaunchArgument(
            "moveit",
            default_value=str(defaults.get("moveit", "false")),
            description="Set to true to launch the MoveIt 2 move_group + RViz",
        ),
        DeclareLaunchArgument(
            "gazebo_simulated_hardware",
            default_value=str(defaults.get("gazebo_simulated_hardware", "false")),
            description="Set to true to launch Ignition Gazebo with the given world",
        ),
        DeclareLaunchArgument(
            "robot_hardware_connected",
            default_value=str(defaults.get("robot_hardware_connected", "false")),
            description="Set to true to use the real hardware controller",
        ),
        DeclareLaunchArgument(
            "rail_width",
            default_value=str(rail_defaults.get("rail_width", defaults.get("rail_width", "0.2"))),
            description="Width of the mount rail (meters)",
        ),
        DeclareLaunchArgument(
            "rail_length",
            default_value=str(rail_defaults.get("rail_length", defaults.get("rail_length", "0.2"))),
            description="Length of the mount rail (meters)",
        ),
        DeclareLaunchArgument(
            "env_config",
            default_value=str(defaults.get("env_config", "env_config.yaml")),
            description="Filename (in fairino_gazebo_config/config/) of the environment objects "
                         "to load into the MoveIt planning scene. Leave unset/empty to skip "
                         "loading any environment.",
        ),
        DeclareLaunchArgument(
            "mount",
            default_value=str(rail_defaults.get("mount", defaults.get("mount", "world"))),
            description="Object to mount the robot to (e.g. world or rail_carriage)",
        ),
        DeclareLaunchArgument(
            "rviz_enabled",
            default_value=str(defaults.get("rviz_enabled", "true")),
            description="Set to true to launch RViz alongside MoveIt",
        ),
        DeclareLaunchArgument(
            "gripper_hardware_connected",
            default_value=str(defaults.get("gripper_hardware_connected", "false")),
            description="Set to true to use the real gripper hardware interface instead of mock",
        ),
        DeclareLaunchArgument(
            "rail_controller",
            default_value=str(defaults.get("rail_controller", "base_config.yaml")),
            description="Filename (in fairino_gazebo_config/config/) of the rail/mount controller yaml",
        ),
        DeclareLaunchArgument(
            "gripper_controller",
            default_value=str(defaults.get("gripper_controller", "gripper_config.yaml")),
            description="Filename (in fairino_gazebo_config/config/) of the gripper controller yaml",
        ),
        DeclareLaunchArgument(
            "gripper_hardware_plugin",
            default_value=str(defaults.get("gripper_hardware_plugin", "mock_components/GenericSystem")),
            description="ros2_control hardware plugin name to use for the gripper "
                         "when gripper_hardware_connected is true",
        ),
    ]
    

    return LaunchDescription(declared_arguments + [OpaqueFunction(function=launch_setup)])