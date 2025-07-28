// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fairino_msgs:msg/RobotNonrtState.idl
// generated code does not contain a copyright notice
#include "fairino_msgs/msg/detail/robot_nonrt_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `prg_name`
// Member `version`
#include "rosidl_runtime_c/string_functions.h"

bool
fairino_msgs__msg__RobotNonrtState__init(fairino_msgs__msg__RobotNonrtState * msg)
{
  if (!msg) {
    return false;
  }
  // j1_cur_pos
  // j2_cur_pos
  // j3_cur_pos
  // j4_cur_pos
  // j5_cur_pos
  // j6_cur_pos
  // j1_cur_tor
  // j2_cur_tor
  // j3_cur_tor
  // j4_cur_tor
  // j5_cur_tor
  // j6_cur_tor
  // cart_x_cur_pos
  // cart_y_cur_pos
  // cart_z_cur_pos
  // cart_a_cur_pos
  // cart_b_cur_pos
  // cart_c_cur_pos
  // flange_x_cur_pos
  // flange_y_cur_pos
  // flange_z_cur_pos
  // flange_a_cur_pos
  // flange_b_cur_pos
  // flange_c_cur_pos
  // exaxispos1
  // exaxispos2
  // exaxispos3
  // exaxispos4
  // ft_fx_data
  // ft_fy_data
  // ft_fz_data
  // ft_tx_data
  // ft_ty_data
  // ft_tz_data
  // ft_actstatus
  // robot_mode
  // tool_num
  // work_num
  // prg_state
  // abnormal_stop
  // prg_name
  if (!rosidl_runtime_c__String__init(&msg->prg_name)) {
    fairino_msgs__msg__RobotNonrtState__fini(msg);
    return false;
  }
  // prg_total_line
  // prg_cur_line
  // dgt_output_h
  // dgt_output_l
  // dgt_input_h
  // dgt_input_l
  // tl_dgt_output_l
  // tl_dgt_input_l
  // emg
  // safetyboxsig
  // robot_motion_done
  // grip_motion_done
  // weldbreakoffstate
  // weldarcstate
  // error_code
  // check_sum
  // timestamp
  // version
  if (!rosidl_runtime_c__String__init(&msg->version)) {
    fairino_msgs__msg__RobotNonrtState__fini(msg);
    return false;
  }
  return true;
}

void
fairino_msgs__msg__RobotNonrtState__fini(fairino_msgs__msg__RobotNonrtState * msg)
{
  if (!msg) {
    return;
  }
  // j1_cur_pos
  // j2_cur_pos
  // j3_cur_pos
  // j4_cur_pos
  // j5_cur_pos
  // j6_cur_pos
  // j1_cur_tor
  // j2_cur_tor
  // j3_cur_tor
  // j4_cur_tor
  // j5_cur_tor
  // j6_cur_tor
  // cart_x_cur_pos
  // cart_y_cur_pos
  // cart_z_cur_pos
  // cart_a_cur_pos
  // cart_b_cur_pos
  // cart_c_cur_pos
  // flange_x_cur_pos
  // flange_y_cur_pos
  // flange_z_cur_pos
  // flange_a_cur_pos
  // flange_b_cur_pos
  // flange_c_cur_pos
  // exaxispos1
  // exaxispos2
  // exaxispos3
  // exaxispos4
  // ft_fx_data
  // ft_fy_data
  // ft_fz_data
  // ft_tx_data
  // ft_ty_data
  // ft_tz_data
  // ft_actstatus
  // robot_mode
  // tool_num
  // work_num
  // prg_state
  // abnormal_stop
  // prg_name
  rosidl_runtime_c__String__fini(&msg->prg_name);
  // prg_total_line
  // prg_cur_line
  // dgt_output_h
  // dgt_output_l
  // dgt_input_h
  // dgt_input_l
  // tl_dgt_output_l
  // tl_dgt_input_l
  // emg
  // safetyboxsig
  // robot_motion_done
  // grip_motion_done
  // weldbreakoffstate
  // weldarcstate
  // error_code
  // check_sum
  // timestamp
  // version
  rosidl_runtime_c__String__fini(&msg->version);
}

