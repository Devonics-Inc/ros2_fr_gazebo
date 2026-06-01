cmake_minimum_required(VERSION 3.22)
project(rail_description)

find_package(ament_cmake REQUIRED)


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
install(DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
