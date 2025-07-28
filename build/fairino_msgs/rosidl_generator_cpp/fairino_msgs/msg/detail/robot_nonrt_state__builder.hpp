// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fairino_msgs:msg/RobotNonrtState.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__BUILDER_HPP_
#define FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "fairino_msgs/msg/detail/robot_nonrt_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace fairino_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotNonrtState_version
{
public:
  explicit Init_RobotNonrtState_version(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  ::fairino_msgs::msg::RobotNonrtState version(::fairino_msgs::msg::RobotNonrtState::_version_type arg)
  {
    msg_.version = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_timestamp
{
public:
  explicit Init_RobotNonrtState_timestamp(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_version timestamp(::fairino_msgs::msg::RobotNonrtState::_timestamp_type arg)
  {
    msg_.timestamp = std::move(arg);
    return Init_RobotNonrtState_version(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_check_sum
{
public:
  explicit Init_RobotNonrtState_check_sum(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_timestamp check_sum(::fairino_msgs::msg::RobotNonrtState::_check_sum_type arg)
  {
    msg_.check_sum = std::move(arg);
    return Init_RobotNonrtState_timestamp(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_error_code
{
public:
  explicit Init_RobotNonrtState_error_code(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_check_sum error_code(::fairino_msgs::msg::RobotNonrtState::_error_code_type arg)
  {
    msg_.error_code = std::move(arg);
    return Init_RobotNonrtState_check_sum(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_weldarcstate
{
public:
  explicit Init_RobotNonrtState_weldarcstate(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_error_code weldarcstate(::fairino_msgs::msg::RobotNonrtState::_weldarcstate_type arg)
  {
    msg_.weldarcstate = std::move(arg);
    return Init_RobotNonrtState_error_code(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_weldbreakoffstate
{
public:
  explicit Init_RobotNonrtState_weldbreakoffstate(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_weldarcstate weldbreakoffstate(::fairino_msgs::msg::RobotNonrtState::_weldbreakoffstate_type arg)
  {
    msg_.weldbreakoffstate = std::move(arg);
    return Init_RobotNonrtState_weldarcstate(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_grip_motion_done
{
public:
  explicit Init_RobotNonrtState_grip_motion_done(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_weldbreakoffstate grip_motion_done(::fairino_msgs::msg::RobotNonrtState::_grip_motion_done_type arg)
  {
    msg_.grip_motion_done = std::move(arg);
    return Init_RobotNonrtState_weldbreakoffstate(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_robot_motion_done
{
public:
  explicit Init_RobotNonrtState_robot_motion_done(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_grip_motion_done robot_motion_done(::fairino_msgs::msg::RobotNonrtState::_robot_motion_done_type arg)
  {
    msg_.robot_motion_done = std::move(arg);
    return Init_RobotNonrtState_grip_motion_done(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_safetyboxsig
{
public:
  explicit Init_RobotNonrtState_safetyboxsig(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_robot_motion_done safetyboxsig(::fairino_msgs::msg::RobotNonrtState::_safetyboxsig_type arg)
  {
    msg_.safetyboxsig = std::move(arg);
    return Init_RobotNonrtState_robot_motion_done(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_emg
{
public:
  explicit Init_RobotNonrtState_emg(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_safetyboxsig emg(::fairino_msgs::msg::RobotNonrtState::_emg_type arg)
  {
    msg_.emg = std::move(arg);
    return Init_RobotNonrtState_safetyboxsig(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_tl_dgt_input_l
{
public:
  explicit Init_RobotNonrtState_tl_dgt_input_l(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_emg tl_dgt_input_l(::fairino_msgs::msg::RobotNonrtState::_tl_dgt_input_l_type arg)
  {
    msg_.tl_dgt_input_l = std::move(arg);
    return Init_RobotNonrtState_emg(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_tl_dgt_output_l
{
public:
  explicit Init_RobotNonrtState_tl_dgt_output_l(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_tl_dgt_input_l tl_dgt_output_l(::fairino_msgs::msg::RobotNonrtState::_tl_dgt_output_l_type arg)
  {
    msg_.tl_dgt_output_l = std::move(arg);
    return Init_RobotNonrtState_tl_dgt_input_l(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_dgt_input_l
{
public:
  explicit Init_RobotNonrtState_dgt_input_l(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_tl_dgt_output_l dgt_input_l(::fairino_msgs::msg::RobotNonrtState::_dgt_input_l_type arg)
  {
    msg_.dgt_input_l = std::move(arg);
    return Init_RobotNonrtState_tl_dgt_output_l(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_dgt_input_h
{
public:
  explicit Init_RobotNonrtState_dgt_input_h(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_dgt_input_l dgt_input_h(::fairino_msgs::msg::RobotNonrtState::_dgt_input_h_type arg)
  {
    msg_.dgt_input_h = std::move(arg);
    return Init_RobotNonrtState_dgt_input_l(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_dgt_output_l
{
public:
  explicit Init_RobotNonrtState_dgt_output_l(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_dgt_input_h dgt_output_l(::fairino_msgs::msg::RobotNonrtState::_dgt_output_l_type arg)
  {
    msg_.dgt_output_l = std::move(arg);
    return Init_RobotNonrtState_dgt_input_h(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_dgt_output_h
{
public:
  explicit Init_RobotNonrtState_dgt_output_h(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_dgt_output_l dgt_output_h(::fairino_msgs::msg::RobotNonrtState::_dgt_output_h_type arg)
  {
    msg_.dgt_output_h = std::move(arg);
    return Init_RobotNonrtState_dgt_output_l(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_prg_cur_line
{
public:
  explicit Init_RobotNonrtState_prg_cur_line(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_dgt_output_h prg_cur_line(::fairino_msgs::msg::RobotNonrtState::_prg_cur_line_type arg)
  {
    msg_.prg_cur_line = std::move(arg);
    return Init_RobotNonrtState_dgt_output_h(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_prg_total_line
{
public:
  explicit Init_RobotNonrtState_prg_total_line(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_prg_cur_line prg_total_line(::fairino_msgs::msg::RobotNonrtState::_prg_total_line_type arg)
  {
    msg_.prg_total_line = std::move(arg);
    return Init_RobotNonrtState_prg_cur_line(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_prg_name
{
public:
  explicit Init_RobotNonrtState_prg_name(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_prg_total_line prg_name(::fairino_msgs::msg::RobotNonrtState::_prg_name_type arg)
  {
    msg_.prg_name = std::move(arg);
    return Init_RobotNonrtState_prg_total_line(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_abnormal_stop
{
public:
  explicit Init_RobotNonrtState_abnormal_stop(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_prg_name abnormal_stop(::fairino_msgs::msg::RobotNonrtState::_abnormal_stop_type arg)
  {
    msg_.abnormal_stop = std::move(arg);
    return Init_RobotNonrtState_prg_name(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_prg_state
{
public:
  explicit Init_RobotNonrtState_prg_state(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_abnormal_stop prg_state(::fairino_msgs::msg::RobotNonrtState::_prg_state_type arg)
  {
    msg_.prg_state = std::move(arg);
    return Init_RobotNonrtState_abnormal_stop(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_work_num
{
public:
  explicit Init_RobotNonrtState_work_num(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_prg_state work_num(::fairino_msgs::msg::RobotNonrtState::_work_num_type arg)
  {
    msg_.work_num = std::move(arg);
    return Init_RobotNonrtState_prg_state(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_tool_num
{
public:
  explicit Init_RobotNonrtState_tool_num(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_work_num tool_num(::fairino_msgs::msg::RobotNonrtState::_tool_num_type arg)
  {
    msg_.tool_num = std::move(arg);
    return Init_RobotNonrtState_work_num(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_robot_mode
{
public:
  explicit Init_RobotNonrtState_robot_mode(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_tool_num robot_mode(::fairino_msgs::msg::RobotNonrtState::_robot_mode_type arg)
  {
    msg_.robot_mode = std::move(arg);
    return Init_RobotNonrtState_tool_num(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_actstatus
{
public:
  explicit Init_RobotNonrtState_ft_actstatus(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_robot_mode ft_actstatus(::fairino_msgs::msg::RobotNonrtState::_ft_actstatus_type arg)
  {
    msg_.ft_actstatus = std::move(arg);
    return Init_RobotNonrtState_robot_mode(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_tz_data
{
public:
  explicit Init_RobotNonrtState_ft_tz_data(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_actstatus ft_tz_data(::fairino_msgs::msg::RobotNonrtState::_ft_tz_data_type arg)
  {
    msg_.ft_tz_data = std::move(arg);
    return Init_RobotNonrtState_ft_actstatus(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_ty_data
{
public:
  explicit Init_RobotNonrtState_ft_ty_data(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_tz_data ft_ty_data(::fairino_msgs::msg::RobotNonrtState::_ft_ty_data_type arg)
  {
    msg_.ft_ty_data = std::move(arg);
    return Init_RobotNonrtState_ft_tz_data(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_tx_data
{
public:
  explicit Init_RobotNonrtState_ft_tx_data(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_ty_data ft_tx_data(::fairino_msgs::msg::RobotNonrtState::_ft_tx_data_type arg)
  {
    msg_.ft_tx_data = std::move(arg);
    return Init_RobotNonrtState_ft_ty_data(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_fz_data
{
public:
  explicit Init_RobotNonrtState_ft_fz_data(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_tx_data ft_fz_data(::fairino_msgs::msg::RobotNonrtState::_ft_fz_data_type arg)
  {
    msg_.ft_fz_data = std::move(arg);
    return Init_RobotNonrtState_ft_tx_data(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_fy_data
{
public:
  explicit Init_RobotNonrtState_ft_fy_data(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_fz_data ft_fy_data(::fairino_msgs::msg::RobotNonrtState::_ft_fy_data_type arg)
  {
    msg_.ft_fy_data = std::move(arg);
    return Init_RobotNonrtState_ft_fz_data(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_ft_fx_data
{
public:
  explicit Init_RobotNonrtState_ft_fx_data(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_fy_data ft_fx_data(::fairino_msgs::msg::RobotNonrtState::_ft_fx_data_type arg)
  {
    msg_.ft_fx_data = std::move(arg);
    return Init_RobotNonrtState_ft_fy_data(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_exaxispos4
{
public:
  explicit Init_RobotNonrtState_exaxispos4(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_ft_fx_data exaxispos4(::fairino_msgs::msg::RobotNonrtState::_exaxispos4_type arg)
  {
    msg_.exaxispos4 = std::move(arg);
    return Init_RobotNonrtState_ft_fx_data(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_exaxispos3
{
public:
  explicit Init_RobotNonrtState_exaxispos3(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_exaxispos4 exaxispos3(::fairino_msgs::msg::RobotNonrtState::_exaxispos3_type arg)
  {
    msg_.exaxispos3 = std::move(arg);
    return Init_RobotNonrtState_exaxispos4(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_exaxispos2
{
public:
  explicit Init_RobotNonrtState_exaxispos2(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_exaxispos3 exaxispos2(::fairino_msgs::msg::RobotNonrtState::_exaxispos2_type arg)
  {
    msg_.exaxispos2 = std::move(arg);
    return Init_RobotNonrtState_exaxispos3(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_exaxispos1
{
public:
  explicit Init_RobotNonrtState_exaxispos1(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_exaxispos2 exaxispos1(::fairino_msgs::msg::RobotNonrtState::_exaxispos1_type arg)
  {
    msg_.exaxispos1 = std::move(arg);
    return Init_RobotNonrtState_exaxispos2(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_flange_c_cur_pos
{
public:
  explicit Init_RobotNonrtState_flange_c_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_exaxispos1 flange_c_cur_pos(::fairino_msgs::msg::RobotNonrtState::_flange_c_cur_pos_type arg)
  {
    msg_.flange_c_cur_pos = std::move(arg);
    return Init_RobotNonrtState_exaxispos1(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_flange_b_cur_pos
{
public:
  explicit Init_RobotNonrtState_flange_b_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_flange_c_cur_pos flange_b_cur_pos(::fairino_msgs::msg::RobotNonrtState::_flange_b_cur_pos_type arg)
  {
    msg_.flange_b_cur_pos = std::move(arg);
    return Init_RobotNonrtState_flange_c_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_flange_a_cur_pos
{
public:
  explicit Init_RobotNonrtState_flange_a_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_flange_b_cur_pos flange_a_cur_pos(::fairino_msgs::msg::RobotNonrtState::_flange_a_cur_pos_type arg)
  {
    msg_.flange_a_cur_pos = std::move(arg);
    return Init_RobotNonrtState_flange_b_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_flange_z_cur_pos
{
public:
  explicit Init_RobotNonrtState_flange_z_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_flange_a_cur_pos flange_z_cur_pos(::fairino_msgs::msg::RobotNonrtState::_flange_z_cur_pos_type arg)
  {
    msg_.flange_z_cur_pos = std::move(arg);
    return Init_RobotNonrtState_flange_a_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_flange_y_cur_pos
{
public:
  explicit Init_RobotNonrtState_flange_y_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_flange_z_cur_pos flange_y_cur_pos(::fairino_msgs::msg::RobotNonrtState::_flange_y_cur_pos_type arg)
  {
    msg_.flange_y_cur_pos = std::move(arg);
    return Init_RobotNonrtState_flange_z_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_flange_x_cur_pos
{
public:
  explicit Init_RobotNonrtState_flange_x_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_flange_y_cur_pos flange_x_cur_pos(::fairino_msgs::msg::RobotNonrtState::_flange_x_cur_pos_type arg)
  {
    msg_.flange_x_cur_pos = std::move(arg);
    return Init_RobotNonrtState_flange_y_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_cart_c_cur_pos
{
public:
  explicit Init_RobotNonrtState_cart_c_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_flange_x_cur_pos cart_c_cur_pos(::fairino_msgs::msg::RobotNonrtState::_cart_c_cur_pos_type arg)
  {
    msg_.cart_c_cur_pos = std::move(arg);
    return Init_RobotNonrtState_flange_x_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_cart_b_cur_pos
{
public:
  explicit Init_RobotNonrtState_cart_b_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_cart_c_cur_pos cart_b_cur_pos(::fairino_msgs::msg::RobotNonrtState::_cart_b_cur_pos_type arg)
  {
    msg_.cart_b_cur_pos = std::move(arg);
    return Init_RobotNonrtState_cart_c_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_cart_a_cur_pos
{
public:
  explicit Init_RobotNonrtState_cart_a_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_cart_b_cur_pos cart_a_cur_pos(::fairino_msgs::msg::RobotNonrtState::_cart_a_cur_pos_type arg)
  {
    msg_.cart_a_cur_pos = std::move(arg);
    return Init_RobotNonrtState_cart_b_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_cart_z_cur_pos
{
public:
  explicit Init_RobotNonrtState_cart_z_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_cart_a_cur_pos cart_z_cur_pos(::fairino_msgs::msg::RobotNonrtState::_cart_z_cur_pos_type arg)
  {
    msg_.cart_z_cur_pos = std::move(arg);
    return Init_RobotNonrtState_cart_a_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_cart_y_cur_pos
{
public:
  explicit Init_RobotNonrtState_cart_y_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_cart_z_cur_pos cart_y_cur_pos(::fairino_msgs::msg::RobotNonrtState::_cart_y_cur_pos_type arg)
  {
    msg_.cart_y_cur_pos = std::move(arg);
    return Init_RobotNonrtState_cart_z_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_cart_x_cur_pos
{
public:
  explicit Init_RobotNonrtState_cart_x_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_cart_y_cur_pos cart_x_cur_pos(::fairino_msgs::msg::RobotNonrtState::_cart_x_cur_pos_type arg)
  {
    msg_.cart_x_cur_pos = std::move(arg);
    return Init_RobotNonrtState_cart_y_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j6_cur_tor
{
public:
  explicit Init_RobotNonrtState_j6_cur_tor(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_cart_x_cur_pos j6_cur_tor(::fairino_msgs::msg::RobotNonrtState::_j6_cur_tor_type arg)
  {
    msg_.j6_cur_tor = std::move(arg);
    return Init_RobotNonrtState_cart_x_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j5_cur_tor
{
public:
  explicit Init_RobotNonrtState_j5_cur_tor(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j6_cur_tor j5_cur_tor(::fairino_msgs::msg::RobotNonrtState::_j5_cur_tor_type arg)
  {
    msg_.j5_cur_tor = std::move(arg);
    return Init_RobotNonrtState_j6_cur_tor(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j4_cur_tor
{
public:
  explicit Init_RobotNonrtState_j4_cur_tor(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j5_cur_tor j4_cur_tor(::fairino_msgs::msg::RobotNonrtState::_j4_cur_tor_type arg)
  {
    msg_.j4_cur_tor = std::move(arg);
    return Init_RobotNonrtState_j5_cur_tor(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j3_cur_tor
{
public:
  explicit Init_RobotNonrtState_j3_cur_tor(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j4_cur_tor j3_cur_tor(::fairino_msgs::msg::RobotNonrtState::_j3_cur_tor_type arg)
  {
    msg_.j3_cur_tor = std::move(arg);
    return Init_RobotNonrtState_j4_cur_tor(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j2_cur_tor
{
public:
  explicit Init_RobotNonrtState_j2_cur_tor(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j3_cur_tor j2_cur_tor(::fairino_msgs::msg::RobotNonrtState::_j2_cur_tor_type arg)
  {
    msg_.j2_cur_tor = std::move(arg);
    return Init_RobotNonrtState_j3_cur_tor(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j1_cur_tor
{
public:
  explicit Init_RobotNonrtState_j1_cur_tor(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j2_cur_tor j1_cur_tor(::fairino_msgs::msg::RobotNonrtState::_j1_cur_tor_type arg)
  {
    msg_.j1_cur_tor = std::move(arg);
    return Init_RobotNonrtState_j2_cur_tor(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j6_cur_pos
{
public:
  explicit Init_RobotNonrtState_j6_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j1_cur_tor j6_cur_pos(::fairino_msgs::msg::RobotNonrtState::_j6_cur_pos_type arg)
  {
    msg_.j6_cur_pos = std::move(arg);
    return Init_RobotNonrtState_j1_cur_tor(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j5_cur_pos
{
public:
  explicit Init_RobotNonrtState_j5_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j6_cur_pos j5_cur_pos(::fairino_msgs::msg::RobotNonrtState::_j5_cur_pos_type arg)
  {
    msg_.j5_cur_pos = std::move(arg);
    return Init_RobotNonrtState_j6_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j4_cur_pos
{
public:
  explicit Init_RobotNonrtState_j4_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j5_cur_pos j4_cur_pos(::fairino_msgs::msg::RobotNonrtState::_j4_cur_pos_type arg)
  {
    msg_.j4_cur_pos = std::move(arg);
    return Init_RobotNonrtState_j5_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j3_cur_pos
{
public:
  explicit Init_RobotNonrtState_j3_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j4_cur_pos j3_cur_pos(::fairino_msgs::msg::RobotNonrtState::_j3_cur_pos_type arg)
  {
    msg_.j3_cur_pos = std::move(arg);
    return Init_RobotNonrtState_j4_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j2_cur_pos
{
public:
  explicit Init_RobotNonrtState_j2_cur_pos(::fairino_msgs::msg::RobotNonrtState & msg)
  : msg_(msg)
  {}
  Init_RobotNonrtState_j3_cur_pos j2_cur_pos(::fairino_msgs::msg::RobotNonrtState::_j2_cur_pos_type arg)
  {
    msg_.j2_cur_pos = std::move(arg);
    return Init_RobotNonrtState_j3_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

class Init_RobotNonrtState_j1_cur_pos
{
public:
  Init_RobotNonrtState_j1_cur_pos()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotNonrtState_j2_cur_pos j1_cur_pos(::fairino_msgs::msg::RobotNonrtState::_j1_cur_pos_type arg)
  {
    msg_.j1_cur_pos = std::move(arg);
    return Init_RobotNonrtState_j2_cur_pos(msg_);
  }

private:
  ::fairino_msgs::msg::RobotNonrtState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fairino_msgs::msg::RobotNonrtState>()
{
  return fairino_msgs::msg::builder::Init_RobotNonrtState_j1_cur_pos();
}

}  // namespace fairino_msgs

#endif  // FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__BUILDER_HPP_
