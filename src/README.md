# Fairino ROS2 Driver (Version 3.7.8)

This document provides a quick tutorial for using MoveIt2 with Fairino Robots, compatible with web version 3.7.8. For a detailed guide, refer to the official documentation: [Fairino ROS2 Guide](https://fairino-doc-en.readthedocs.io/3.7.8/ROSGuide/index.html#frcobot-ros2).

## Checking the Robot Web Version

To verify the web version on your robot:
1. Open the Fairino Web App.
2. Navigate to **System > About**.
3. Confirm that the web version is **3.7.8**. If it differs, follow the steps below to update.

## Updating the Web Version

To change the web version to 3.7.8:
1. Download the software package from [Fairino Robot Software](https://fairino-doc-en.readthedocs.io/3.7.8/download.html#robot-software):
   - Select **FAIRINO-CobotSoftware-QX-V3.7.8-Release-250120**.
   - Unzip the folder to your file system.
2. In the Web App, go to **Application > Tool App > System Upgrade**.
3. In the **Software Upgrade** section, click **Choose File** and select `software.tar.gz` from the unzipped folder.
4. Click **Upload** and wait until the Web App prompts you to restart the control box.
5. After restarting, verify the web version in **System > About**.

## Setting Up the ROS2 Workspace

Follow these steps to set up your ROS2 environment and integrate the Fairino ROS2 Driver:

1. **Prepare the Environment**:
   - Ensure you have **Ubuntu 22.04** with **ROS2 Humble** installed. Refer to the [ROS2 Setup Guide](https://fairino-doc-en.readthedocs.io/3.7.8/ROSGuide/ros2guide.html) for detailed instructions.

2. **Create a ROS2 Workspace**:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws
   ```

3. **Download the Driver**:
   - Download and unzip the contents of the Fairino ROS2 Driver repository into the `~/ros2_ws/src` directory.

4. **Build the Workspace**:
   - To build all packages:
     ```bash
     colcon build
     source install/setup.bash
     ```
   - To build specific packages, use the following commands:
     - **fairino_msgs**:
       ```bash
       colcon build --packages-select fairino_msgs
       source install/setup.bash
       ```
     - **fairino_hardware**:
       ```bash
       colcon build --packages-select fairino_hardware
       source install/setup.bash
       ```
     - **fairino_description**:
       ```bash
       colcon build --packages-select fairino_description
       source install/setup.bash
       ```
     - **fairino5_v6_moveit2_config** (example MoveIt2 configuration):
       ```bash
       colcon build --packages-select fairino5_v6_moveit2_config
       source install/setup.bash
       ```

5. **Custom MoveIt2 Package** (Optional):
   - To create a customized MoveIt2 package, follow the [MoveIt2 Configuration Guide](https://fairino-doc-en.readthedocs.io/3.7.8/ROSGuide/moveIt2.html#configuring-the-moveit2-model-of-the-fairino-robotic-arm).

6. **Launch the Demo**:
   - For the default package (e.g., FR3):
     ```bash
     ros2 launch fairino3_v6_moveit2_config demo.launch.py
     ```
   - For a customized MoveIt2 package (e.g., FR3):
     ```bash
     ros2 launch fairino3_v6_robot_moveit_config smoveit_config demo.launch.py
     ```

   After launching, the robot should appear in the RViz environment in its packing position. You can:
   - **Set Target Position**: Drag and drop the blue sphere at the robot's end effector in the 3D interface (right side).
   - **Adjust End Effector Attitude**: Use the red, green, and blue rings to rotate the end effector.
   - **Plan Trajectory**: Click the **Plan** button on the left to generate a trajectory.
   - **Execute Movement**: Click the **Execute** button to move the robot along the planned trajectory.
   - **Plan & Execute**: Use the **Plan & Execute** button to automatically plan and execute the trajectory.
   - **Adjust Joint Angles**: Switch to the **Joints** tab to modify joint angles, then use the **Plan**, **Execute**, or **Plan & Execute** buttons to move the robot.

7. **Fairino Hardware Compilation**:
   - Compile the `fairino_hardware` plugin package as described above. Upon successful compilation, the file `libfairino_hardware.so` will be generated in `~/ros2_ws/install/fairino_hardware/lib/fairino_hardware`.
   - Edit the ROS2 control configuration file:
     - Open `~/ros2_ws/install/fairino3_v6_moveit2_config/share/fairino3_v6_moveit2_config/config/fairino3_v6_robot.ros2_control.xacro`.
     - Modify **line 9** as shown in the referenced image: [Configuration Image](https://github.com/user-attachments/assets/d9619e3b-cd95-4640-b7b8-6395d0482bab).
   - Re-run the demo launch file:
     ```bash
     source install/setup.bash
     ros2 launch fairino3_v6_moveit2_config demo.launch.py
     ```

   The robot's actual position should now be reflected in RViz, enabling control via MoveIt2 and RViz.
