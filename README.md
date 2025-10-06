# Porting your Fairino Robot Into Gazebo


## Environment
This repo is built using ROS2 Humble on Ubuntu 22.04 (Jammy Jellyfish) and Gazebo Fortress 6.17.0 (aka Gazebo Ignition) with the x86_64 architecture.

<u>NOTE:</u> If you are using the aarch64 architecture, you will need to use `sudo apt install libxmlrpc-c++8-dev` to install the appropriate XMLRPC library

## Introduction
In this README I will cover the steps needed to configure your ROS2 environment for your Fairino. This will include:

- [Instalation of your ROS2 Environment](#step-0-building-and-installing-ros2)

- [Instalation of Gazebo Ignition](#gazebo-install-heading)

- [Configutation of your robot](#step-1-building-your-fairino-workspace)

- [Porting your robot into Gazebo](#step-2-commands-to-run-your-gazebo-simulator)

- [MoveIt2 configuration/Demo]

## Step 0) Building and installing ROS2
- To install ROS2 Humble, you can follow the instructions on either the [ROS2 Humble documentation page](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) or the [Fairino ROS2 manual](https://fairino-doc-en.readthedocs.io/latest/ROSGuide/ros2guide.html)
    - If you choose the latter, then follow instructions <i><u><b>until</b></u></i> section 2.2 "Compile and build fairino_hardware" since we are going to be using a modified version.
- To install Gazebo 6.17, follow the link [here](https://gazebosim.org/docs/fortress/install_ubuntu/) or follow the steps below: 

<a id="gazebo-install-heading"></a>

- ### Installing ROS2 control libraries:
    - Run the following commands to install the ROS2 humble control packges:
    >
        sudo apt udpate
        sudo apt install ros-humble-ros2-control ros-humble-ros2-controllers

- ### Install Gazebo Ignition 6.17

    - First install some necessary tools:

            sudo apt-get update
            sudo apt-get install lsb-release gnupg

    - Then install Gazebo Fortress:

        >
            sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

            echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

            sudo apt-get update

            sudo apt-get install ignition-fortress


- Note that if you are looking to use the ROS2 API commands, you will need to set up a SimMachine to interporate the XML packets sent by the fairino ros2_cmd_server. For SimMachine installation isntructions, follow the guide in the Fairino Documentation page [here](https://fairino-doc-en.readthedocs.io/latest/VMMachine/controller_docker_machine.html)



## Step 1) Building your Fairino workspace
<p>If you build your workspace as is, you will get the following environment:

- A Gazebo Environment with an Fairino robot mirroring your targeted IP <b>`(this repo defaults to 192.168.55.2)`</b>
- The simulated Fairino will follow your physical Fairino or SimMachine
- A MoveIt2 control example that can hook up to your SimMachine or physical hardware
- A digital Fairino controllable via ROS2s /joint_trajectory that is separate from any physical robot or SimMachine

    ### Step 1a) Configuring your IP
    To change the IP address that the state publisher listens to (the target being your Fairino robot) in the following files:
    
    <b> `src/fairino_hardware/include/fairino_hardware/data_types_def.h` </b> 
    
    <b> `src/fairino_gazebo_config/launch/rt_state_data.py` </b> 
    
    <b> `src/fairino_hardware/include/fairino_hardware/fairino_hardware_interface.hpp` </b>
    
    
    Find the line that sets the Controller/Robot IP and change it to match the robot IP you'd like to target.



Now, you can build your workspace by running <b>`colcon build --symlink-install`</b>

## Step 2) Commands to run your Gazebo simulator:

To run the Gazebo Sim to mirror your robot/SimMachine, use the following command (examples for Fr3):

 `$ ros2 launch fairino3_moveit2_config fr3_gazebo_mirror.launch.py`

To run the Gazebo Sim with a simulated Fairino ONLY, use the following command (examples for Fr3):

 `$ ros2 launch fairino3_moveit2_config digital_fr3_gazebo_sim.launch.py`

Note: that this can be done with any of the fairino models

<!-- Now, when you open a terminal and use 'rqt_graph' your setup should look like this:
    <img src="src/README_rqt_graph.png" width="1080"> -->


Now, you can set up a script using the SDK or ROS2 controllers to control your robot and watch it move in Gazebo!

To command the fully simulated robot, use the ROS2 /joint_trajectory message and send it to the corresponding Fairino ROS2 controller

### POSSIBLE ERRORS:

If your robot shows up as an entity in Gazebo but you cannot see the model, it is usually due to a conflicting resource path. To fix this, close gazebo and write in the following command to your terminal before re-running:

    export IGN_GAZEBO_RESOURCE_PATH=$IGN_GAZEBO_RESOURCE_PATH:~/[path-to-directory]/ros2_fr_gz/install/fairino_description/share

If your terminal says it cannot find the SimJointPublisher.py:
navigate to `/src/fairino{model_number}_moveit2_config/launch` and add an empty folder called "\_\_pycache\_\_"
Now rebuild your workspace.

## Step3) Run the MoveIt2 demo
<h4>To run the MoveIt2 demo system, use:</h4>

 `$ ros2 launch fairino{model_number}_v6_moveit2_config demo.launch.py`

-   <h4>Ex for Fr3:</h4> 
        
    `$ ros2 launch fairino3_v6_moveit2_config demo.launch.py`




    <!-- ### Step 1b) Choose your control method
    If you prefer to use the Fairino ROS2 API instead of the /joint_trajectories, you'll need to change the IP address in your workspace to match your SimMachine (defaulted to 192.168.58.2) and use <b> ros2 run fairino_hardware ros2_cmd_server</b> which runs
    <b> `src/fairino_hardware/include/src/command_server_node.cpp` </b> 

    An example program of this is in <b>~/ros2_fr_gz/src/fairino_hardware/examples/src/test_msg.py </b> -->