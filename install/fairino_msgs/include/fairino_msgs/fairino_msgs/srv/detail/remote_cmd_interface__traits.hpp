// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fairino_msgs:srv/RemoteCmdInterface.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__SRV__DETAIL__REMOTE_CMD_INTERFACE__TRAITS_HPP_
#define FAIRINO_MSGS__SRV__DETAIL__REMOTE_CMD_INTERFACE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fairino_msgs/srv/detail/remote_cmd_interface__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fairino_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const RemoteCmdInterface_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: cmd_str
  {
    out << "cmd_str: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_str, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RemoteCmdInterface_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: cmd_str
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_str: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_str, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RemoteCmdInterface_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fairino_msgs

namespace rosidl_generator_traits
{

[[deprecated("use fairino_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fairino_msgs::srv::RemoteCmdInterface_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fairino_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fairino_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const fairino_msgs::srv::RemoteCmdInterface_Request & msg)
{
  return fairino_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fairino_msgs::srv::RemoteCmdInterface_Request>()
{
  return "fairino_msgs::srv::RemoteCmdInterface_Request";
}

template<>
inline const char * name<fairino_msgs::srv::RemoteCmdInterface_Request>()
{
  return "fairino_msgs/srv/RemoteCmdInterface_Request";
}

template<>
struct has_fixed_size<fairino_msgs::srv::RemoteCmdInterface_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fairino_msgs::srv::RemoteCmdInterface_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fairino_msgs::srv::RemoteCmdInterface_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace fairino_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const RemoteCmdInterface_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: cmd_res
  {
    out << "cmd_res: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_res, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RemoteCmdInterface_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: cmd_res
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cmd_res: ";
    rosidl_generator_traits::value_to_yaml(msg.cmd_res, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RemoteCmdInterface_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace fairino_msgs

namespace rosidl_generator_traits
{

[[deprecated("use fairino_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fairino_msgs::srv::RemoteCmdInterface_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fairino_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fairino_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const fairino_msgs::srv::RemoteCmdInterface_Response & msg)
{
  return fairino_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fairino_msgs::srv::RemoteCmdInterface_Response>()
{
  return "fairino_msgs::srv::RemoteCmdInterface_Response";
}

template<>
inline const char * name<fairino_msgs::srv::RemoteCmdInterface_Response>()
{
  return "fairino_msgs/srv/RemoteCmdInterface_Response";
}

template<>
struct has_fixed_size<fairino_msgs::srv::RemoteCmdInterface_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fairino_msgs::srv::RemoteCmdInterface_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fairino_msgs::srv::RemoteCmdInterface_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fairino_msgs::srv::RemoteCmdInterface>()
{
  return "fairino_msgs::srv::RemoteCmdInterface";
}

template<>
inline const char * name<fairino_msgs::srv::RemoteCmdInterface>()
{
  return "fairino_msgs/srv/RemoteCmdInterface";
}

template<>
struct has_fixed_size<fairino_msgs::srv::RemoteCmdInterface>
  : std::integral_constant<
    bool,
    has_fixed_size<fairino_msgs::srv::RemoteCmdInterface_Request>::value &&
    has_fixed_size<fairino_msgs::srv::RemoteCmdInterface_Response>::value
  >
{
};

template<>
struct has_bounded_size<fairino_msgs::srv::RemoteCmdInterface>
  : std::integral_constant<
    bool,
    has_bounded_size<fairino_msgs::srv::RemoteCmdInterface_Request>::value &&
    has_bounded_size<fairino_msgs::srv::RemoteCmdInterface_Response>::value
  >
{
};

template<>
struct is_service<fairino_msgs::srv::RemoteCmdInterface>
  : std::true_type
{
};

template<>
struct is_service_request<fairino_msgs::srv::RemoteCmdInterface_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fairino_msgs::srv::RemoteCmdInterface_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FAIRINO_MSGS__SRV__DETAIL__REMOTE_CMD_INTERFACE__TRAITS_HPP_
