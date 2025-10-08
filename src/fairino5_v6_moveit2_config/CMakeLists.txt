cmake_minimum_required(VERSION 3.22)
project(fairino5_v6_moveit2_config)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rclcpp REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(geometry_msgs REQUIRED)
ament_package()

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME}
  PATTERN "setup_assistant.launch" EXCLUDE)
  
  
add_executable(moveit_traj_test src/moveit_traj_test.cpp)
ament_target_dependencies(moveit_traj_test
  rclcpp
  moveit_ros_planning_interface
  geometry_msgs
)

install(TARGETS moveit_traj_test DESTINATION lib/${PROJECT_NAME})



install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
install(FILES .setup_assistant DESTINATION share/${PROJECT_NAME})
