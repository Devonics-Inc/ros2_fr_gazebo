# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fairino_msgs:msg/RobotNonrtState.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

# Member 'safetyboxsig'
import numpy  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RobotNonrtState(type):
    """Metaclass of message 'RobotNonrtState'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fairino_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fairino_msgs.msg.RobotNonrtState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__robot_nonrt_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__robot_nonrt_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__robot_nonrt_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__robot_nonrt_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__robot_nonrt_state

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RobotNonrtState(metaclass=Metaclass_RobotNonrtState):
    """Message class 'RobotNonrtState'."""

    __slots__ = [
        '_j1_cur_pos',
        '_j2_cur_pos',
        '_j3_cur_pos',
        '_j4_cur_pos',
        '_j5_cur_pos',
        '_j6_cur_pos',
        '_j1_cur_tor',
        '_j2_cur_tor',
        '_j3_cur_tor',
        '_j4_cur_tor',
        '_j5_cur_tor',
        '_j6_cur_tor',
        '_cart_x_cur_pos',
        '_cart_y_cur_pos',
        '_cart_z_cur_pos',
        '_cart_a_cur_pos',
        '_cart_b_cur_pos',
        '_cart_c_cur_pos',
        '_flange_x_cur_pos',
        '_flange_y_cur_pos',
        '_flange_z_cur_pos',
        '_flange_a_cur_pos',
        '_flange_b_cur_pos',
        '_flange_c_cur_pos',
        '_exaxispos1',
        '_exaxispos2',
        '_exaxispos3',
        '_exaxispos4',
        '_ft_fx_data',
        '_ft_fy_data',
        '_ft_fz_data',
        '_ft_tx_data',
        '_ft_ty_data',
        '_ft_tz_data',
        '_ft_actstatus',
        '_robot_mode',
        '_tool_num',
        '_work_num',
        '_prg_state',
        '_abnormal_stop',
        '_prg_name',
        '_prg_total_line',
        '_prg_cur_line',
        '_dgt_output_h',
        '_dgt_output_l',
        '_dgt_input_h',
        '_dgt_input_l',
        '_tl_dgt_output_l',
        '_tl_dgt_input_l',
        '_emg',
        '_safetyboxsig',
        '_robot_motion_done',
        '_grip_motion_done',
        '_weldbreakoffstate',
        '_weldarcstate',
        '_error_code',
        '_check_sum',
        '_timestamp',
        '_version',
    ]

    _fields_and_field_types = {
        'j1_cur_pos': 'double',
        'j2_cur_pos': 'double',
        'j3_cur_pos': 'double',
        'j4_cur_pos': 'double',
        'j5_cur_pos': 'double',
        'j6_cur_pos': 'double',
        'j1_cur_tor': 'double',
        'j2_cur_tor': 'double',
        'j3_cur_tor': 'double',
        'j4_cur_tor': 'double',
        'j5_cur_tor': 'double',
        'j6_cur_tor': 'double',
        'cart_x_cur_pos': 'double',
        'cart_y_cur_pos': 'double',
        'cart_z_cur_pos': 'double',
        'cart_a_cur_pos': 'double',
        'cart_b_cur_pos': 'double',
        'cart_c_cur_pos': 'double',
        'flange_x_cur_pos': 'double',
        'flange_y_cur_pos': 'double',
        'flange_z_cur_pos': 'double',
        'flange_a_cur_pos': 'double',
        'flange_b_cur_pos': 'double',
        'flange_c_cur_pos': 'double',
        'exaxispos1': 'double',
        'exaxispos2': 'double',
        'exaxispos3': 'double',
        'exaxispos4': 'double',
        'ft_fx_data': 'double',
        'ft_fy_data': 'double',
        'ft_fz_data': 'double',
        'ft_tx_data': 'double',
        'ft_ty_data': 'double',
        'ft_tz_data': 'double',
        'ft_actstatus': 'uint8',
        'robot_mode': 'uint8',
        'tool_num': 'uint8',
        'work_num': 'uint8',
        'prg_state': 'uint8',
        'abnormal_stop': 'uint8',
        'prg_name': 'string',
        'prg_total_line': 'uint8',
        'prg_cur_line': 'uint8',
        'dgt_output_h': 'uint8',
        'dgt_output_l': 'uint8',
        'dgt_input_h': 'uint8',
        'dgt_input_l': 'uint8',
        'tl_dgt_output_l': 'uint8',
        'tl_dgt_input_l': 'uint8',
        'emg': 'uint8',
        'safetyboxsig': 'uint8[6]',
        'robot_motion_done': 'uint8',
        'grip_motion_done': 'uint8',
        'weldbreakoffstate': 'uint8',
        'weldarcstate': 'uint8',
        'error_code': 'uint8',
        'check_sum': 'uint8',
        'timestamp': 'uint64',
        'version': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.Array(rosidl_parser.definition.BasicType('uint8'), 6),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.j1_cur_pos = kwargs.get('j1_cur_pos', float())
        self.j2_cur_pos = kwargs.get('j2_cur_pos', float())
        self.j3_cur_pos = kwargs.get('j3_cur_pos', float())
        self.j4_cur_pos = kwargs.get('j4_cur_pos', float())
        self.j5_cur_pos = kwargs.get('j5_cur_pos', float())
        self.j6_cur_pos = kwargs.get('j6_cur_pos', float())
        self.j1_cur_tor = kwargs.get('j1_cur_tor', float())
        self.j2_cur_tor = kwargs.get('j2_cur_tor', float())
        self.j3_cur_tor = kwargs.get('j3_cur_tor', float())
        self.j4_cur_tor = kwargs.get('j4_cur_tor', float())
        self.j5_cur_tor = kwargs.get('j5_cur_tor', float())
        self.j6_cur_tor = kwargs.get('j6_cur_tor', float())
        self.cart_x_cur_pos = kwargs.get('cart_x_cur_pos', float())
        self.cart_y_cur_pos = kwargs.get('cart_y_cur_pos', float())
        self.cart_z_cur_pos = kwargs.get('cart_z_cur_pos', float())
        self.cart_a_cur_pos = kwargs.get('cart_a_cur_pos', float())
        self.cart_b_cur_pos = kwargs.get('cart_b_cur_pos', float())
        self.cart_c_cur_pos = kwargs.get('cart_c_cur_pos', float())
        self.flange_x_cur_pos = kwargs.get('flange_x_cur_pos', float())
        self.flange_y_cur_pos = kwargs.get('flange_y_cur_pos', float())
        self.flange_z_cur_pos = kwargs.get('flange_z_cur_pos', float())
        self.flange_a_cur_pos = kwargs.get('flange_a_cur_pos', float())
        self.flange_b_cur_pos = kwargs.get('flange_b_cur_pos', float())
        self.flange_c_cur_pos = kwargs.get('flange_c_cur_pos', float())
        self.exaxispos1 = kwargs.get('exaxispos1', float())
        self.exaxispos2 = kwargs.get('exaxispos2', float())
        self.exaxispos3 = kwargs.get('exaxispos3', float())
        self.exaxispos4 = kwargs.get('exaxispos4', float())
        self.ft_fx_data = kwargs.get('ft_fx_data', float())
        self.ft_fy_data = kwargs.get('ft_fy_data', float())
        self.ft_fz_data = kwargs.get('ft_fz_data', float())
        self.ft_tx_data = kwargs.get('ft_tx_data', float())
        self.ft_ty_data = kwargs.get('ft_ty_data', float())
        self.ft_tz_data = kwargs.get('ft_tz_data', float())
        self.ft_actstatus = kwargs.get('ft_actstatus', int())
        self.robot_mode = kwargs.get('robot_mode', int())
        self.tool_num = kwargs.get('tool_num', int())
        self.work_num = kwargs.get('work_num', int())
        self.prg_state = kwargs.get('prg_state', int())
        self.abnormal_stop = kwargs.get('abnormal_stop', int())
        self.prg_name = kwargs.get('prg_name', str())
        self.prg_total_line = kwargs.get('prg_total_line', int())
        self.prg_cur_line = kwargs.get('prg_cur_line', int())
        self.dgt_output_h = kwargs.get('dgt_output_h', int())
        self.dgt_output_l = kwargs.get('dgt_output_l', int())
        self.dgt_input_h = kwargs.get('dgt_input_h', int())
        self.dgt_input_l = kwargs.get('dgt_input_l', int())
        self.tl_dgt_output_l = kwargs.get('tl_dgt_output_l', int())
        self.tl_dgt_input_l = kwargs.get('tl_dgt_input_l', int())
        self.emg = kwargs.get('emg', int())
        if 'safetyboxsig' not in kwargs:
            self.safetyboxsig = numpy.zeros(6, dtype=numpy.uint8)
        else:
            self.safetyboxsig = numpy.array(kwargs.get('safetyboxsig'), dtype=numpy.uint8)
            assert self.safetyboxsig.shape == (6, )
        self.robot_motion_done = kwargs.get('robot_motion_done', int())
        self.grip_motion_done = kwargs.get('grip_motion_done', int())
        self.weldbreakoffstate = kwargs.get('weldbreakoffstate', int())
        self.weldarcstate = kwargs.get('weldarcstate', int())
        self.error_code = kwargs.get('error_code', int())
        self.check_sum = kwargs.get('check_sum', int())
        self.timestamp = kwargs.get('timestamp', int())
        self.version = kwargs.get('version', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.j1_cur_pos != other.j1_cur_pos:
            return False
        if self.j2_cur_pos != other.j2_cur_pos:
            return False
        if self.j3_cur_pos != other.j3_cur_pos:
            return False
        if self.j4_cur_pos != other.j4_cur_pos:
            return False
        if self.j5_cur_pos != other.j5_cur_pos:
            return False
        if self.j6_cur_pos != other.j6_cur_pos:
            return False
        if self.j1_cur_tor != other.j1_cur_tor:
            return False
        if self.j2_cur_tor != other.j2_cur_tor:
            return False
        if self.j3_cur_tor != other.j3_cur_tor:
            return False
        if self.j4_cur_tor != other.j4_cur_tor:
            return False
        if self.j5_cur_tor != other.j5_cur_tor:
            return False
        if self.j6_cur_tor != other.j6_cur_tor:
            return False
        if self.cart_x_cur_pos != other.cart_x_cur_pos:
            return False
        if self.cart_y_cur_pos != other.cart_y_cur_pos:
            return False
        if self.cart_z_cur_pos != other.cart_z_cur_pos:
            return False
        if self.cart_a_cur_pos != other.cart_a_cur_pos:
            return False
        if self.cart_b_cur_pos != other.cart_b_cur_pos:
            return False
        if self.cart_c_cur_pos != other.cart_c_cur_pos:
            return False
        if self.flange_x_cur_pos != other.flange_x_cur_pos:
            return False
        if self.flange_y_cur_pos != other.flange_y_cur_pos:
            return False
        if self.flange_z_cur_pos != other.flange_z_cur_pos:
            return False
        if self.flange_a_cur_pos != other.flange_a_cur_pos:
            return False
        if self.flange_b_cur_pos != other.flange_b_cur_pos:
            return False
        if self.flange_c_cur_pos != other.flange_c_cur_pos:
            return False
        if self.exaxispos1 != other.exaxispos1:
            return False
        if self.exaxispos2 != other.exaxispos2:
            return False
        if self.exaxispos3 != other.exaxispos3:
            return False
        if self.exaxispos4 != other.exaxispos4:
            return False
        if self.ft_fx_data != other.ft_fx_data:
            return False
        if self.ft_fy_data != other.ft_fy_data:
            return False
        if self.ft_fz_data != other.ft_fz_data:
            return False
        if self.ft_tx_data != other.ft_tx_data:
            return False
        if self.ft_ty_data != other.ft_ty_data:
            return False
        if self.ft_tz_data != other.ft_tz_data:
            return False
        if self.ft_actstatus != other.ft_actstatus:
            return False
        if self.robot_mode != other.robot_mode:
            return False
        if self.tool_num != other.tool_num:
            return False
        if self.work_num != other.work_num:
            return False
        if self.prg_state != other.prg_state:
            return False
        if self.abnormal_stop != other.abnormal_stop:
            return False
        if self.prg_name != other.prg_name:
            return False
        if self.prg_total_line != other.prg_total_line:
            return False
        if self.prg_cur_line != other.prg_cur_line:
            return False
        if self.dgt_output_h != other.dgt_output_h:
            return False
        if self.dgt_output_l != other.dgt_output_l:
            return False
        if self.dgt_input_h != other.dgt_input_h:
            return False
        if self.dgt_input_l != other.dgt_input_l:
            return False
        if self.tl_dgt_output_l != other.tl_dgt_output_l:
            return False
        if self.tl_dgt_input_l != other.tl_dgt_input_l:
            return False
        if self.emg != other.emg:
            return False
        if all(self.safetyboxsig != other.safetyboxsig):
            return False
        if self.robot_motion_done != other.robot_motion_done:
            return False
        if self.grip_motion_done != other.grip_motion_done:
            return False
        if self.weldbreakoffstate != other.weldbreakoffstate:
            return False
        if self.weldarcstate != other.weldarcstate:
            return False
        if self.error_code != other.error_code:
            return False
        if self.check_sum != other.check_sum:
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.version != other.version:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def j1_cur_pos(self):
        """Message field 'j1_cur_pos'."""
        return self._j1_cur_pos

    @j1_cur_pos.setter
    def j1_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j1_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j1_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j1_cur_pos = value

    @builtins.property
    def j2_cur_pos(self):
        """Message field 'j2_cur_pos'."""
        return self._j2_cur_pos

    @j2_cur_pos.setter
    def j2_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j2_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j2_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j2_cur_pos = value

    @builtins.property
    def j3_cur_pos(self):
        """Message field 'j3_cur_pos'."""
        return self._j3_cur_pos

    @j3_cur_pos.setter
    def j3_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j3_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j3_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j3_cur_pos = value

    @builtins.property
    def j4_cur_pos(self):
        """Message field 'j4_cur_pos'."""
        return self._j4_cur_pos

    @j4_cur_pos.setter
    def j4_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j4_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j4_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j4_cur_pos = value

    @builtins.property
    def j5_cur_pos(self):
        """Message field 'j5_cur_pos'."""
        return self._j5_cur_pos

    @j5_cur_pos.setter
    def j5_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j5_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j5_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j5_cur_pos = value

    @builtins.property
    def j6_cur_pos(self):
        """Message field 'j6_cur_pos'."""
        return self._j6_cur_pos

    @j6_cur_pos.setter
    def j6_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j6_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j6_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j6_cur_pos = value

    @builtins.property
    def j1_cur_tor(self):
        """Message field 'j1_cur_tor'."""
        return self._j1_cur_tor

    @j1_cur_tor.setter
    def j1_cur_tor(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j1_cur_tor' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j1_cur_tor' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j1_cur_tor = value

    @builtins.property
    def j2_cur_tor(self):
        """Message field 'j2_cur_tor'."""
        return self._j2_cur_tor

    @j2_cur_tor.setter
    def j2_cur_tor(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j2_cur_tor' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j2_cur_tor' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j2_cur_tor = value

    @builtins.property
    def j3_cur_tor(self):
        """Message field 'j3_cur_tor'."""
        return self._j3_cur_tor

    @j3_cur_tor.setter
    def j3_cur_tor(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j3_cur_tor' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j3_cur_tor' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j3_cur_tor = value

    @builtins.property
    def j4_cur_tor(self):
        """Message field 'j4_cur_tor'."""
        return self._j4_cur_tor

    @j4_cur_tor.setter
    def j4_cur_tor(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j4_cur_tor' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j4_cur_tor' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j4_cur_tor = value

    @builtins.property
    def j5_cur_tor(self):
        """Message field 'j5_cur_tor'."""
        return self._j5_cur_tor

    @j5_cur_tor.setter
    def j5_cur_tor(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j5_cur_tor' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j5_cur_tor' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j5_cur_tor = value

    @builtins.property
    def j6_cur_tor(self):
        """Message field 'j6_cur_tor'."""
        return self._j6_cur_tor

    @j6_cur_tor.setter
    def j6_cur_tor(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'j6_cur_tor' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'j6_cur_tor' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._j6_cur_tor = value

    @builtins.property
    def cart_x_cur_pos(self):
        """Message field 'cart_x_cur_pos'."""
        return self._cart_x_cur_pos

    @cart_x_cur_pos.setter
    def cart_x_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cart_x_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cart_x_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cart_x_cur_pos = value

    @builtins.property
    def cart_y_cur_pos(self):
        """Message field 'cart_y_cur_pos'."""
        return self._cart_y_cur_pos

    @cart_y_cur_pos.setter
    def cart_y_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cart_y_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cart_y_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cart_y_cur_pos = value

    @builtins.property
    def cart_z_cur_pos(self):
        """Message field 'cart_z_cur_pos'."""
        return self._cart_z_cur_pos

    @cart_z_cur_pos.setter
    def cart_z_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cart_z_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cart_z_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cart_z_cur_pos = value

    @builtins.property
    def cart_a_cur_pos(self):
        """Message field 'cart_a_cur_pos'."""
        return self._cart_a_cur_pos

    @cart_a_cur_pos.setter
    def cart_a_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cart_a_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cart_a_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cart_a_cur_pos = value

    @builtins.property
    def cart_b_cur_pos(self):
        """Message field 'cart_b_cur_pos'."""
        return self._cart_b_cur_pos

    @cart_b_cur_pos.setter
    def cart_b_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cart_b_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cart_b_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cart_b_cur_pos = value

    @builtins.property
    def cart_c_cur_pos(self):
        """Message field 'cart_c_cur_pos'."""
        return self._cart_c_cur_pos

    @cart_c_cur_pos.setter
    def cart_c_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cart_c_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'cart_c_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._cart_c_cur_pos = value

    @builtins.property
    def flange_x_cur_pos(self):
        """Message field 'flange_x_cur_pos'."""
        return self._flange_x_cur_pos

    @flange_x_cur_pos.setter
    def flange_x_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'flange_x_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'flange_x_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._flange_x_cur_pos = value

    @builtins.property
    def flange_y_cur_pos(self):
        """Message field 'flange_y_cur_pos'."""
        return self._flange_y_cur_pos

    @flange_y_cur_pos.setter
    def flange_y_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'flange_y_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'flange_y_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._flange_y_cur_pos = value

    @builtins.property
    def flange_z_cur_pos(self):
        """Message field 'flange_z_cur_pos'."""
        return self._flange_z_cur_pos

    @flange_z_cur_pos.setter
    def flange_z_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'flange_z_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'flange_z_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._flange_z_cur_pos = value

    @builtins.property
    def flange_a_cur_pos(self):
        """Message field 'flange_a_cur_pos'."""
        return self._flange_a_cur_pos

    @flange_a_cur_pos.setter
    def flange_a_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'flange_a_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'flange_a_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._flange_a_cur_pos = value

    @builtins.property
    def flange_b_cur_pos(self):
        """Message field 'flange_b_cur_pos'."""
        return self._flange_b_cur_pos

    @flange_b_cur_pos.setter
    def flange_b_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'flange_b_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'flange_b_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._flange_b_cur_pos = value

    @builtins.property
    def flange_c_cur_pos(self):
        """Message field 'flange_c_cur_pos'."""
        return self._flange_c_cur_pos

    @flange_c_cur_pos.setter
    def flange_c_cur_pos(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'flange_c_cur_pos' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'flange_c_cur_pos' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._flange_c_cur_pos = value

    @builtins.property
    def exaxispos1(self):
        """Message field 'exaxispos1'."""
        return self._exaxispos1

    @exaxispos1.setter
    def exaxispos1(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'exaxispos1' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'exaxispos1' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._exaxispos1 = value

    @builtins.property
    def exaxispos2(self):
        """Message field 'exaxispos2'."""
        return self._exaxispos2

    @exaxispos2.setter
    def exaxispos2(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'exaxispos2' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'exaxispos2' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._exaxispos2 = value

    @builtins.property
    def exaxispos3(self):
        """Message field 'exaxispos3'."""
        return self._exaxispos3

    @exaxispos3.setter
    def exaxispos3(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'exaxispos3' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'exaxispos3' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._exaxispos3 = value

    @builtins.property
    def exaxispos4(self):
        """Message field 'exaxispos4'."""
        return self._exaxispos4

    @exaxispos4.setter
    def exaxispos4(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'exaxispos4' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'exaxispos4' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._exaxispos4 = value

    @builtins.property
    def ft_fx_data(self):
        """Message field 'ft_fx_data'."""
        return self._ft_fx_data

    @ft_fx_data.setter
    def ft_fx_data(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ft_fx_data' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ft_fx_data' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ft_fx_data = value

    @builtins.property
    def ft_fy_data(self):
        """Message field 'ft_fy_data'."""
        return self._ft_fy_data

    @ft_fy_data.setter
    def ft_fy_data(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ft_fy_data' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ft_fy_data' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ft_fy_data = value

    @builtins.property
    def ft_fz_data(self):
        """Message field 'ft_fz_data'."""
        return self._ft_fz_data

    @ft_fz_data.setter
    def ft_fz_data(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ft_fz_data' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ft_fz_data' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ft_fz_data = value

    @builtins.property
    def ft_tx_data(self):
        """Message field 'ft_tx_data'."""
        return self._ft_tx_data

    @ft_tx_data.setter
    def ft_tx_data(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ft_tx_data' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ft_tx_data' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ft_tx_data = value

    @builtins.property
    def ft_ty_data(self):
        """Message field 'ft_ty_data'."""
        return self._ft_ty_data

    @ft_ty_data.setter
    def ft_ty_data(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ft_ty_data' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ft_ty_data' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ft_ty_data = value

    @builtins.property
    def ft_tz_data(self):
        """Message field 'ft_tz_data'."""
        return self._ft_tz_data

    @ft_tz_data.setter
    def ft_tz_data(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'ft_tz_data' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'ft_tz_data' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._ft_tz_data = value

    @builtins.property
    def ft_actstatus(self):
        """Message field 'ft_actstatus'."""
        return self._ft_actstatus

    @ft_actstatus.setter
    def ft_actstatus(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'ft_actstatus' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'ft_actstatus' field must be an unsigned integer in [0, 255]"
        self._ft_actstatus = value

    @builtins.property
    def robot_mode(self):
        """Message field 'robot_mode'."""
        return self._robot_mode

    @robot_mode.setter
    def robot_mode(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot_mode' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'robot_mode' field must be an unsigned integer in [0, 255]"
        self._robot_mode = value

    @builtins.property
    def tool_num(self):
        """Message field 'tool_num'."""
        return self._tool_num

    @tool_num.setter
    def tool_num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tool_num' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'tool_num' field must be an unsigned integer in [0, 255]"
        self._tool_num = value

    @builtins.property
    def work_num(self):
        """Message field 'work_num'."""
        return self._work_num

    @work_num.setter
    def work_num(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'work_num' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'work_num' field must be an unsigned integer in [0, 255]"
        self._work_num = value

    @builtins.property
    def prg_state(self):
        """Message field 'prg_state'."""
        return self._prg_state

    @prg_state.setter
    def prg_state(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'prg_state' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'prg_state' field must be an unsigned integer in [0, 255]"
        self._prg_state = value

    @builtins.property
    def abnormal_stop(self):
        """Message field 'abnormal_stop'."""
        return self._abnormal_stop

    @abnormal_stop.setter
    def abnormal_stop(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'abnormal_stop' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'abnormal_stop' field must be an unsigned integer in [0, 255]"
        self._abnormal_stop = value

    @builtins.property
    def prg_name(self):
        """Message field 'prg_name'."""
        return self._prg_name

    @prg_name.setter
    def prg_name(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'prg_name' field must be of type 'str'"
        self._prg_name = value

    @builtins.property
    def prg_total_line(self):
        """Message field 'prg_total_line'."""
        return self._prg_total_line

    @prg_total_line.setter
    def prg_total_line(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'prg_total_line' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'prg_total_line' field must be an unsigned integer in [0, 255]"
        self._prg_total_line = value

    @builtins.property
    def prg_cur_line(self):
        """Message field 'prg_cur_line'."""
        return self._prg_cur_line

    @prg_cur_line.setter
    def prg_cur_line(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'prg_cur_line' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'prg_cur_line' field must be an unsigned integer in [0, 255]"
        self._prg_cur_line = value

    @builtins.property
    def dgt_output_h(self):
        """Message field 'dgt_output_h'."""
        return self._dgt_output_h

    @dgt_output_h.setter
    def dgt_output_h(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dgt_output_h' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'dgt_output_h' field must be an unsigned integer in [0, 255]"
        self._dgt_output_h = value

    @builtins.property
    def dgt_output_l(self):
        """Message field 'dgt_output_l'."""
        return self._dgt_output_l

    @dgt_output_l.setter
    def dgt_output_l(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dgt_output_l' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'dgt_output_l' field must be an unsigned integer in [0, 255]"
        self._dgt_output_l = value

    @builtins.property
    def dgt_input_h(self):
        """Message field 'dgt_input_h'."""
        return self._dgt_input_h

    @dgt_input_h.setter
    def dgt_input_h(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dgt_input_h' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'dgt_input_h' field must be an unsigned integer in [0, 255]"
        self._dgt_input_h = value

    @builtins.property
    def dgt_input_l(self):
        """Message field 'dgt_input_l'."""
        return self._dgt_input_l

    @dgt_input_l.setter
    def dgt_input_l(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'dgt_input_l' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'dgt_input_l' field must be an unsigned integer in [0, 255]"
        self._dgt_input_l = value

    @builtins.property
    def tl_dgt_output_l(self):
        """Message field 'tl_dgt_output_l'."""
        return self._tl_dgt_output_l

    @tl_dgt_output_l.setter
    def tl_dgt_output_l(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tl_dgt_output_l' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'tl_dgt_output_l' field must be an unsigned integer in [0, 255]"
        self._tl_dgt_output_l = value

    @builtins.property
    def tl_dgt_input_l(self):
        """Message field 'tl_dgt_input_l'."""
        return self._tl_dgt_input_l

    @tl_dgt_input_l.setter
    def tl_dgt_input_l(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tl_dgt_input_l' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'tl_dgt_input_l' field must be an unsigned integer in [0, 255]"
        self._tl_dgt_input_l = value

    @builtins.property
    def emg(self):
        """Message field 'emg'."""
        return self._emg

    @emg.setter
    def emg(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'emg' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'emg' field must be an unsigned integer in [0, 255]"
        self._emg = value

    @builtins.property
    def safetyboxsig(self):
        """Message field 'safetyboxsig'."""
        return self._safetyboxsig

    @safetyboxsig.setter
    def safetyboxsig(self, value):
        if isinstance(value, numpy.ndarray):
            assert value.dtype == numpy.uint8, \
                "The 'safetyboxsig' numpy.ndarray() must have the dtype of 'numpy.uint8'"
            assert value.size == 6, \
                "The 'safetyboxsig' numpy.ndarray() must have a size of 6"
            self._safetyboxsig = value
            return
        if __debug__:
            from collections.abc import Sequence
            from collections.abc import Set
            from collections import UserList
            from collections import UserString
            assert \
                ((isinstance(value, Sequence) or
                  isinstance(value, Set) or
                  isinstance(value, UserList)) and
                 not isinstance(value, str) and
                 not isinstance(value, UserString) and
                 len(value) == 6 and
                 all(isinstance(v, int) for v in value) and
                 all(val >= 0 and val < 256 for val in value)), \
                "The 'safetyboxsig' field must be a set or sequence with length 6 and each value of type 'int' and each unsigned integer in [0, 255]"
        self._safetyboxsig = numpy.array(value, dtype=numpy.uint8)

    @builtins.property
    def robot_motion_done(self):
        """Message field 'robot_motion_done'."""
        return self._robot_motion_done

    @robot_motion_done.setter
    def robot_motion_done(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'robot_motion_done' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'robot_motion_done' field must be an unsigned integer in [0, 255]"
        self._robot_motion_done = value

    @builtins.property
    def grip_motion_done(self):
        """Message field 'grip_motion_done'."""
        return self._grip_motion_done

    @grip_motion_done.setter
    def grip_motion_done(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'grip_motion_done' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'grip_motion_done' field must be an unsigned integer in [0, 255]"
        self._grip_motion_done = value

    @builtins.property
    def weldbreakoffstate(self):
        """Message field 'weldbreakoffstate'."""
        return self._weldbreakoffstate

    @weldbreakoffstate.setter
    def weldbreakoffstate(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'weldbreakoffstate' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'weldbreakoffstate' field must be an unsigned integer in [0, 255]"
        self._weldbreakoffstate = value

    @builtins.property
    def weldarcstate(self):
        """Message field 'weldarcstate'."""
        return self._weldarcstate

    @weldarcstate.setter
    def weldarcstate(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'weldarcstate' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'weldarcstate' field must be an unsigned integer in [0, 255]"
        self._weldarcstate = value

    @builtins.property
    def error_code(self):
        """Message field 'error_code'."""
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'error_code' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'error_code' field must be an unsigned integer in [0, 255]"
        self._error_code = value

    @builtins.property
    def check_sum(self):
        """Message field 'check_sum'."""
        return self._check_sum

    @check_sum.setter
    def check_sum(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'check_sum' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'check_sum' field must be an unsigned integer in [0, 255]"
        self._check_sum = value

    @builtins.property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp = value

    @builtins.property
    def version(self):
        """Message field 'version'."""
        return self._version

    @version.setter
    def version(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'version' field must be of type 'str'"
        self._version = value
