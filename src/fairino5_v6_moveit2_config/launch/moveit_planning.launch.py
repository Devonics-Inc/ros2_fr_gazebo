from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, FindExecutable
from launch_ros.substitutions import FindPackageShare
import os
import xacro

def generate_launch_description():
    pkg_share = FindPackageShare('fairino5_v6_moveit2_config').find('fairino5_v6_moveit2_config')

    # Load robot description (same URDF as Gazebo)
    xacro_file = os.path.join(pkg_share, 'config', 'fairino5_v6_robot.urdf.xacro')
    robot_description_raw = xacro.process_file(xacro_file, mappings={'control_system': 'gazebo'}).toxml()

    robot_description = {"robot_description": robot_description_raw}
    robot_description_semantic = {
        "robot_description_semantic": PathJoinSubstitution(
            [pkg_share, "config", "fairino5_v6.srdf"]
        )
    }
    kinematics_yaml = os.path.join(pkg_share, "config", "kinematics.yaml")
    ros2_controllers_yaml = os.path.join(pkg_share, "config", "ros2_controllers.yaml")

    # MoveGroup node (the MoveIt 2 planner backend)
    move_group_node = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            robot_description,
            robot_description_semantic,
            {"moveit_controller_manager": "moveit_simple_controller_manager/MoveItSimpleControllerManager"},
            {"use_sim_time": True},
            kinematics_yaml,
            ros2_controllers_yaml,
        ],
    )

    # Your trajectory test node
    moveit_test_node = Node(
        package="fairino5_v6_moveit2_config",
        executable="moveit_traj_test",
        output="screen",
    )

    # Optional RViz2 visualization
    rviz_config_file = os.path.join(pkg_share, "config", "moveit.rviz")
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_file],
        parameters=[robot_description, robot_description_semantic],
    )

    return LaunchDescription([
        move_group_node,
        moveit_test_node,
        rviz_node,
    ])
