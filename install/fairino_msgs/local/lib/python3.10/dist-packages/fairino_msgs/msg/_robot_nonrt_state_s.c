// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from fairino_msgs:msg/RobotNonrtState.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "fairino_msgs/msg/detail/robot_nonrt_state__struct.h"
#include "fairino_msgs/msg/detail/robot_nonrt_state__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool fairino_msgs__msg__robot_nonrt_state__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[52];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("fairino_msgs.msg._robot_nonrt_state.RobotNonrtState", full_classname_dest, 51) == 0);
  }
  fairino_msgs__msg__RobotNonrtState * ros_message = _ros_message;
  {  // j1_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "j1_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j1_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j2_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "j2_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j2_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j3_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "j3_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j3_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j4_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "j4_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j4_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j5_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "j5_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j5_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j6_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "j6_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j6_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j1_cur_tor
    PyObject * field = PyObject_GetAttrString(_pymsg, "j1_cur_tor");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j1_cur_tor = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j2_cur_tor
    PyObject * field = PyObject_GetAttrString(_pymsg, "j2_cur_tor");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j2_cur_tor = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j3_cur_tor
    PyObject * field = PyObject_GetAttrString(_pymsg, "j3_cur_tor");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j3_cur_tor = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j4_cur_tor
    PyObject * field = PyObject_GetAttrString(_pymsg, "j4_cur_tor");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j4_cur_tor = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j5_cur_tor
    PyObject * field = PyObject_GetAttrString(_pymsg, "j5_cur_tor");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j5_cur_tor = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // j6_cur_tor
    PyObject * field = PyObject_GetAttrString(_pymsg, "j6_cur_tor");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->j6_cur_tor = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cart_x_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "cart_x_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cart_x_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cart_y_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "cart_y_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cart_y_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cart_z_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "cart_z_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cart_z_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cart_a_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "cart_a_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cart_a_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cart_b_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "cart_b_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cart_b_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cart_c_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "cart_c_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->cart_c_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flange_x_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flange_x_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->flange_x_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flange_y_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flange_y_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->flange_y_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flange_z_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flange_z_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->flange_z_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flange_a_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flange_a_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->flange_a_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flange_b_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flange_b_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->flange_b_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // flange_c_cur_pos
    PyObject * field = PyObject_GetAttrString(_pymsg, "flange_c_cur_pos");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->flange_c_cur_pos = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // exaxispos1
    PyObject * field = PyObject_GetAttrString(_pymsg, "exaxispos1");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->exaxispos1 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // exaxispos2
    PyObject * field = PyObject_GetAttrString(_pymsg, "exaxispos2");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->exaxispos2 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // exaxispos3
    PyObject * field = PyObject_GetAttrString(_pymsg, "exaxispos3");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->exaxispos3 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // exaxispos4
    PyObject * field = PyObject_GetAttrString(_pymsg, "exaxispos4");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->exaxispos4 = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_fx_data
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_fx_data");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ft_fx_data = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_fy_data
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_fy_data");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ft_fy_data = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_fz_data
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_fz_data");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ft_fz_data = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_tx_data
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_tx_data");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ft_tx_data = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_ty_data
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_ty_data");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ft_ty_data = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_tz_data
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_tz_data");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->ft_tz_data = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // ft_actstatus
    PyObject * field = PyObject_GetAttrString(_pymsg, "ft_actstatus");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->ft_actstatus = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // robot_mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot_mode");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->robot_mode = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tool_num
    PyObject * field = PyObject_GetAttrString(_pymsg, "tool_num");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tool_num = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // work_num
    PyObject * field = PyObject_GetAttrString(_pymsg, "work_num");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->work_num = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // prg_state
    PyObject * field = PyObject_GetAttrString(_pymsg, "prg_state");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->prg_state = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // abnormal_stop
    PyObject * field = PyObject_GetAttrString(_pymsg, "abnormal_stop");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->abnormal_stop = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // prg_name
    PyObject * field = PyObject_GetAttrString(_pymsg, "prg_name");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->prg_name, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // prg_total_line
    PyObject * field = PyObject_GetAttrString(_pymsg, "prg_total_line");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->prg_total_line = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // prg_cur_line
    PyObject * field = PyObject_GetAttrString(_pymsg, "prg_cur_line");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->prg_cur_line = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // dgt_output_h
    PyObject * field = PyObject_GetAttrString(_pymsg, "dgt_output_h");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->dgt_output_h = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // dgt_output_l
    PyObject * field = PyObject_GetAttrString(_pymsg, "dgt_output_l");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->dgt_output_l = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // dgt_input_h
    PyObject * field = PyObject_GetAttrString(_pymsg, "dgt_input_h");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->dgt_input_h = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // dgt_input_l
    PyObject * field = PyObject_GetAttrString(_pymsg, "dgt_input_l");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->dgt_input_l = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tl_dgt_output_l
    PyObject * field = PyObject_GetAttrString(_pymsg, "tl_dgt_output_l");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tl_dgt_output_l = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tl_dgt_input_l
    PyObject * field = PyObject_GetAttrString(_pymsg, "tl_dgt_input_l");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tl_dgt_input_l = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // emg
    PyObject * field = PyObject_GetAttrString(_pymsg, "emg");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->emg = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // safetyboxsig
    PyObject * field = PyObject_GetAttrString(_pymsg, "safetyboxsig");
    if (!field) {
      return false;
    }
    {
      // TODO(dirk-thomas) use a better way to check the type before casting
      assert(field->ob_type != NULL);
      assert(field->ob_type->tp_name != NULL);
      assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
      PyArrayObject * seq_field = (PyArrayObject *)field;
      Py_INCREF(seq_field);
      assert(PyArray_NDIM(seq_field) == 1);
      assert(PyArray_TYPE(seq_field) == NPY_UINT8);
      Py_ssize_t size = 6;
      uint8_t * dest = ros_message->safetyboxsig;
      for (Py_ssize_t i = 0; i < size; ++i) {
        uint8_t tmp = *(npy_uint8 *)PyArray_GETPTR1(seq_field, i);
        memcpy(&dest[i], &tmp, sizeof(uint8_t));
      }
      Py_DECREF(seq_field);
    }
    Py_DECREF(field);
  }
  {  // robot_motion_done
    PyObject * field = PyObject_GetAttrString(_pymsg, "robot_motion_done");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->robot_motion_done = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // grip_motion_done
    PyObject * field = PyObject_GetAttrString(_pymsg, "grip_motion_done");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->grip_motion_done = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // weldbreakoffstate
    PyObject * field = PyObject_GetAttrString(_pymsg, "weldbreakoffstate");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->weldbreakoffstate = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // weldarcstate
    PyObject * field = PyObject_GetAttrString(_pymsg, "weldarcstate");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->weldarcstate = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // error_code
    PyObject * field = PyObject_GetAttrString(_pymsg, "error_code");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->error_code = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // check_sum
    PyObject * field = PyObject_GetAttrString(_pymsg, "check_sum");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->check_sum = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // timestamp
    PyObject * field = PyObject_GetAttrString(_pymsg, "timestamp");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->timestamp = PyLong_AsUnsignedLongLong(field);
    Py_DECREF(field);
  }
  {  // version
    PyObject * field = PyObject_GetAttrString(_pymsg, "version");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->version, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * fairino_msgs__msg__robot_nonrt_state__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of RobotNonrtState */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("fairino_msgs.msg._robot_nonrt_state");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "RobotNonrtState");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  fairino_msgs__msg__RobotNonrtState * ros_message = (fairino_msgs__msg__RobotNonrtState *)raw_ros_message;
  {  // j1_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j1_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j1_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j2_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j2_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j2_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j3_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j3_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j3_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j4_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j4_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j4_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j5_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j5_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j5_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j6_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j6_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j6_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j1_cur_tor
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j1_cur_tor);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j1_cur_tor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j2_cur_tor
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j2_cur_tor);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j2_cur_tor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j3_cur_tor
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j3_cur_tor);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j3_cur_tor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j4_cur_tor
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j4_cur_tor);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j4_cur_tor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j5_cur_tor
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j5_cur_tor);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j5_cur_tor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // j6_cur_tor
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->j6_cur_tor);
    {
      int rc = PyObject_SetAttrString(_pymessage, "j6_cur_tor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cart_x_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cart_x_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cart_x_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cart_y_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cart_y_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cart_y_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cart_z_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cart_z_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cart_z_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cart_a_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cart_a_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cart_a_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cart_b_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cart_b_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cart_b_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cart_c_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->cart_c_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cart_c_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flange_x_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->flange_x_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flange_x_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flange_y_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->flange_y_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flange_y_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flange_z_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->flange_z_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flange_z_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flange_a_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->flange_a_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flange_a_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flange_b_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->flange_b_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flange_b_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // flange_c_cur_pos
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->flange_c_cur_pos);
    {
      int rc = PyObject_SetAttrString(_pymessage, "flange_c_cur_pos", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // exaxispos1
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->exaxispos1);
    {
      int rc = PyObject_SetAttrString(_pymessage, "exaxispos1", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // exaxispos2
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->exaxispos2);
    {
      int rc = PyObject_SetAttrString(_pymessage, "exaxispos2", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // exaxispos3
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->exaxispos3);
    {
      int rc = PyObject_SetAttrString(_pymessage, "exaxispos3", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // exaxispos4
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->exaxispos4);
    {
      int rc = PyObject_SetAttrString(_pymessage, "exaxispos4", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_fx_data
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ft_fx_data);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_fx_data", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_fy_data
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ft_fy_data);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_fy_data", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_fz_data
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ft_fz_data);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_fz_data", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_tx_data
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ft_tx_data);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_tx_data", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_ty_data
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ft_ty_data);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_ty_data", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_tz_data
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->ft_tz_data);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_tz_data", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // ft_actstatus
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->ft_actstatus);
    {
      int rc = PyObject_SetAttrString(_pymessage, "ft_actstatus", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // robot_mode
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->robot_mode);
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot_mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tool_num
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tool_num);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tool_num", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // work_num
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->work_num);
    {
      int rc = PyObject_SetAttrString(_pymessage, "work_num", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // prg_state
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->prg_state);
    {
      int rc = PyObject_SetAttrString(_pymessage, "prg_state", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // abnormal_stop
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->abnormal_stop);
    {
      int rc = PyObject_SetAttrString(_pymessage, "abnormal_stop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // prg_name
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->prg_name.data,
      strlen(ros_message->prg_name.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "prg_name", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // prg_total_line
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->prg_total_line);
    {
      int rc = PyObject_SetAttrString(_pymessage, "prg_total_line", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // prg_cur_line
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->prg_cur_line);
    {
      int rc = PyObject_SetAttrString(_pymessage, "prg_cur_line", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dgt_output_h
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->dgt_output_h);
    {
      int rc = PyObject_SetAttrString(_pymessage, "dgt_output_h", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dgt_output_l
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->dgt_output_l);
    {
      int rc = PyObject_SetAttrString(_pymessage, "dgt_output_l", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dgt_input_h
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->dgt_input_h);
    {
      int rc = PyObject_SetAttrString(_pymessage, "dgt_input_h", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // dgt_input_l
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->dgt_input_l);
    {
      int rc = PyObject_SetAttrString(_pymessage, "dgt_input_l", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tl_dgt_output_l
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tl_dgt_output_l);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tl_dgt_output_l", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tl_dgt_input_l
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tl_dgt_input_l);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tl_dgt_input_l", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // emg
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->emg);
    {
      int rc = PyObject_SetAttrString(_pymessage, "emg", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // safetyboxsig
    PyObject * field = NULL;
    field = PyObject_GetAttrString(_pymessage, "safetyboxsig");
    if (!field) {
      return NULL;
    }
    assert(field->ob_type != NULL);
    assert(field->ob_type->tp_name != NULL);
    assert(strcmp(field->ob_type->tp_name, "numpy.ndarray") == 0);
    PyArrayObject * seq_field = (PyArrayObject *)field;
    assert(PyArray_NDIM(seq_field) == 1);
    assert(PyArray_TYPE(seq_field) == NPY_UINT8);
    assert(sizeof(npy_uint8) == sizeof(uint8_t));
    npy_uint8 * dst = (npy_uint8 *)PyArray_GETPTR1(seq_field, 0);
    uint8_t * src = &(ros_message->safetyboxsig[0]);
    memcpy(dst, src, 6 * sizeof(uint8_t));
    Py_DECREF(field);
  }
  {  // robot_motion_done
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->robot_motion_done);
    {
      int rc = PyObject_SetAttrString(_pymessage, "robot_motion_done", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // grip_motion_done
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->grip_motion_done);
    {
      int rc = PyObject_SetAttrString(_pymessage, "grip_motion_done", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // weldbreakoffstate
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->weldbreakoffstate);
    {
      int rc = PyObject_SetAttrString(_pymessage, "weldbreakoffstate", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // weldarcstate
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->weldarcstate);
    {
      int rc = PyObject_SetAttrString(_pymessage, "weldarcstate", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // error_code
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->error_code);
    {
      int rc = PyObject_SetAttrString(_pymessage, "error_code", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // check_sum
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->check_sum);
    {
      int rc = PyObject_SetAttrString(_pymessage, "check_sum", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // timestamp
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLongLong(ros_message->timestamp);
    {
      int rc = PyObject_SetAttrString(_pymessage, "timestamp", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // version
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->version.data,
      strlen(ros_message->version.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "version", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