bool
fairino_msgs__msg__RobotNonrtState__are_equal(const fairino_msgs__msg__RobotNonrtState * lhs, const fairino_msgs__msg__RobotNonrtState * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // j1_cur_pos
  if (lhs->j1_cur_pos != rhs->j1_cur_pos) {
    return false;
  }
  // j2_cur_pos
  if (lhs->j2_cur_pos != rhs->j2_cur_pos) {
    return false;
  }
  // j3_cur_pos
  if (lhs->j3_cur_pos != rhs->j3_cur_pos) {
    return false;
  }
  // j4_cur_pos
  if (lhs->j4_cur_pos != rhs->j4_cur_pos) {
    return false;
  }
  // j5_cur_pos
  if (lhs->j5_cur_pos != rhs->j5_cur_pos) {
    return false;
  }
  // j6_cur_pos
  if (lhs->j6_cur_pos != rhs->j6_cur_pos) {
    return false;
  }
  // j1_cur_tor
  if (lhs->j1_cur_tor != rhs->j1_cur_tor) {
    return false;
  }
  // j2_cur_tor
  if (lhs->j2_cur_tor != rhs->j2_cur_tor) {
    return false;
  }
  // j3_cur_tor
  if (lhs->j3_cur_tor != rhs->j3_cur_tor) {
    return false;
  }
  // j4_cur_tor
  if (lhs->j4_cur_tor != rhs->j4_cur_tor) {
    return false;
  }
  // j5_cur_tor
  if (lhs->j5_cur_tor != rhs->j5_cur_tor) {
    return false;
  }
  // j6_cur_tor
  if (lhs->j6_cur_tor != rhs->j6_cur_tor) {
    return false;
  }
  // cart_x_cur_pos
  if (lhs->cart_x_cur_pos != rhs->cart_x_cur_pos) {
    return false;
  }
  // cart_y_cur_pos
  if (lhs->cart_y_cur_pos != rhs->cart_y_cur_pos) {
    return false;
  }
  // cart_z_cur_pos
  if (lhs->cart_z_cur_pos != rhs->cart_z_cur_pos) {
    return false;
  }
  // cart_a_cur_pos
  if (lhs->cart_a_cur_pos != rhs->cart_a_cur_pos) {
    return false;
  }
  // cart_b_cur_pos
  if (lhs->cart_b_cur_pos != rhs->cart_b_cur_pos) {
    return false;
  }
  // cart_c_cur_pos
  if (lhs->cart_c_cur_pos != rhs->cart_c_cur_pos) {
    return false;
  }
  // flange_x_cur_pos
  if (lhs->flange_x_cur_pos != rhs->flange_x_cur_pos) {
    return false;
  }
  // flange_y_cur_pos
  if (lhs->flange_y_cur_pos != rhs->flange_y_cur_pos) {
    return false;
  }
  // flange_z_cur_pos
  if (lhs->flange_z_cur_pos != rhs->flange_z_cur_pos) {
    return false;
  }
  // flange_a_cur_pos
  if (lhs->flange_a_cur_pos != rhs->flange_a_cur_pos) {
    return false;
  }
  // flange_b_cur_pos
  if (lhs->flange_b_cur_pos != rhs->flange_b_cur_pos) {
    return false;
  }
  // flange_c_cur_pos
  if (lhs->flange_c_cur_pos != rhs->flange_c_cur_pos) {
    return false;
  }
  // exaxispos1
  if (lhs->exaxispos1 != rhs->exaxispos1) {
    return false;
  }
  // exaxispos2
  if (lhs->exaxispos2 != rhs->exaxispos2) {
    return false;
  }
  // exaxispos3
  if (lhs->exaxispos3 != rhs->exaxispos3) {
    return false;
  }
  // exaxispos4
  if (lhs->exaxispos4 != rhs->exaxispos4) {
    return false;
  }
  // ft_fx_data
  if (lhs->ft_fx_data != rhs->ft_fx_data) {
    return false;
  }
  // ft_fy_data
  if (lhs->ft_fy_data != rhs->ft_fy_data) {
    return false;
  }
  // ft_fz_data
  if (lhs->ft_fz_data != rhs->ft_fz_data) {
    return false;
  }
  // ft_tx_data
  if (lhs->ft_tx_data != rhs->ft_tx_data) {
    return false;
  }
  // ft_ty_data
  if (lhs->ft_ty_data != rhs->ft_ty_data) {
    return false;
  }
  // ft_tz_data
  if (lhs->ft_tz_data != rhs->ft_tz_data) {
    return false;
  }
  // ft_actstatus
  if (lhs->ft_actstatus != rhs->ft_actstatus) {
    return false;
  }
  // robot_mode
  if (lhs->robot_mode != rhs->robot_mode) {
    return false;
  }
  // tool_num
  if (lhs->tool_num != rhs->tool_num) {
    return false;
  }
  // work_num
  if (lhs->work_num != rhs->work_num) {
    return false;
  }
  // prg_state
  if (lhs->prg_state != rhs->prg_state) {
    return false;
  }
  // abnormal_stop
  if (lhs->abnormal_stop != rhs->abnormal_stop) {
    return false;
  }
  // prg_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->prg_name), &(rhs->prg_name)))
  {
    return false;
  }
  // prg_total_line
  if (lhs->prg_total_line != rhs->prg_total_line) {
    return false;
  }
  // prg_cur_line
  if (lhs->prg_cur_line != rhs->prg_cur_line) {
    return false;
  }
  // dgt_output_h
  if (lhs->dgt_output_h != rhs->dgt_output_h) {
    return false;
  }
  // dgt_output_l
  if (lhs->dgt_output_l != rhs->dgt_output_l) {
    return false;
  }
  // dgt_input_h
  if (lhs->dgt_input_h != rhs->dgt_input_h) {
    return false;
  }
  // dgt_input_l
  if (lhs->dgt_input_l != rhs->dgt_input_l) {
    return false;
  }
  // tl_dgt_output_l
  if (lhs->tl_dgt_output_l != rhs->tl_dgt_output_l) {
    return false;
  }
  // tl_dgt_input_l
  if (lhs->tl_dgt_input_l != rhs->tl_dgt_input_l) {
    return false;
  }
  // emg
  if (lhs->emg != rhs->emg) {
    return false;
  }
  // safetyboxsig
  for (size_t i = 0; i < 6; ++i) {
    if (lhs->safetyboxsig[i] != rhs->safetyboxsig[i]) {
      return false;
    }
  }
  // robot_motion_done
  if (lhs->robot_motion_done != rhs->robot_motion_done) {
    return false;
  }
  // grip_motion_done
  if (lhs->grip_motion_done != rhs->grip_motion_done) {
    return false;
  }
  // weldbreakoffstate
  if (lhs->weldbreakoffstate != rhs->weldbreakoffstate) {
    return false;
  }
  // weldarcstate
  if (lhs->weldarcstate != rhs->weldarcstate) {
    return false;
  }
  // error_code
  if (lhs->error_code != rhs->error_code) {
    return false;
  }
  // check_sum
  if (lhs->check_sum != rhs->check_sum) {
    return false;
  }
  // timestamp
  if (lhs->timestamp != rhs->timestamp) {
    return false;
  }
  // version
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->version), &(rhs->version)))
  {
    return false;
  }
  return true;
}

