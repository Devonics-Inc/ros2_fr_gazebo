cmake_minimum_required(VERSION 3.22)
project(rail_description)

find_package(ament_cmake REQUIRED)

<<<<<<< HEAD
install(PROGRAMS
  src/mill_goal_pub.py
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY config src
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
=======

#add_executable(gazebo_world_to_moveit src/gazebo_world_to_moveit.cpp)

#target_include_directories(gazebo_world_to_moveit PUBLIC
#	${ros_gz_INCLUDE_DIRS}
#	/usr/include/ignition/msgs8
#	/usr/include/ignition/gazebo6
#)
#install(TARGETS gazebo_world_to_moveit
#	DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
>>>>>>> 283bdb1ee8ab1ba60250def566606a6668c2fdaf
