cmake_minimum_required(VERSION 3.22)
project(fairino_gazebo_config)

find_package(ament_cmake REQUIRED)

ament_package()
install(PROGRAMS
  launch/SimJointPublisher.py
  DESTINATION lib/${PROJECT_NAME}
)