bool
fairino_msgs__msg__RobotNonrtState__copy(
  const fairino_msgs__msg__RobotNonrtState * input,
  fairino_msgs__msg__RobotNonrtState * output)
{
  if (!input || !output) {
    return false;
  }
  // j1_cur_pos
  output->j1_cur_pos = input->j1_cur_pos;
  // j2_cur_pos
  output->j2_cur_pos = input->j2_cur_pos;
  // j3_cur_pos
  output->j3_cur_pos = input->j3_cur_pos;
  // j4_cur_pos
  output->j4_cur_pos = input->j4_cur_pos;
  // j5_cur_pos
  output->j5_cur_pos = input->j5_cur_pos;
  // j6_cur_pos
  output->j6_cur_pos = input->j6_cur_pos;
  // j1_cur_tor
  output->j1_cur_tor = input->j1_cur_tor;
  // j2_cur_tor
  output->j2_cur_tor = input->j2_cur_tor;
  // j3_cur_tor
  output->j3_cur_tor = input->j3_cur_tor;
  // j4_cur_tor
  output->j4_cur_tor = input->j4_cur_tor;
  // j5_cur_tor
  output->j5_cur_tor = input->j5_cur_tor;
  // j6_cur_tor
  output->j6_cur_tor = input->j6_cur_tor;
  // cart_x_cur_pos
  output->cart_x_cur_pos = input->cart_x_cur_pos;
  // cart_y_cur_pos
  output->cart_y_cur_pos = input->cart_y_cur_pos;
  // cart_z_cur_pos
  output->cart_z_cur_pos = input->cart_z_cur_pos;
  // cart_a_cur_pos
  output->cart_a_cur_pos = input->cart_a_cur_pos;
  // cart_b_cur_pos
  output->cart_b_cur_pos = input->cart_b_cur_pos;
  // cart_c_cur_pos
  output->cart_c_cur_pos = input->cart_c_cur_pos;
  // flange_x_cur_pos
  output->flange_x_cur_pos = input->flange_x_cur_pos;
  // flange_y_cur_pos
  output->flange_y_cur_pos = input->flange_y_cur_pos;
  // flange_z_cur_pos
  output->flange_z_cur_pos = input->flange_z_cur_pos;
  // flange_a_cur_pos
  output->flange_a_cur_pos = input->flange_a_cur_pos;
  // flange_b_cur_pos
  output->flange_b_cur_pos = input->flange_b_cur_pos;
  // flange_c_cur_pos
  output->flange_c_cur_pos = input->flange_c_cur_pos;
  // exaxispos1
  output->exaxispos1 = input->exaxispos1;
  // exaxispos2
  output->exaxispos2 = input->exaxispos2;
  // exaxispos3
  output->exaxispos3 = input->exaxispos3;
  // exaxispos4
  output->exaxispos4 = input->exaxispos4;
  // ft_fx_data
  output->ft_fx_data = input->ft_fx_data;
  // ft_fy_data
  output->ft_fy_data = input->ft_fy_data;
  // ft_fz_data
  output->ft_fz_data = input->ft_fz_data;
  // ft_tx_data
  output->ft_tx_data = input->ft_tx_data;
  // ft_ty_data
  output->ft_ty_data = input->ft_ty_data;
  // ft_tz_data
  output->ft_tz_data = input->ft_tz_data;
  // ft_actstatus
  output->ft_actstatus = input->ft_actstatus;
  // robot_mode
  output->robot_mode = input->robot_mode;
  // tool_num
  output->tool_num = input->tool_num;
  // work_num
  output->work_num = input->work_num;
  // prg_state
  output->prg_state = input->prg_state;
  // abnormal_stop
  output->abnormal_stop = input->abnormal_stop;
  // prg_name
  if (!rosidl_runtime_c__String__copy(
      &(input->prg_name), &(output->prg_name)))
  {
    return false;
  }
  // prg_total_line
  output->prg_total_line = input->prg_total_line;
  // prg_cur_line
  output->prg_cur_line = input->prg_cur_line;
  // dgt_output_h
  output->dgt_output_h = input->dgt_output_h;
  // dgt_output_l
  output->dgt_output_l = input->dgt_output_l;
  // dgt_input_h
  output->dgt_input_h = input->dgt_input_h;
  // dgt_input_l
  output->dgt_input_l = input->dgt_input_l;
  // tl_dgt_output_l
  output->tl_dgt_output_l = input->tl_dgt_output_l;
  // tl_dgt_input_l
  output->tl_dgt_input_l = input->tl_dgt_input_l;
  // emg
  output->emg = input->emg;
  // safetyboxsig
  for (size_t i = 0; i < 6; ++i) {
    output->safetyboxsig[i] = input->safetyboxsig[i];
  }
  // robot_motion_done
  output->robot_motion_done = input->robot_motion_done;
  // grip_motion_done
  output->grip_motion_done = input->grip_motion_done;
  // weldbreakoffstate
  output->weldbreakoffstate = input->weldbreakoffstate;
  // weldarcstate
  output->weldarcstate = input->weldarcstate;
  // error_code
  output->error_code = input->error_code;
  // check_sum
  output->check_sum = input->check_sum;
  // timestamp
  output->timestamp = input->timestamp;
  // version
  if (!rosidl_runtime_c__String__copy(
      &(input->version), &(output->version)))
  {
    return false;
  }
  return true;
}

