// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from fairino_msgs:msg/RobotNonrtState.idl
// generated code does not contain a copyright notice
#include "fairino_msgs/msg/detail/robot_nonrt_state__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "fairino_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "fairino_msgs/msg/detail/robot_nonrt_state__struct.h"
#include "fairino_msgs/msg/detail/robot_nonrt_state__functions.h"
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

#include "rosidl_runtime_c/string.h"  // prg_name, version
#include "rosidl_runtime_c/string_functions.h"  // prg_name, version

// forward declare type support functions


using _RobotNonrtState__ros_msg_type = fairino_msgs__msg__RobotNonrtState;

static bool _RobotNonrtState__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _RobotNonrtState__ros_msg_type * ros_message = static_cast<const _RobotNonrtState__ros_msg_type *>(untyped_ros_message);
  // Field name: j1_cur_pos
  {
    cdr << ros_message->j1_cur_pos;
  }

  // Field name: j2_cur_pos
  {
    cdr << ros_message->j2_cur_pos;
  }

  // Field name: j3_cur_pos
  {
    cdr << ros_message->j3_cur_pos;
  }

  // Field name: j4_cur_pos
  {
    cdr << ros_message->j4_cur_pos;
  }

  // Field name: j5_cur_pos
  {
    cdr << ros_message->j5_cur_pos;
  }

  // Field name: j6_cur_pos
  {
    cdr << ros_message->j6_cur_pos;
  }

  // Field name: j1_cur_tor
  {
    cdr << ros_message->j1_cur_tor;
  }

  // Field name: j2_cur_tor
  {
    cdr << ros_message->j2_cur_tor;
  }

  // Field name: j3_cur_tor
  {
    cdr << ros_message->j3_cur_tor;
  }

  // Field name: j4_cur_tor
  {
    cdr << ros_message->j4_cur_tor;
  }

  // Field name: j5_cur_tor
  {
    cdr << ros_message->j5_cur_tor;
  }

  // Field name: j6_cur_tor
  {
    cdr << ros_message->j6_cur_tor;
  }

  // Field name: cart_x_cur_pos
  {
    cdr << ros_message->cart_x_cur_pos;
  }

  // Field name: cart_y_cur_pos
  {
    cdr << ros_message->cart_y_cur_pos;
  }

  // Field name: cart_z_cur_pos
  {
    cdr << ros_message->cart_z_cur_pos;
  }

  // Field name: cart_a_cur_pos
  {
    cdr << ros_message->cart_a_cur_pos;
  }

  // Field name: cart_b_cur_pos
  {
    cdr << ros_message->cart_b_cur_pos;
  }

  // Field name: cart_c_cur_pos
  {
    cdr << ros_message->cart_c_cur_pos;
  }

  // Field name: flange_x_cur_pos
  {
    cdr << ros_message->flange_x_cur_pos;
  }

  // Field name: flange_y_cur_pos
  {
    cdr << ros_message->flange_y_cur_pos;
  }

  // Field name: flange_z_cur_pos
  {
    cdr << ros_message->flange_z_cur_pos;
  }

  // Field name: flange_a_cur_pos
  {
    cdr << ros_message->flange_a_cur_pos;
  }

  // Field name: flange_b_cur_pos
  {
    cdr << ros_message->flange_b_cur_pos;
  }

  // Field name: flange_c_cur_pos
  {
    cdr << ros_message->flange_c_cur_pos;
  }

  // Field name: exaxispos1
  {
    cdr << ros_message->exaxispos1;
  }

  // Field name: exaxispos2
  {
    cdr << ros_message->exaxispos2;
  }

  // Field name: exaxispos3
  {
    cdr << ros_message->exaxispos3;
  }

  // Field name: exaxispos4
  {
    cdr << ros_message->exaxispos4;
  }

  // Field name: ft_fx_data
  {
    cdr << ros_message->ft_fx_data;
  }

  // Field name: ft_fy_data
  {
    cdr << ros_message->ft_fy_data;
  }

  // Field name: ft_fz_data
  {
    cdr << ros_message->ft_fz_data;
  }

  // Field name: ft_tx_data
  {
    cdr << ros_message->ft_tx_data;
  }

  // Field name: ft_ty_data
  {
    cdr << ros_message->ft_ty_data;
  }

  // Field name: ft_tz_data
  {
    cdr << ros_message->ft_tz_data;
  }

  // Field name: ft_actstatus
  {
    cdr << ros_message->ft_actstatus;
  }

  // Field name: robot_mode
  {
    cdr << ros_message->robot_mode;
  }

  // Field name: tool_num
  {
    cdr << ros_message->tool_num;
  }

  // Field name: work_num
  {
    cdr << ros_message->work_num;
  }

  // Field name: prg_state
  {
    cdr << ros_message->prg_state;
  }

  // Field name: abnormal_stop
  {
    cdr << ros_message->abnormal_stop;
  }

  // Field name: prg_name
  {
    const rosidl_runtime_c__String * str = &ros_message->prg_name;
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

  // Field name: prg_total_line
  {
    cdr << ros_message->prg_total_line;
  }

  // Field name: prg_cur_line
  {
    cdr << ros_message->prg_cur_line;
  }

  // Field name: dgt_output_h
  {
    cdr << ros_message->dgt_output_h;
  }

  // Field name: dgt_output_l
  {
    cdr << ros_message->dgt_output_l;
  }

  // Field name: dgt_input_h
  {
    cdr << ros_message->dgt_input_h;
  }

  // Field name: dgt_input_l
  {
    cdr << ros_message->dgt_input_l;
  }

  // Field name: tl_dgt_output_l
  {
    cdr << ros_message->tl_dgt_output_l;
  }

  // Field name: tl_dgt_input_l
  {
    cdr << ros_message->tl_dgt_input_l;
  }

  // Field name: emg
  {
    cdr << ros_message->emg;
  }

  // Field name: safetyboxsig
  {
    size_t size = 6;
    auto array_ptr = ros_message->safetyboxsig;
    cdr.serializeArray(array_ptr, size);
  }

  // Field name: robot_motion_done
  {
    cdr << ros_message->robot_motion_done;
  }

  // Field name: grip_motion_done
  {
    cdr << ros_message->grip_motion_done;
  }

  // Field name: weldbreakoffstate
  {
    cdr << ros_message->weldbreakoffstate;
  }

  // Field name: weldarcstate
  {
    cdr << ros_message->weldarcstate;
  }

  // Field name: error_code
  {
    cdr << ros_message->error_code;
  }

  // Field name: check_sum
  {
    cdr << ros_message->check_sum;
  }

  // Field name: timestamp
  {
    cdr << ros_message->timestamp;
  }

  // Field name: version
  {
    const rosidl_runtime_c__String * str = &ros_message->version;
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

static bool _RobotNonrtState__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _RobotNonrtState__ros_msg_type * ros_message = static_cast<_RobotNonrtState__ros_msg_type *>(untyped_ros_message);
  // Field name: j1_cur_pos
  {
    cdr >> ros_message->j1_cur_pos;
  }

  // Field name: j2_cur_pos
  {
    cdr >> ros_message->j2_cur_pos;
  }

  // Field name: j3_cur_pos
  {
    cdr >> ros_message->j3_cur_pos;
  }

  // Field name: j4_cur_pos
  {
    cdr >> ros_message->j4_cur_pos;
  }

  // Field name: j5_cur_pos
  {
    cdr >> ros_message->j5_cur_pos;
  }

  // Field name: j6_cur_pos
  {
    cdr >> ros_message->j6_cur_pos;
  }

  // Field name: j1_cur_tor
  {
    cdr >> ros_message->j1_cur_tor;
  }

  // Field name: j2_cur_tor
  {
    cdr >> ros_message->j2_cur_tor;
  }

  // Field name: j3_cur_tor
  {
    cdr >> ros_message->j3_cur_tor;
  }

  // Field name: j4_cur_tor
  {
    cdr >> ros_message->j4_cur_tor;
  }

  // Field name: j5_cur_tor
  {
    cdr >> ros_message->j5_cur_tor;
  }

  // Field name: j6_cur_tor
  {
    cdr >> ros_message->j6_cur_tor;
  }

  // Field name: cart_x_cur_pos
  {
    cdr >> ros_message->cart_x_cur_pos;
  }

  // Field name: cart_y_cur_pos
  {
    cdr >> ros_message->cart_y_cur_pos;
  }

  // Field name: cart_z_cur_pos
  {
    cdr >> ros_message->cart_z_cur_pos;
  }

  // Field name: cart_a_cur_pos
  {
    cdr >> ros_message->cart_a_cur_pos;
  }

  // Field name: cart_b_cur_pos
  {
    cdr >> ros_message->cart_b_cur_pos;
  }

  // Field name: cart_c_cur_pos
  {
    cdr >> ros_message->cart_c_cur_pos;
  }

  // Field name: flange_x_cur_pos
  {
    cdr >> ros_message->flange_x_cur_pos;
  }

  // Field name: flange_y_cur_pos
  {
    cdr >> ros_message->flange_y_cur_pos;
  }

  // Field name: flange_z_cur_pos
  {
    cdr >> ros_message->flange_z_cur_pos;
  }

  // Field name: flange_a_cur_pos
  {
    cdr >> ros_message->flange_a_cur_pos;
  }

  // Field name: flange_b_cur_pos
  {
    cdr >> ros_message->flange_b_cur_pos;
  }

  // Field name: flange_c_cur_pos
  {
    cdr >> ros_message->flange_c_cur_pos;
  }

  // Field name: exaxispos1
  {
    cdr >> ros_message->exaxispos1;
  }

  // Field name: exaxispos2
  {
    cdr >> ros_message->exaxispos2;
  }

  // Field name: exaxispos3
  {
    cdr >> ros_message->exaxispos3;
  }

  // Field name: exaxispos4
  {
    cdr >> ros_message->exaxispos4;
  }

  // Field name: ft_fx_data
  {
    cdr >> ros_message->ft_fx_data;
  }

  // Field name: ft_fy_data
  {
    cdr >> ros_message->ft_fy_data;
  }

  // Field name: ft_fz_data
  {
    cdr >> ros_message->ft_fz_data;
  }

  // Field name: ft_tx_data
  {
    cdr >> ros_message->ft_tx_data;
  }

  // Field name: ft_ty_data
  {
    cdr >> ros_message->ft_ty_data;
  }

  // Field name: ft_tz_data
  {
    cdr >> ros_message->ft_tz_data;
  }

  // Field name: ft_actstatus
  {
    cdr >> ros_message->ft_actstatus;
  }

  // Field name: robot_mode
  {
    cdr >> ros_message->robot_mode;
  }

  // Field name: tool_num
  {
    cdr >> ros_message->tool_num;
  }

  // Field name: work_num
  {
    cdr >> ros_message->work_num;
  }

  // Field name: prg_state
  {
    cdr >> ros_message->prg_state;
  }

  // Field name: abnormal_stop
  {
    cdr >> ros_message->abnormal_stop;
  }

  // Field name: prg_name
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->prg_name.data) {
      rosidl_runtime_c__String__init(&ros_message->prg_name);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->prg_name,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'prg_name'\n");
      return false;
    }
  }

  // Field name: prg_total_line
  {
    cdr >> ros_message->prg_total_line;
  }

  // Field name: prg_cur_line
  {
    cdr >> ros_message->prg_cur_line;
  }

  // Field name: dgt_output_h
  {
    cdr >> ros_message->dgt_output_h;
  }

  // Field name: dgt_output_l
  {
    cdr >> ros_message->dgt_output_l;
  }

  // Field name: dgt_input_h
  {
    cdr >> ros_message->dgt_input_h;
  }

  // Field name: dgt_input_l
  {
    cdr >> ros_message->dgt_input_l;
  }

  // Field name: tl_dgt_output_l
  {
    cdr >> ros_message->tl_dgt_output_l;
  }

  // Field name: tl_dgt_input_l
  {
    cdr >> ros_message->tl_dgt_input_l;
  }

  // Field name: emg
  {
    cdr >> ros_message->emg;
  }

  // Field name: safetyboxsig
  {
    size_t size = 6;
    auto array_ptr = ros_message->safetyboxsig;
    cdr.deserializeArray(array_ptr, size);
  }

  // Field name: robot_motion_done
  {
    cdr >> ros_message->robot_motion_done;
  }

  // Field name: grip_motion_done
  {
    cdr >> ros_message->grip_motion_done;
  }

  // Field name: weldbreakoffstate
  {
    cdr >> ros_message->weldbreakoffstate;
  }

  // Field name: weldarcstate
  {
    cdr >> ros_message->weldarcstate;
  }

  // Field name: error_code
  {
    cdr >> ros_message->error_code;
  }

  // Field name: check_sum
  {
    cdr >> ros_message->check_sum;
  }

  // Field name: timestamp
  {
    cdr >> ros_message->timestamp;
  }

  // Field name: version
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->version.data) {
      rosidl_runtime_c__String__init(&ros_message->version);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->version,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'version'\n");
      return false;
    }
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fairino_msgs
size_t get_serialized_size_fairino_msgs__msg__RobotNonrtState(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _RobotNonrtState__ros_msg_type * ros_message = static_cast<const _RobotNonrtState__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name j1_cur_pos
  {
    size_t item_size = sizeof(ros_message->j1_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j2_cur_pos
  {
    size_t item_size = sizeof(ros_message->j2_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j3_cur_pos
  {
    size_t item_size = sizeof(ros_message->j3_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j4_cur_pos
  {
    size_t item_size = sizeof(ros_message->j4_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j5_cur_pos
  {
    size_t item_size = sizeof(ros_message->j5_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j6_cur_pos
  {
    size_t item_size = sizeof(ros_message->j6_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j1_cur_tor
  {
    size_t item_size = sizeof(ros_message->j1_cur_tor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j2_cur_tor
  {
    size_t item_size = sizeof(ros_message->j2_cur_tor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j3_cur_tor
  {
    size_t item_size = sizeof(ros_message->j3_cur_tor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j4_cur_tor
  {
    size_t item_size = sizeof(ros_message->j4_cur_tor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j5_cur_tor
  {
    size_t item_size = sizeof(ros_message->j5_cur_tor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name j6_cur_tor
  {
    size_t item_size = sizeof(ros_message->j6_cur_tor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cart_x_cur_pos
  {
    size_t item_size = sizeof(ros_message->cart_x_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cart_y_cur_pos
  {
    size_t item_size = sizeof(ros_message->cart_y_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cart_z_cur_pos
  {
    size_t item_size = sizeof(ros_message->cart_z_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cart_a_cur_pos
  {
    size_t item_size = sizeof(ros_message->cart_a_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cart_b_cur_pos
  {
    size_t item_size = sizeof(ros_message->cart_b_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cart_c_cur_pos
  {
    size_t item_size = sizeof(ros_message->cart_c_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flange_x_cur_pos
  {
    size_t item_size = sizeof(ros_message->flange_x_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flange_y_cur_pos
  {
    size_t item_size = sizeof(ros_message->flange_y_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flange_z_cur_pos
  {
    size_t item_size = sizeof(ros_message->flange_z_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flange_a_cur_pos
  {
    size_t item_size = sizeof(ros_message->flange_a_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flange_b_cur_pos
  {
    size_t item_size = sizeof(ros_message->flange_b_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name flange_c_cur_pos
  {
    size_t item_size = sizeof(ros_message->flange_c_cur_pos);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name exaxispos1
  {
    size_t item_size = sizeof(ros_message->exaxispos1);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name exaxispos2
  {
    size_t item_size = sizeof(ros_message->exaxispos2);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name exaxispos3
  {
    size_t item_size = sizeof(ros_message->exaxispos3);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name exaxispos4
  {
    size_t item_size = sizeof(ros_message->exaxispos4);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_fx_data
  {
    size_t item_size = sizeof(ros_message->ft_fx_data);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_fy_data
  {
    size_t item_size = sizeof(ros_message->ft_fy_data);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_fz_data
  {
    size_t item_size = sizeof(ros_message->ft_fz_data);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_tx_data
  {
    size_t item_size = sizeof(ros_message->ft_tx_data);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_ty_data
  {
    size_t item_size = sizeof(ros_message->ft_ty_data);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_tz_data
  {
    size_t item_size = sizeof(ros_message->ft_tz_data);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ft_actstatus
  {
    size_t item_size = sizeof(ros_message->ft_actstatus);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name robot_mode
  {
    size_t item_size = sizeof(ros_message->robot_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tool_num
  {
    size_t item_size = sizeof(ros_message->tool_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name work_num
  {
    size_t item_size = sizeof(ros_message->work_num);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name prg_state
  {
    size_t item_size = sizeof(ros_message->prg_state);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name abnormal_stop
  {
    size_t item_size = sizeof(ros_message->abnormal_stop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name prg_name
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->prg_name.size + 1);
  // field.name prg_total_line
  {
    size_t item_size = sizeof(ros_message->prg_total_line);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name prg_cur_line
  {
    size_t item_size = sizeof(ros_message->prg_cur_line);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dgt_output_h
  {
    size_t item_size = sizeof(ros_message->dgt_output_h);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dgt_output_l
  {
    size_t item_size = sizeof(ros_message->dgt_output_l);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dgt_input_h
  {
    size_t item_size = sizeof(ros_message->dgt_input_h);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dgt_input_l
  {
    size_t item_size = sizeof(ros_message->dgt_input_l);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tl_dgt_output_l
  {
    size_t item_size = sizeof(ros_message->tl_dgt_output_l);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name tl_dgt_input_l
  {
    size_t item_size = sizeof(ros_message->tl_dgt_input_l);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name emg
  {
    size_t item_size = sizeof(ros_message->emg);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name safetyboxsig
  {
    size_t array_size = 6;
    auto array_ptr = ros_message->safetyboxsig;
    (void)array_ptr;
    size_t item_size = sizeof(array_ptr[0]);
    current_alignment += array_size * item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name robot_motion_done
  {
    size_t item_size = sizeof(ros_message->robot_motion_done);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name grip_motion_done
  {
    size_t item_size = sizeof(ros_message->grip_motion_done);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name weldbreakoffstate
  {
    size_t item_size = sizeof(ros_message->weldbreakoffstate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name weldarcstate
  {
    size_t item_size = sizeof(ros_message->weldarcstate);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name error_code
  {
    size_t item_size = sizeof(ros_message->error_code);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name check_sum
  {
    size_t item_size = sizeof(ros_message->check_sum);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name timestamp
  {
    size_t item_size = sizeof(ros_message->timestamp);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name version
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->version.size + 1);

  return current_alignment - initial_alignment;
}

static uint32_t _RobotNonrtState__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_fairino_msgs__msg__RobotNonrtState(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fairino_msgs
size_t max_serialized_size_fairino_msgs__msg__RobotNonrtState(
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

  // member: j1_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j2_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j3_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j4_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j5_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j6_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j1_cur_tor
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j2_cur_tor
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j3_cur_tor
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j4_cur_tor
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j5_cur_tor
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: j6_cur_tor
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cart_x_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cart_y_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cart_z_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cart_a_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cart_b_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cart_c_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: flange_x_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: flange_y_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: flange_z_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: flange_a_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: flange_b_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: flange_c_cur_pos
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: exaxispos1
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: exaxispos2
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: exaxispos3
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: exaxispos4
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_fx_data
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_fy_data
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_fz_data
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_tx_data
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_ty_data
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_tz_data
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ft_actstatus
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: robot_mode
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: tool_num
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: work_num
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: prg_state
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: abnormal_stop
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: prg_name
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
  // member: prg_total_line
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: prg_cur_line
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: dgt_output_h
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: dgt_output_l
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: dgt_input_h
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: dgt_input_l
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: tl_dgt_output_l
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: tl_dgt_input_l
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: emg
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: safetyboxsig
  {
    size_t array_size = 6;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: robot_motion_done
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: grip_motion_done
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: weldbreakoffstate
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: weldarcstate
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: error_code
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: check_sum
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: timestamp
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint64_t);
    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: version
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
    using DataType = fairino_msgs__msg__RobotNonrtState;
    is_plain =
      (
      offsetof(DataType, version) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static size_t _RobotNonrtState__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_fairino_msgs__msg__RobotNonrtState(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_RobotNonrtState = {
  "fairino_msgs::msg",
  "RobotNonrtState",
  _RobotNonrtState__cdr_serialize,
  _RobotNonrtState__cdr_deserialize,
  _RobotNonrtState__get_serialized_size,
  _RobotNonrtState__max_serialized_size
};

static rosidl_message_type_support_t _RobotNonrtState__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_RobotNonrtState,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fairino_msgs, msg, RobotNonrtState)() {
  return &_RobotNonrtState__type_support;
}

#if defined(__cplusplus)
}
#endif
