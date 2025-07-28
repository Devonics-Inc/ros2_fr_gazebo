// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fairino_msgs:srv/RemoteCmdInterface.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__SRV__DETAIL__REMOTE_CMD_INTERFACE__BUILDER_HPP_
#define FAIRINO_MSGS__SRV__DETAIL__REMOTE_CMD_INTERFACE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fairino_msgs/srv/detail/remote_cmd_interface__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fairino_msgs
{

namespace srv
{

namespace builder
{

class Init_RemoteCmdInterface_Request_cmd_str
{
public:
  Init_RemoteCmdInterface_Request_cmd_str()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fairino_msgs::srv::RemoteCmdInterface_Request cmd_str(::fairino_msgs::srv::RemoteCmdInterface_Request::_cmd_str_type arg)
  {
    msg_.cmd_str = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fairino_msgs::srv::RemoteCmdInterface_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fairino_msgs::srv::RemoteCmdInterface_Request>()
{
  return fairino_msgs::srv::builder::Init_RemoteCmdInterface_Request_cmd_str();
}

}  // namespace fairino_msgs


namespace fairino_msgs
{

namespace srv
{

namespace builder
{

class Init_RemoteCmdInterface_Response_cmd_res
{
public:
  Init_RemoteCmdInterface_Response_cmd_res()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::fairino_msgs::srv::RemoteCmdInterface_Response cmd_res(::fairino_msgs::srv::RemoteCmdInterface_Response::_cmd_res_type arg)
  {
    msg_.cmd_res = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fairino_msgs::srv::RemoteCmdInterface_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::fairino_msgs::srv::RemoteCmdInterface_Response>()
{
  return fairino_msgs::srv::builder::Init_RemoteCmdInterface_Response_cmd_res();
}

}  // namespace fairino_msgs

#endif  // FAIRINO_MSGS__SRV__DETAIL__REMOTE_CMD_INTERFACE__BUILDER_HPP_
