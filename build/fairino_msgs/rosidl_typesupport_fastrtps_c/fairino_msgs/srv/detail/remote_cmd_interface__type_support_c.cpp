// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from fairino_msgs:srv/RemoteCmdInterface.idl
// generated code does not contain a copyright notice
#include "fairino_msgs/srv/detail/remote_cmd_interface__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "fairino_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "fairino_msgs/srv/detail/remote_cmd_interface__struct.h"
#include "fairino_msgs/srv/detail/remote_cmd_interface__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "rosidl_runtime_c/string.h"  // cmd_str
#include "rosidl_runtime_c/string_functions.h"  // cmd_str

// forward declare type support functions


using _RemoteCmdInterface_Request__ros_msg_type = fairino_msgs__srv__RemoteCmdInterface_Request;

static bool _RemoteCmdInterface_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RemoteCmdInterface_Request__ros_msg_type * ros_message = static_cast<const _RemoteCmdInterface_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd_str
  {
    const rosidl_runtime_c__String * str = &ros_message->cmd_str;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _RemoteCmdInterface_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RemoteCmdInterface_Request__ros_msg_type * ros_message = static_cast<_RemoteCmdInterface_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd_str
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->cmd_str.data) {
      rosidl_runtime_c__String__init(&ros_message->cmd_str);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->cmd_str,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'cmd_str'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fairino_msgs
size_t get_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RemoteCmdInterface_Request__ros_msg_type * ros_message = static_cast<const _RemoteCmdInterface_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name cmd_str
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->cmd_str.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _RemoteCmdInterface_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fairino_msgs
size_t max_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Request(
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

  // member: cmd_str
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
    using DataType = fairino_msgs__srv__RemoteCmdInterface_Request;
    is_plain =
      (
      offsetof(DataType, cmd_str) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RemoteCmdInterface_Request__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Request(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RemoteCmdInterface_Request = {
  "fairino_msgs::srv",
  "RemoteCmdInterface_Request",
  _RemoteCmdInterface_Request__cdr_serialize,
  _RemoteCmdInterface_Request__cdr_deserialize,
  _RemoteCmdInterface_Request__get_serialized_size,
  _RemoteCmdInterface_Request__max_serialized_size
};

static rosidl_message_type_support_t _RemoteCmdInterface_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RemoteCmdInterface_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fairino_msgs, srv, RemoteCmdInterface_Request)() {
  return &_RemoteCmdInterface_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "fairino_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "fairino_msgs/srv/detail/remote_cmd_interface__struct.h"
// already included above
// #include "fairino_msgs/srv/detail/remote_cmd_interface__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

// already included above
// #include "rosidl_runtime_c/string.h"  // cmd_res
// already included above
// #include "rosidl_runtime_c/string_functions.h"  // cmd_res

// forward declare type support functions


using _RemoteCmdInterface_Response__ros_msg_type = fairino_msgs__srv__RemoteCmdInterface_Response;

static bool _RemoteCmdInterface_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RemoteCmdInterface_Response__ros_msg_type * ros_message = static_cast<const _RemoteCmdInterface_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd_res
  {
    const rosidl_runtime_c__String * str = &ros_message->cmd_res;
    if (str->capacity == 0 || str->capacity <= str->size) {
      fprintf(stderr, "string capacity not greater than size\n");
      return false;
    }
    if (str->data[str->size] != '\0') {
      fprintf(stderr, "string not null-terminated\n");
      return false;
    }
    cdr << str->data;
  }

  return true;
}

static bool _RemoteCmdInterface_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RemoteCmdInterface_Response__ros_msg_type * ros_message = static_cast<_RemoteCmdInterface_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: cmd_res
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->cmd_res.data) {
      rosidl_runtime_c__String__init(&ros_message->cmd_res);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->cmd_res,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'cmd_res'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fairino_msgs
size_t get_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RemoteCmdInterface_Response__ros_msg_type * ros_message = static_cast<const _RemoteCmdInterface_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name cmd_res
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->cmd_res.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _RemoteCmdInterface_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fairino_msgs
size_t max_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Response(
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

  // member: cmd_res
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
    using DataType = fairino_msgs__srv__RemoteCmdInterface_Response;
    is_plain =
      (
      offsetof(DataType, cmd_res) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RemoteCmdInterface_Response__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_fairino_msgs__srv__RemoteCmdInterface_Response(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RemoteCmdInterface_Response = {
  "fairino_msgs::srv",
  "RemoteCmdInterface_Response",
  _RemoteCmdInterface_Response__cdr_serialize,
  _RemoteCmdInterface_Response__cdr_deserialize,
  _RemoteCmdInterface_Response__get_serialized_size,
  _RemoteCmdInterface_Response__max_serialized_size
};

static rosidl_message_type_support_t _RemoteCmdInterface_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RemoteCmdInterface_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fairino_msgs, srv, RemoteCmdInterface_Response)() {
  return &_RemoteCmdInterface_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "fairino_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "fairino_msgs/srv/remote_cmd_interface.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t RemoteCmdInterface__callbacks = {
  "fairino_msgs::srv",
  "RemoteCmdInterface",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fairino_msgs, srv, RemoteCmdInterface_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fairino_msgs, srv, RemoteCmdInterface_Response)(),
};

static rosidl_service_type_support_t RemoteCmdInterface__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &RemoteCmdInterface__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fairino_msgs, srv, RemoteCmdInterface)() {
  return &RemoteCmdInterface__handle;
}

#if defined(__cplusplus)
}
#endif
