cmake_minimum_required(VERSION 3.22)
project(controllers)

find_package(ament_cmake REQUIRED)


install(DIRECTORY ext_axis_controllers fairino_controllers gripper_controllers DESTINATION share/${PROJECT_NAME})


ament_package()
