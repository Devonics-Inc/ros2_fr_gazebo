# Porting your FR3 Into Gazebo
Written and developed by Granger Pasko

## Introduction
<p>Hello devs and devinas, in this README I will cover the steps needed to configure your gazebo environment to mirror your Fairino FR3. This will also go over the contetns of this directory and how they interact as well as how to manipulate them to your specific needs.</p>

## Step 1) Building your workspace
<p>If you build your workspace as is, you will get the following environment:

- A Gazebo Environment with an FR3 mirroring your targeted IP (this repo defaults to 192.168.55.2)
- The simulated FR3 will follow your robot, all commands must be made either through the SDK or the WebApp

    ### Step 1a) Configuring your IP
    To change the IP address that the state publisher listens to (the target being your Fairino robot), you need to navigate to:
    <b> src/fairino_hardware/include/fairino_hardware/data_types_def.h </b>
    Find the line that sets the Controller IP and change it to match the robot IP you'd like to target.

    ### Step 1b) Choose your control method
    If you prefer to use the ROS2 control interface to command your robot instead of the SDK, you can navigate to:
    <b> src/fairino_hardware/include/src/command_server_node.cpp </b>
    Here, you can uncomment the ROS2 command Node to re-enable the ros2 control system.
    
    NOTE: this will remove SDK functionality from your robot

Now, you can build your workspace by running <b>colcon build --symlink-install</b>

## Step 2) Commands to run your simulator

To run the gazebo Sim, use <b>~/fr3_gazebo</b>$ ros2 launch fairino3_moveit2_config fr3_gazebo_sim.launch.py

Below are the steps to run the process manually:

Run the commands below IN ORDER (Don't forget to use 'source isntall/setup.bash' for each termianl)

1) 
    <b>~/fr3_gazebo</b>$ ros2 run fairino_hardware ros2_cmd_server

    This will create the link from your robot to your ROS system.

2) 
    <b>~/fr3_gazebo</b>$ ros2 run fairino3_moveit2_config SimJointPublisher.py

    This node subscribes to /nonrt_state_data and translates the joint positions to radians and publishes them to the /state_data topic

3) 
    <b>~/fr3_gazebo</b>$ ros2 launch fairino3_moveit2_config rsp.launch.py

    This node creates the /robot_description and /tf topics. This allows Gazebo to view the 3D model of the robot and links the proper control nodes to said /robot_description

4) 
    <b>~/fr3_gazebo</b>$ ros2 launch ros_gz_sim gz_sim.launch.py

    Use this to launch gazebo through ROS

5) 
    <b>~/fr3_gazebo</b>$ ros2 run ros_gz_sim create -topic robot_description

    Creates a robot based off the published /robot_description topic and spawns it in gazebo

6) 
    <b>~/fr3_gazebo</b>$ ros2 control load_controller --set-state active joint_state_broadcaster

    Sets up communication for ROS2 and Gazebo robot joint states

7)
    <b>~/fr3_gazebo</b>$ ros2 control load_controller --set-state active fairino3_controller

    Loads the fairino3_controller to move the simulated robot in gazebo


Now, when you open a terminal and use 'rqt_graph' your setup should look like this:
    ![alt text](src/README_rqt_graph.png)


Now, you can set up a script using the SDK to control your robot and watch it move in Gazebo!


### POSSIBLE ERRORS:

If your robot shows up as an entity in Gazebo but you cannot see the model, it is usually due to a conflicting resource path. To fix this, close gazebo and write in the following command to your terminal before re-running:

export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/[path to directory]/fr3_gazebo/install/fairino_description/share

If your terminal says it cannot find the SimJointPublisher.py:
navigate to /src/fairino3_moveit2_config/launch and add an empty folder called "__pycache__"
Now rebuild your workspace.
