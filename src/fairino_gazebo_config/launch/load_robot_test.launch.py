# Copyright 2020 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression
)
from launch.conditions import LaunchConfigurationEquals, LaunchConfigurationNotEquals, IfCondition

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    declared_arguments = []
    # Robot specific arguments
    declared_arguments.append(
        DeclareLaunchArgument(
            "robot_model",
            default_value="fairino5",
            description="Robot's model",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "control_system",
            description="Control library",
            default_value="moveit",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "robot_mount",
            default_value="world",
            description="Name of the gripper attached to the arm",
        )
    )
    
    robot_model = LaunchConfiguration("robot_model")
    robot_mount = LaunchConfiguration("robot_mount")
    control_system = LaunchConfiguration("control_system")

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("fairino_description"), "robots", "fairino.urdf.xacro"]
            ),
            " ",
            "name:=test_robot",
            " ",
            "robot_mount:=",
            robot_mount,
            " ",
            "control_system:=",
            control_system,
            " ",
        ]
    )
    robot_description = {"robot_description": robot_description_content}


    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
    )

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
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
        parameters=[{"use_sim_time": True}]
    )

    nodes_to_start = [
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz,
    ]

    return LaunchDescription(declared_arguments + nodes_to_start)