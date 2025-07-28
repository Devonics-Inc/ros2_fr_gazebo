// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fairino_msgs:msg/RobotNonrtState.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__TRAITS_HPP_
#define FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "fairino_msgs/msg/detail/robot_nonrt_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fairino_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RobotNonrtState & msg,
  std::ostream & out)
{
  out << "{";
  // member: j1_cur_pos
  {
    out << "j1_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j1_cur_pos, out);
    out << ", ";
  }

  // member: j2_cur_pos
  {
    out << "j2_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j2_cur_pos, out);
    out << ", ";
  }

  // member: j3_cur_pos
  {
    out << "j3_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j3_cur_pos, out);
    out << ", ";
  }

  // member: j4_cur_pos
  {
    out << "j4_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j4_cur_pos, out);
    out << ", ";
  }

  // member: j5_cur_pos
  {
    out << "j5_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j5_cur_pos, out);
    out << ", ";
  }

  // member: j6_cur_pos
  {
    out << "j6_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j6_cur_pos, out);
    out << ", ";
  }

  // member: j1_cur_tor
  {
    out << "j1_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j1_cur_tor, out);
    out << ", ";
  }

  // member: j2_cur_tor
  {
    out << "j2_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j2_cur_tor, out);
    out << ", ";
  }

  // member: j3_cur_tor
  {
    out << "j3_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j3_cur_tor, out);
    out << ", ";
  }

  // member: j4_cur_tor
  {
    out << "j4_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j4_cur_tor, out);
    out << ", ";
  }

  // member: j5_cur_tor
  {
    out << "j5_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j5_cur_tor, out);
    out << ", ";
  }

  // member: j6_cur_tor
  {
    out << "j6_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j6_cur_tor, out);
    out << ", ";
  }

  // member: cart_x_cur_pos
  {
    out << "cart_x_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_x_cur_pos, out);
    out << ", ";
  }

  // member: cart_y_cur_pos
  {
    out << "cart_y_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_y_cur_pos, out);
    out << ", ";
  }

  // member: cart_z_cur_pos
  {
    out << "cart_z_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_z_cur_pos, out);
    out << ", ";
  }

  // member: cart_a_cur_pos
  {
    out << "cart_a_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_a_cur_pos, out);
    out << ", ";
  }

  // member: cart_b_cur_pos
  {
    out << "cart_b_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_b_cur_pos, out);
    out << ", ";
  }

  // member: cart_c_cur_pos
  {
    out << "cart_c_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_c_cur_pos, out);
    out << ", ";
  }

  // member: flange_x_cur_pos
  {
    out << "flange_x_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_x_cur_pos, out);
    out << ", ";
  }

  // member: flange_y_cur_pos
  {
    out << "flange_y_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_y_cur_pos, out);
    out << ", ";
  }

  // member: flange_z_cur_pos
  {
    out << "flange_z_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_z_cur_pos, out);
    out << ", ";
  }

  // member: flange_a_cur_pos
  {
    out << "flange_a_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_a_cur_pos, out);
    out << ", ";
  }

  // member: flange_b_cur_pos
  {
    out << "flange_b_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_b_cur_pos, out);
    out << ", ";
  }

  // member: flange_c_cur_pos
  {
    out << "flange_c_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_c_cur_pos, out);
    out << ", ";
  }

  // member: exaxispos1
  {
    out << "exaxispos1: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos1, out);
    out << ", ";
  }

  // member: exaxispos2
  {
    out << "exaxispos2: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos2, out);
    out << ", ";
  }

  // member: exaxispos3
  {
    out << "exaxispos3: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos3, out);
    out << ", ";
  }

  // member: exaxispos4
  {
    out << "exaxispos4: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos4, out);
    out << ", ";
  }

  // member: ft_fx_data
  {
    out << "ft_fx_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_fx_data, out);
    out << ", ";
  }

  // member: ft_fy_data
  {
    out << "ft_fy_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_fy_data, out);
    out << ", ";
  }

  // member: ft_fz_data
  {
    out << "ft_fz_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_fz_data, out);
    out << ", ";
  }

  // member: ft_tx_data
  {
    out << "ft_tx_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_tx_data, out);
    out << ", ";
  }

  // member: ft_ty_data
  {
    out << "ft_ty_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_ty_data, out);
    out << ", ";
  }

  // member: ft_tz_data
  {
    out << "ft_tz_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_tz_data, out);
    out << ", ";
  }

  // member: ft_actstatus
  {
    out << "ft_actstatus: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_actstatus, out);
    out << ", ";
  }

  // member: robot_mode
  {
    out << "robot_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_mode, out);
    out << ", ";
  }

  // member: tool_num
  {
    out << "tool_num: ";
    rosidl_generator_traits::value_to_yaml(msg.tool_num, out);
    out << ", ";
  }

  // member: work_num
  {
    out << "work_num: ";
    rosidl_generator_traits::value_to_yaml(msg.work_num, out);
    out << ", ";
  }

  // member: prg_state
  {
    out << "prg_state: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_state, out);
    out << ", ";
  }

  // member: abnormal_stop
  {
    out << "abnormal_stop: ";
    rosidl_generator_traits::value_to_yaml(msg.abnormal_stop, out);
    out << ", ";
  }

  // member: prg_name
  {
    out << "prg_name: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_name, out);
    out << ", ";
  }

  // member: prg_total_line
  {
    out << "prg_total_line: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_total_line, out);
    out << ", ";
  }

  // member: prg_cur_line
  {
    out << "prg_cur_line: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_cur_line, out);
    out << ", ";
  }

  // member: dgt_output_h
  {
    out << "dgt_output_h: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_output_h, out);
    out << ", ";
  }

  // member: dgt_output_l
  {
    out << "dgt_output_l: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_output_l, out);
    out << ", ";
  }

  // member: dgt_input_h
  {
    out << "dgt_input_h: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_input_h, out);
    out << ", ";
  }

  // member: dgt_input_l
  {
    out << "dgt_input_l: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_input_l, out);
    out << ", ";
  }

  // member: tl_dgt_output_l
  {
    out << "tl_dgt_output_l: ";
    rosidl_generator_traits::value_to_yaml(msg.tl_dgt_output_l, out);
    out << ", ";
  }

  // member: tl_dgt_input_l
  {
    out << "tl_dgt_input_l: ";
    rosidl_generator_traits::value_to_yaml(msg.tl_dgt_input_l, out);
    out << ", ";
  }

  // member: emg
  {
    out << "emg: ";
    rosidl_generator_traits::value_to_yaml(msg.emg, out);
    out << ", ";
  }

  // member: safetyboxsig
  {
    if (msg.safetyboxsig.size() == 0) {
      out << "safetyboxsig: []";
    } else {
      out << "safetyboxsig: [";
      size_t pending_items = msg.safetyboxsig.size();
      for (auto item : msg.safetyboxsig) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: robot_motion_done
  {
    out << "robot_motion_done: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_motion_done, out);
    out << ", ";
  }

  // member: grip_motion_done
  {
    out << "grip_motion_done: ";
    rosidl_generator_traits::value_to_yaml(msg.grip_motion_done, out);
    out << ", ";
  }

  // member: weldbreakoffstate
  {
    out << "weldbreakoffstate: ";
    rosidl_generator_traits::value_to_yaml(msg.weldbreakoffstate, out);
    out << ", ";
  }

  // member: weldarcstate
  {
    out << "weldarcstate: ";
    rosidl_generator_traits::value_to_yaml(msg.weldarcstate, out);
    out << ", ";
  }

  // member: error_code
  {
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << ", ";
  }

  // member: check_sum
  {
    out << "check_sum: ";
    rosidl_generator_traits::value_to_yaml(msg.check_sum, out);
    out << ", ";
  }

  // member: timestamp
  {
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: version
  {
    out << "version: ";
    rosidl_generator_traits::value_to_yaml(msg.version, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RobotNonrtState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: j1_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j1_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j1_cur_pos, out);
    out << "\n";
  }

  // member: j2_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j2_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j2_cur_pos, out);
    out << "\n";
  }

  // member: j3_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j3_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j3_cur_pos, out);
    out << "\n";
  }

  // member: j4_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j4_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j4_cur_pos, out);
    out << "\n";
  }

  // member: j5_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j5_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j5_cur_pos, out);
    out << "\n";
  }

  // member: j6_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j6_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.j6_cur_pos, out);
    out << "\n";
  }

  // member: j1_cur_tor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j1_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j1_cur_tor, out);
    out << "\n";
  }

  // member: j2_cur_tor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j2_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j2_cur_tor, out);
    out << "\n";
  }

  // member: j3_cur_tor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j3_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j3_cur_tor, out);
    out << "\n";
  }

  // member: j4_cur_tor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j4_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j4_cur_tor, out);
    out << "\n";
  }

  // member: j5_cur_tor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j5_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j5_cur_tor, out);
    out << "\n";
  }

  // member: j6_cur_tor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "j6_cur_tor: ";
    rosidl_generator_traits::value_to_yaml(msg.j6_cur_tor, out);
    out << "\n";
  }

  // member: cart_x_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cart_x_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_x_cur_pos, out);
    out << "\n";
  }

  // member: cart_y_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cart_y_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_y_cur_pos, out);
    out << "\n";
  }

  // member: cart_z_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cart_z_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_z_cur_pos, out);
    out << "\n";
  }

  // member: cart_a_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cart_a_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_a_cur_pos, out);
    out << "\n";
  }

  // member: cart_b_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cart_b_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_b_cur_pos, out);
    out << "\n";
  }

  // member: cart_c_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cart_c_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.cart_c_cur_pos, out);
    out << "\n";
  }

  // member: flange_x_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flange_x_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_x_cur_pos, out);
    out << "\n";
  }

  // member: flange_y_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flange_y_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_y_cur_pos, out);
    out << "\n";
  }

  // member: flange_z_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flange_z_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_z_cur_pos, out);
    out << "\n";
  }

  // member: flange_a_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flange_a_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_a_cur_pos, out);
    out << "\n";
  }

  // member: flange_b_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flange_b_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_b_cur_pos, out);
    out << "\n";
  }

  // member: flange_c_cur_pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "flange_c_cur_pos: ";
    rosidl_generator_traits::value_to_yaml(msg.flange_c_cur_pos, out);
    out << "\n";
  }

  // member: exaxispos1
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exaxispos1: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos1, out);
    out << "\n";
  }

  // member: exaxispos2
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exaxispos2: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos2, out);
    out << "\n";
  }

  // member: exaxispos3
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exaxispos3: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos3, out);
    out << "\n";
  }

  // member: exaxispos4
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "exaxispos4: ";
    rosidl_generator_traits::value_to_yaml(msg.exaxispos4, out);
    out << "\n";
  }

  // member: ft_fx_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_fx_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_fx_data, out);
    out << "\n";
  }

  // member: ft_fy_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_fy_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_fy_data, out);
    out << "\n";
  }

  // member: ft_fz_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_fz_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_fz_data, out);
    out << "\n";
  }

  // member: ft_tx_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_tx_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_tx_data, out);
    out << "\n";
  }

  // member: ft_ty_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_ty_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_ty_data, out);
    out << "\n";
  }

  // member: ft_tz_data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_tz_data: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_tz_data, out);
    out << "\n";
  }

  // member: ft_actstatus
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "ft_actstatus: ";
    rosidl_generator_traits::value_to_yaml(msg.ft_actstatus, out);
    out << "\n";
  }

  // member: robot_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_mode, out);
    out << "\n";
  }

  // member: tool_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tool_num: ";
    rosidl_generator_traits::value_to_yaml(msg.tool_num, out);
    out << "\n";
  }

  // member: work_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "work_num: ";
    rosidl_generator_traits::value_to_yaml(msg.work_num, out);
    out << "\n";
  }

  // member: prg_state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "prg_state: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_state, out);
    out << "\n";
  }

  // member: abnormal_stop
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "abnormal_stop: ";
    rosidl_generator_traits::value_to_yaml(msg.abnormal_stop, out);
    out << "\n";
  }

  // member: prg_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "prg_name: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_name, out);
    out << "\n";
  }

  // member: prg_total_line
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "prg_total_line: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_total_line, out);
    out << "\n";
  }

  // member: prg_cur_line
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "prg_cur_line: ";
    rosidl_generator_traits::value_to_yaml(msg.prg_cur_line, out);
    out << "\n";
  }

  // member: dgt_output_h
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dgt_output_h: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_output_h, out);
    out << "\n";
  }

  // member: dgt_output_l
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dgt_output_l: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_output_l, out);
    out << "\n";
  }

  // member: dgt_input_h
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dgt_input_h: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_input_h, out);
    out << "\n";
  }

  // member: dgt_input_l
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dgt_input_l: ";
    rosidl_generator_traits::value_to_yaml(msg.dgt_input_l, out);
    out << "\n";
  }

  // member: tl_dgt_output_l
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tl_dgt_output_l: ";
    rosidl_generator_traits::value_to_yaml(msg.tl_dgt_output_l, out);
    out << "\n";
  }

  // member: tl_dgt_input_l
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tl_dgt_input_l: ";
    rosidl_generator_traits::value_to_yaml(msg.tl_dgt_input_l, out);
    out << "\n";
  }

  // member: emg
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "emg: ";
    rosidl_generator_traits::value_to_yaml(msg.emg, out);
    out << "\n";
  }

  // member: safetyboxsig
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.safetyboxsig.size() == 0) {
      out << "safetyboxsig: []\n";
    } else {
      out << "safetyboxsig:\n";
      for (auto item : msg.safetyboxsig) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: robot_motion_done
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_motion_done: ";
    rosidl_generator_traits::value_to_yaml(msg.robot_motion_done, out);
    out << "\n";
  }

  // member: grip_motion_done
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "grip_motion_done: ";
    rosidl_generator_traits::value_to_yaml(msg.grip_motion_done, out);
    out << "\n";
  }

  // member: weldbreakoffstate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "weldbreakoffstate: ";
    rosidl_generator_traits::value_to_yaml(msg.weldbreakoffstate, out);
    out << "\n";
  }

  // member: weldarcstate
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "weldarcstate: ";
    rosidl_generator_traits::value_to_yaml(msg.weldarcstate, out);
    out << "\n";
  }

  // member: error_code
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << "\n";
  }

  // member: check_sum
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "check_sum: ";
    rosidl_generator_traits::value_to_yaml(msg.check_sum, out);
    out << "\n";
  }

  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp: ";
    rosidl_generator_traits::value_to_yaml(msg.timestamp, out);
    out << "\n";
  }

  // member: version
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "version: ";
    rosidl_generator_traits::value_to_yaml(msg.version, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RobotNonrtState & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace fairino_msgs

namespace rosidl_generator_traits
{

[[deprecated("use fairino_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const fairino_msgs::msg::RobotNonrtState & msg,
  std::ostream & out, size_t indentation = 0)
{
  fairino_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use fairino_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const fairino_msgs::msg::RobotNonrtState & msg)
{
  return fairino_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<fairino_msgs::msg::RobotNonrtState>()
{
  return "fairino_msgs::msg::RobotNonrtState";
}

template<>
inline const char * name<fairino_msgs::msg::RobotNonrtState>()
{
  return "fairino_msgs/msg/RobotNonrtState";
}

template<>
struct has_fixed_size<fairino_msgs::msg::RobotNonrtState>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fairino_msgs::msg::RobotNonrtState>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fairino_msgs::msg::RobotNonrtState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__TRAITS_HPP_
