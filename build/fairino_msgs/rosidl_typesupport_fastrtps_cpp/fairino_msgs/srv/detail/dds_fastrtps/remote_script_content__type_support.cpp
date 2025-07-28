// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from fairino_msgs:srv/RemoteScriptContent.idl
// generated code does not contain a copyright notice
#include "fairino_msgs/srv/detail/remote_script_content__rosidl_typesupport_fastrtps_cpp.hpp"
#include "fairino_msgs/srv/detail/remote_script_content__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace fairino_msgs
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
cdr_serialize(
  const fairino_msgs::srv::RemoteScriptContent_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: line_str
  cdr << ros_message.line_str;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  fairino_msgs::srv::RemoteScriptContent_Request & ros_message)
{
  // Member: line_str
  cdr >> ros_message.line_str;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
get_serialized_size(
  const fairino_msgs::srv::RemoteScriptContent_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: line_str
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.line_str.size() + 1);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
max_serialized_size_RemoteScriptContent_Request(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: line_str
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = fairino_msgs::srv::RemoteScriptContent_Request;
    is_plain =
      (
      offsetof(DataType, line_str) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _RemoteScriptContent_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const fairino_msgs::srv::RemoteScriptContent_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _RemoteScriptContent_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<fairino_msgs::srv::RemoteScriptContent_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _RemoteScriptContent_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const fairino_msgs::srv::RemoteScriptContent_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _RemoteScriptContent_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_RemoteScriptContent_Request(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _RemoteScriptContent_Request__callbacks = {
  "fairino_msgs::srv",
  "RemoteScriptContent_Request",
  _RemoteScriptContent_Request__cdr_serialize,
  _RemoteScriptContent_Request__cdr_deserialize,
  _RemoteScriptContent_Request__get_serialized_size,
  _RemoteScriptContent_Request__max_serialized_size
};

static rosidl_message_type_support_t _RemoteScriptContent_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_RemoteScriptContent_Request__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace fairino_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_fairino_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<fairino_msgs::srv::RemoteScriptContent_Request>()
{
  return &fairino_msgs::srv::typesupport_fastrtps_cpp::_RemoteScriptContent_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, fairino_msgs, srv, RemoteScriptContent_Request)() {
  return &fairino_msgs::srv::typesupport_fastrtps_cpp::_RemoteScriptContent_Request__handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include <limits>
// already included above
// #include <stdexcept>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
// already included above
// #include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace fairino_msgs
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
cdr_serialize(
  const fairino_msgs::srv::RemoteScriptContent_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: res
  cdr << ros_message.res;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  fairino_msgs::srv::RemoteScriptContent_Response & ros_message)
{
  // Member: res
  cdr >> ros_message.res;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
get_serialized_size(
  const fairino_msgs::srv::RemoteScriptContent_Response & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: res
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.res.size() + 1);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_fairino_msgs
max_serialized_size_RemoteScriptContent_Response(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: res
  {
    size_t array_size = 1;

    full_bounded = false;
    is_plain = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = fairino_msgs::srv::RemoteScriptContent_Response;
    is_plain =
      (
      offsetof(DataType, res) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _RemoteScriptContent_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const fairino_msgs::srv::RemoteScriptContent_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _RemoteScriptContent_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<fairino_msgs::srv::RemoteScriptContent_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _RemoteScriptContent_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const fairino_msgs::srv::RemoteScriptContent_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _RemoteScriptContent_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_RemoteScriptContent_Response(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _RemoteScriptContent_Response__callbacks = {
  "fairino_msgs::srv",
  "RemoteScriptContent_Response",
  _RemoteScriptContent_Response__cdr_serialize,
  _RemoteScriptContent_Response__cdr_deserialize,
  _RemoteScriptContent_Response__get_serialized_size,
  _RemoteScriptContent_Response__max_serialized_size
};

static rosidl_message_type_support_t _RemoteScriptContent_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_RemoteScriptContent_Response__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace fairino_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_fairino_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<fairino_msgs::srv::RemoteScriptContent_Response>()
{
  return &fairino_msgs::srv::typesupport_fastrtps_cpp::_RemoteScriptContent_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, fairino_msgs, srv, RemoteScriptContent_Response)() {
  return &fairino_msgs::srv::typesupport_fastrtps_cpp::_RemoteScriptContent_Response__handle;
}

#ifdef __cplusplus
}
#endif

#include "rmw/error_handling.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support_decl.hpp"

namespace fairino_msgs
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

static service_type_support_callbacks_t _RemoteScriptContent__callbacks = {
  "fairino_msgs::srv",
  "RemoteScriptContent",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, fairino_msgs, srv, RemoteScriptContent_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, fairino_msgs, srv, RemoteScriptContent_Response)(),
};

static rosidl_service_type_support_t _RemoteScriptContent__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_RemoteScriptContent__callbacks,
  get_service_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace fairino_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_fairino_msgs
const rosidl_service_type_support_t *
get_service_type_support_handle<fairino_msgs::srv::RemoteScriptContent>()
{
  return &fairino_msgs::srv::typesupport_fastrtps_cpp::_RemoteScriptContent__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, fairino_msgs, srv, RemoteScriptContent)() {
  return &fairino_msgs::srv::typesupport_fastrtps_cpp::_RemoteScriptContent__handle;
}

#ifdef __cplusplus
}
#endif
