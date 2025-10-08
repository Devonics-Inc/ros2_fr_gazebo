cmake_minimum_required(VERSION 3.22)
project(fairino_gazebo_config)

find_package(ament_cmake REQUIRED)


#add_executable(gazebo_world_to_moveit src/gazebo_world_to_moveit.cpp)

#target_include_directories(gazebo_world_to_moveit PUBLIC
#	${ros_gz_INCLUDE_DIRS}
#	/usr/include/ignition/msgs8
#	/usr/include/ignition/gazebo6
#)
#install(TARGETS gazebo_world_to_moveit
#	DESTINATION lib/${PROJECT_NAME})


install(PROGRAMS
  launch/SimJointPublisher.py
  launch/DigitalTwin_rsp.py
  launch/sim_trajectory_pub.py
  launch/rt_state_data.py
  src/gazebo_world_to_moveit.py
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
