# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fairino_msgs:srv/RemoteCmdInterface.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RemoteCmdInterface_Request(type):
    """Metaclass of message 'RemoteCmdInterface_Request'."""

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
                'fairino_msgs.srv.RemoteCmdInterface_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__remote_cmd_interface__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__remote_cmd_interface__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__remote_cmd_interface__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__remote_cmd_interface__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__remote_cmd_interface__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RemoteCmdInterface_Request(metaclass=Metaclass_RemoteCmdInterface_Request):
    """Message class 'RemoteCmdInterface_Request'."""

    __slots__ = [
        '_cmd_str',
    ]

    _fields_and_field_types = {
        'cmd_str': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.cmd_str = kwargs.get('cmd_str', str())

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
        if self.cmd_str != other.cmd_str:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def cmd_str(self):
        """Message field 'cmd_str'."""
        return self._cmd_str

    @cmd_str.setter
    def cmd_str(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'cmd_str' field must be of type 'str'"
        self._cmd_str = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RemoteCmdInterface_Response(type):
    """Metaclass of message 'RemoteCmdInterface_Response'."""

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
                'fairino_msgs.srv.RemoteCmdInterface_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__remote_cmd_interface__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__remote_cmd_interface__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__remote_cmd_interface__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__remote_cmd_interface__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__remote_cmd_interface__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RemoteCmdInterface_Response(metaclass=Metaclass_RemoteCmdInterface_Response):
    """Message class 'RemoteCmdInterface_Response'."""

    __slots__ = [
        '_cmd_res',
    ]

    _fields_and_field_types = {
        'cmd_res': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.cmd_res = kwargs.get('cmd_res', str())

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
        if self.cmd_res != other.cmd_res:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def cmd_res(self):
        """Message field 'cmd_res'."""
        return self._cmd_res

    @cmd_res.setter
    def cmd_res(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'cmd_res' field must be of type 'str'"
        self._cmd_res = value


class Metaclass_RemoteCmdInterface(type):
    """Metaclass of service 'RemoteCmdInterface'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('fairino_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'fairino_msgs.srv.RemoteCmdInterface')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__remote_cmd_interface

            from fairino_msgs.srv import _remote_cmd_interface
            if _remote_cmd_interface.Metaclass_RemoteCmdInterface_Request._TYPE_SUPPORT is None:
                _remote_cmd_interface.Metaclass_RemoteCmdInterface_Request.__import_type_support__()
            if _remote_cmd_interface.Metaclass_RemoteCmdInterface_Response._TYPE_SUPPORT is None:
                _remote_cmd_interface.Metaclass_RemoteCmdInterface_Response.__import_type_support__()


class RemoteCmdInterface(metaclass=Metaclass_RemoteCmdInterface):
    from fairino_msgs.srv._remote_cmd_interface import RemoteCmdInterface_Request as Request
    from fairino_msgs.srv._remote_cmd_interface import RemoteCmdInterface_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
