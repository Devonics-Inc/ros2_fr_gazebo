// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fairino_msgs:srv/RemoteScriptContent.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__SRV__DETAIL__REMOTE_SCRIPT_CONTENT__TRAITS_HPP_
#define FAIRINO_MSGS__SRV__DETAIL__REMOTE_SCRIPT_CONTENT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fairino_msgs/srv/detail/remote_script_content__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fairino_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const RemoteScriptContent_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: line_str
  {
    out << "line_str: ";
    rosidl_generator_traits::value_to_yaml(msg.line_str, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RemoteScriptContent_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: line_str
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "line_str: ";
    rosidl_generator_traits::value_to_yaml(msg.line_str, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RemoteScriptContent_Request & msg, bool use_flow_style = false)
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
  const fairino_msgs::srv::RemoteScriptContent_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  fairino_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fairino_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const fairino_msgs::srv::RemoteScriptContent_Request & msg)
{
  return fairino_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fairino_msgs::srv::RemoteScriptContent_Request>()
{
  return "fairino_msgs::srv::RemoteScriptContent_Request";
}

template<>
inline const char * name<fairino_msgs::srv::RemoteScriptContent_Request>()
{
  return "fairino_msgs/srv/RemoteScriptContent_Request";
}

template<>
struct has_fixed_size<fairino_msgs::srv::RemoteScriptContent_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fairino_msgs::srv::RemoteScriptContent_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fairino_msgs::srv::RemoteScriptContent_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace fairino_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const RemoteScriptContent_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: res
  {
    out << "res: ";
    rosidl_generator_traits::value_to_yaml(msg.res, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RemoteScriptContent_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: res
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "res: ";
    rosidl_generator_traits::value_to_yaml(msg.res, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RemoteScriptContent_Response & msg, bool use_flow_style = false)
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
  const fairino_msgs::srv::RemoteScriptContent_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  fairino_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fairino_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const fairino_msgs::srv::RemoteScriptContent_Response & msg)
{
  return fairino_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<fairino_msgs::srv::RemoteScriptContent_Response>()
{
  return "fairino_msgs::srv::RemoteScriptContent_Response";
}

template<>
inline const char * name<fairino_msgs::srv::RemoteScriptContent_Response>()
{
  return "fairino_msgs/srv/RemoteScriptContent_Response";
}

template<>
struct has_fixed_size<fairino_msgs::srv::RemoteScriptContent_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fairino_msgs::srv::RemoteScriptContent_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fairino_msgs::srv::RemoteScriptContent_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fairino_msgs::srv::RemoteScriptContent>()
{
  return "fairino_msgs::srv::RemoteScriptContent";
}

template<>
inline const char * name<fairino_msgs::srv::RemoteScriptContent>()
{
  return "fairino_msgs/srv/RemoteScriptContent";
}

template<>
struct has_fixed_size<fairino_msgs::srv::RemoteScriptContent>
  : std::integral_constant<
    bool,
    has_fixed_size<fairino_msgs::srv::RemoteScriptContent_Request>::value &&
    has_fixed_size<fairino_msgs::srv::RemoteScriptContent_Response>::value
  >
{
};

template<>
struct has_bounded_size<fairino_msgs::srv::RemoteScriptContent>
  : std::integral_constant<
    bool,
    has_bounded_size<fairino_msgs::srv::RemoteScriptContent_Request>::value &&
    has_bounded_size<fairino_msgs::srv::RemoteScriptContent_Response>::value
  >
{
};

template<>
struct is_service<fairino_msgs::srv::RemoteScriptContent>
  : std::true_type
{
};

template<>
struct is_service_request<fairino_msgs::srv::RemoteScriptContent_Request>
  : std::true_type
{
};

template<>
struct is_service_response<fairino_msgs::srv::RemoteScriptContent_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // FAIRINO_MSGS__SRV__DETAIL__REMOTE_SCRIPT_CONTENT__TRAITS_HPP_
