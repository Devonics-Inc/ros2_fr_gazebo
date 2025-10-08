#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/pose_stamped.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit_msgs/msg/collision_object.hpp>
#include <shape_msgs/msg/solid_primitive.hpp>

class MoveItPlannerNode : public rclcpp::Node
{
public:
  MoveItPlannerNode() : Node("moveit_test_planner")
  {
    RCLCPP_INFO(get_logger(), "Node constructed (but MoveGroup not yet initialized).");
  }

  void init_moveit()
  {
    const std::string PLANNING_GROUP = "fairino5_v6_group";

    // Now safe: shared_ptr to this node exists
    move_group_ = std::make_shared<moveit::planning_interface::MoveGroupInterface>(
        this->shared_from_this(), PLANNING_GROUP);

    planning_scene_interface_ = std::make_shared<moveit::planning_interface::PlanningSceneInterface>();

    RCLCPP_INFO(get_logger(), "MoveIt interfaces initialized.");

    addTestObject();
    planToPose();
  }

private:
  void addTestObject()
  {
    moveit_msgs::msg::CollisionObject collision_object;
    collision_object.header.frame_id = "base_link";
    collision_object.id = "test_box";

    shape_msgs::msg::SolidPrimitive primitive;
    primitive.type = primitive.BOX;
    primitive.dimensions = {0.1, 0.1, 0.1};

    geometry_msgs::msg::Pose box_pose;
    box_pose.position.x = 0.4;
    box_pose.position.y = 0.0;
    box_pose.position.z = 0.2;
    box_pose.orientation.w = 1.0;

    collision_object.primitives.push_back(primitive);
    collision_object.primitive_poses.push_back(box_pose);
    collision_object.operation = collision_object.ADD;

    planning_scene_interface_->applyCollisionObjects({collision_object});
    RCLCPP_INFO(get_logger(), "Added test box to planning scene.");
  }

  void planToPose()
  {
    geometry_msgs::msg::Pose target_pose;
    target_pose.orientation.w = 1.0;
    target_pose.position.x = 0.3;
    target_pose.position.y = 0.2;
    target_pose.position.z = 0.3;

    move_group_->setPoseTarget(target_pose);

    moveit::planning_interface::MoveGroupInterface::Plan plan;
    bool success = (move_group_->plan(plan) == moveit::core::MoveItErrorCode::SUCCESS);

    if (success)
    {
      RCLCPP_INFO(get_logger(), "Trajectory planned successfully.");
      RCLCPP_INFO(get_logger(), "Number of points: %zu", plan.trajectory_.joint_trajectory.points.size());

      size_t limit = std::min<size_t>(3, plan.trajectory_.joint_trajectory.points.size());
      for (size_t i = 0; i < limit; ++i)
      {
        const auto &pt = plan.trajectory_.joint_trajectory.points[i];
        std::ostringstream ss;
        ss << "Point " << i << ": [ ";
        for (double pos : pt.positions)
          ss << pos << " ";
        ss << "]";
        RCLCPP_INFO(get_logger(), "%s", ss.str().c_str());
      }
    }
    else
    {
      RCLCPP_WARN(get_logger(), "Failed to find a valid plan.");
    }
  }

  std::shared_ptr<moveit::planning_interface::MoveGroupInterface> move_group_;
  std::shared_ptr<moveit::planning_interface::PlanningSceneInterface> planning_scene_interface_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);

  // Node is now owned by shared_ptr BEFORE we call shared_from_this()
  auto node = std::make_shared<MoveItPlannerNode>();
  node->init_moveit();  // safe now

  rclcpp::spin_some(node);
  rclcpp::shutdown();
  return 0;
}