fairino_msgs__msg__RobotNonrtState *
fairino_msgs__msg__RobotNonrtState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__msg__RobotNonrtState * msg = (fairino_msgs__msg__RobotNonrtState *)allocator.allocate(sizeof(fairino_msgs__msg__RobotNonrtState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fairino_msgs__msg__RobotNonrtState));
  bool success = fairino_msgs__msg__RobotNonrtState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fairino_msgs__msg__RobotNonrtState__destroy(fairino_msgs__msg__RobotNonrtState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fairino_msgs__msg__RobotNonrtState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fairino_msgs__msg__RobotNonrtState__Sequence__init(fairino_msgs__msg__RobotNonrtState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__msg__RobotNonrtState * data = NULL;

  if (size) {
    data = (fairino_msgs__msg__RobotNonrtState *)allocator.zero_allocate(size, sizeof(fairino_msgs__msg__RobotNonrtState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fairino_msgs__msg__RobotNonrtState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fairino_msgs__msg__RobotNonrtState__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
fairino_msgs__msg__RobotNonrtState__Sequence__fini(fairino_msgs__msg__RobotNonrtState__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      fairino_msgs__msg__RobotNonrtState__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

fairino_msgs__msg__RobotNonrtState__Sequence *
fairino_msgs__msg__RobotNonrtState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__msg__RobotNonrtState__Sequence * array = (fairino_msgs__msg__RobotNonrtState__Sequence *)allocator.allocate(sizeof(fairino_msgs__msg__RobotNonrtState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fairino_msgs__msg__RobotNonrtState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fairino_msgs__msg__RobotNonrtState__Sequence__destroy(fairino_msgs__msg__RobotNonrtState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fairino_msgs__msg__RobotNonrtState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fairino_msgs__msg__RobotNonrtState__Sequence__are_equal(const fairino_msgs__msg__RobotNonrtState__Sequence * lhs, const fairino_msgs__msg__RobotNonrtState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fairino_msgs__msg__RobotNonrtState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fairino_msgs__msg__RobotNonrtState__Sequence__copy(
  const fairino_msgs__msg__RobotNonrtState__Sequence * input,
  fairino_msgs__msg__RobotNonrtState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fairino_msgs__msg__RobotNonrtState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fairino_msgs__msg__RobotNonrtState * data =
      (fairino_msgs__msg__RobotNonrtState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fairino_msgs__msg__RobotNonrtState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fairino_msgs__msg__RobotNonrtState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fairino_msgs__msg__RobotNonrtState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
