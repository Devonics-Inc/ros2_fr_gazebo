#include "fairino_hardware/command_server.hpp"
#include "rclcpp/rclcpp.hpp"
#include "libfairino/include/robot.h"

int main(int argc, char *argv[]){
    // Main function used to create a simplified command client
    rclcpp::init(argc,argv);
    rclcpp::executors::SingleThreadedExecutor mulexecutor;
    // Below is the ROS2 command node; ALLOWS ONLY ROS2 COMMANDS, NO SDK
    // auto command_server_node = std::make_shared<robot_command_thread>("fr_command_server");
    // mulexecutor.add_node(command_server_node);
    
    // Create a non-real-time status feedback node
    auto robot_state_node = std::make_shared<robot_recv_thread>("fr_state_brodcast");
    mulexecutor.add_node(robot_state_node);// Add status feedback node to executable
    mulexecutor.spin();
    rclcpp::shutdown();
    return 0;
}
