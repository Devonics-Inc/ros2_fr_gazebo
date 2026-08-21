cmake_minimum_required(VERSION 3.22)
project(fairino_gazebo_config)

find_package(ament_cmake REQUIRED)



install(DIRECTORY launch config  DESTINATION share/${PROJECT_NAME}
  PATTERN "setup_assistant.launch" EXCLUDE)


install(PROGRAMS
  launch/SimJointPublisher.py
  launch/sim_trajectory_pub.py
  launch/launch_helpers.py
  src/gazebo_world_to_moveit.py
  src/scene_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
