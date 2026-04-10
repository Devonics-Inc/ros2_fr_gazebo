### This module is for the storage of various robot mounts/rails

## How to create a new rail:
### Step 1:
- Create a urdf.xacro for the new rail that contains the structure and collisions.
- When naming joints and links, follow the guidelines below:
    - Make the joint you want to move the name of the object + _joint. For example, if I had a new rail file called "new_rail.urdf.xacro", I would name the prismatic joint "new_rail_joint"
    - Make the base link the name of the new object + "_base"
    
            example: <link name="new_rail_base"/>

    - For the link where you want the robot to mount, name it new object + "_carriage" 
    
          example: <link name="new_rail_base"/>
    
    Use the "test_rail" located in this repo as a guide.

### Step2:
- Find the ros2_controllers.yaml file in the moveit2_config folder and add the proper controllers to the yaml.

