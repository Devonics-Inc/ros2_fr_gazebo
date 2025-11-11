import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription, LaunchContext
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    ExecuteProcess
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

"""
THIS CREATES A DIGITAL FAIRINO, THAT MIRRORS THE ROBOT AT THE IP ADDRESS SET IN /rt_state_data

USE NORMAL CONTROL FOR YOUR ROBOT AND THE GAZEBO BOT WILL FOLLOW

"""

def generate_launch_description():
    pkg_share = get_package_share_directory('fairino_description')
    if('IGN_GAZEBO_RESOURCE_PATH' in os.environ):
        gazebo_resource_path = os.environ['IGN_GAZEBO_RESOURCE_PATH'] + ':' + pkg_share
    else:
        gazebo_resource_path = pkg_share


    # Declare root model; Currently does nothing, can be used in the future for allowing multi-robot model functionality
    robot_model = LaunchConfiguration('robot_model')
    robot_model_arg = DeclareLaunchArgument(
        'robot_model',
        default_value="fairino5",
        description="Name of robot model to spawn (ie. Fairino3)"
    )

    # Declare world file (default to empty)
    world = LaunchConfiguration('world')
    world_arg = DeclareLaunchArgument(
        'world',
        default_value="empty.sdf",
        description="Name of world file to spawn robot into"
    )

    # Uses different joint publishers for SDK and ROS
    control_method = LaunchConfiguration('sdk')
    control_method_arg = DeclareLaunchArgument(
        'sdk',
        default_value="False",
        description="True if using the SDK for robot control, false if using ROS"
    )

    moveit = LaunchConfiguration('moveit')
    moveit_arg = DeclareLaunchArgument(
        'moveit',
        default_value="false",
        description="Set to true to use moveit controller and obscicle porting from gazebo"
    )


    # -------------IGNORE THE FOLLOWING (in development) ----------
    # gripper_arg = DeclareLaunchArgument(
    #     'gripper',
    #     default_value='None',
    #     description='Type of gripper to attach to wrist3_link'
    # )

    # mount_arg = DeclareLaunchArgument(
    #     'mount',
    #     default_value='None',
    #     description='Type of mount object to attach under base_link'
    # )
    # ------------------------------------------------------------
    

    # Translate the /nonnrt_state_data for the /joint_states topic
    """     USING ROBOT_STATE_PKG SOCKET    """
    joint_state_pub = Node(
        package="fairino_gazebo_config",
        executable="rt_state_data.py",
        parameters=[{'robot_model': robot_model}],
        condition=LaunchConfigurationEquals("sdk","False")
    )
    """     USING ROBOT_STATE_PKG SOCKET FORWARDING    """
    joint_state_pub_sdk = Node(
        package="fairino_gazebo_config",
        executable="rt_state_data_SDK.py",
        parameters=[{'robot_model': robot_model}],
        condition=LaunchConfigurationEquals("sdk","True")
    )

    # xacro_file = os.path.join(get_package_share_directory(f'{fr_model}_v6_moveit2_config'),file_subpath)
    # fr_model = LaunchConfiguration('robot_model')
    # xacro_file = PathJoinSubstitution([
    #     FindPackageShare(PythonExpression([fr_model, "_v6_moveit2_config"])),
    #     'config',
    #     PythonExpression([fr_model, "_v6_robot.urdf.xacro"])
    # ])

    # robot_description_raw = Command([
    #     FindExecutable(name='xacro'),
    #     ' ',
    #     PathJoinSubstitution([
    #         FindPackageShare(PythonExpression([
    #             LaunchConfiguration('robot_model'), "_v6_moveit2_config"
    #         ])),
    #         'config',
    #         PythonExpression([
    #             LaunchConfiguration('robot_model'), "_v6_robot.urdf.xacro"
    #         ])
    #     ]),
    #     ' control_system:=gazebo'
    # ])

    # rsp = Node(
    #     package="robot_state_publisher",
    #     executable="robot_state_publisher",
    #     output="screen",
    #     parameters=[{"robot_description": robot_description_raw}],
    # )
    robot_description = Command([
        FindExecutable(name='xacro'),
        ' ',
        PathJoinSubstitution([
            FindPackageShare(PythonExpression([
                "'", LaunchConfiguration('robot_model'), "_v6_moveit2_config'"
            ])),
            'config',
            PythonExpression([
                "'", LaunchConfiguration('robot_model'), "_v6_robot.urdf.xacro'"
            ])
        ]),
        ' control_system:=gazebo'
    ])

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description}],
    )

    ##########################################################

    # ------------------------
    # Gazebo
    # ------------------------
    # Create an instance of Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ]),
        #launch_arguments={'gz_args': [ ' -r']}.items()
        launch_arguments={
            'gz_args': [world, ' -r']

        }.items()
    )
    
    # Spawn the robot into gazebo
    spawn_robot = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=['-topic', 'robot_description'],
    )

    # Spawn the joint_state_broadcaster for the gazebo robot
    joint_state_broadcaster = ExecuteProcess(
        cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'joint_state_broadcaster'],
        output="screen"
    )

    # Spawn the fairino_controller for the gazebo robot
    controllers = [
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino3_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino3")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino5_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino5")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino10_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino10")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino16_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino16")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino20_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino20")
        ),
        ExecuteProcess(
            cmd=["ros2", "control", "load_controller", "--set-state", 'active', 'fairino30_controller'],
            output="screen",
            condition=LaunchConfigurationEquals("robot_model", "fairino30")
        )
    ]

     # -------------------- MOVEIT 2 CONTROLLER --------------------
    # Move Group parameters for moveit control - NOW WITH KINEMATICS CONFIG
    move_group = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(PythonExpression([
                    LaunchConfiguration("robot_model"), "_v6_moveit2_config"
                ])),
                'launch',
                'move_group.launch.py'
            ])
        ]),
        launch_arguments={'use_sim_time': 'true'}.items(),
        condition=IfCondition(moveit)
    )


    # World file -> MoveIt collision parser
    moveit_obs_gen = Node(
        package="fairino_gazebo_config",
        executable="gazebo_world_to_moveit.py",
        arguments=[world],
        condition=IfCondition(moveit),
        parameters=[{"use_sim_time": True}]
    )
        
    
    return LaunchDescription([
        SetEnvironmentVariable(name='IGN_GAZEBO_RESOURCE_PATH', value=gazebo_resource_path),
        robot_model_arg,
        world_arg,
        control_method_arg,
        moveit_arg,
        # mount_arg,
        # gripper_arg,
        robot_model_arg,
        joint_state_pub,
        joint_state_pub_sdk,
        rsp,
        joint_state_broadcaster,
        *controllers,
        gazebo,
        spawn_robot,
        move_group,
        moveit_obs_gen
    ])
