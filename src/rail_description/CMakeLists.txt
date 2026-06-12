cmake_minimum_required(VERSION 3.22)
project(rail_description)

find_package(ament_cmake REQUIRED)

install(PROGRAMS
  src/mill_goal_pub.py
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY config src
  DESTINATION share/${PROJECT_NAME}
)

ament_package()