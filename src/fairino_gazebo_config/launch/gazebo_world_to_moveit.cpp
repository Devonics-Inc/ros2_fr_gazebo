#include <gz/transport/Node.hh>
#include <rclcpp/rclcpp.hpp>
#include <ros_gz_interfaces/msg/serialized_step_map.hpp>

class WorldStateBridge : public rclcpp::Node {
public:
  WorldStateBridge() : Node("gz_world_state_bridge") {
    // Initialize Gazebo transport node
    gz_node.Subscribe("/world/empty/state", &WorldStateBridge::OnWorldState, this);
  }

private:
  void OnWorldState(const gz::msgs::SerializedStepMap &msg) {
    RCLCPP_INFO(this->get_logger(), "Received world state with %d models",
                msg.state().model_size());
  }

  gz::transport::Node gz_node;
};

int main(int argc, char **argv) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<WorldStateBridge>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
