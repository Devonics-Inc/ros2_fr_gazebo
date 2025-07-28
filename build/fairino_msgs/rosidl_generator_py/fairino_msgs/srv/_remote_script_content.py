# generated from rosidl_generator_py/resource/_idl.py.em
# with input from fairino_msgs:srv/RemoteScriptContent.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RemoteScriptContent_Request(type):
    """Metaclass of message 'RemoteScriptContent_Request'."""

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
                'fairino_msgs.srv.RemoteScriptContent_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__remote_script_content__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__remote_script_content__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__remote_script_content__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__remote_script_content__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__remote_script_content__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RemoteScriptContent_Request(metaclass=Metaclass_RemoteScriptContent_Request):
    """Message class 'RemoteScriptContent_Request'."""

    __slots__ = [
        '_line_str',
    ]

    _fields_and_field_types = {
        'line_str': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.line_str = kwargs.get('line_str', str())

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
        if self.line_str != other.line_str:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def line_str(self):
        """Message field 'line_str'."""
        return self._line_str

    @line_str.setter
    def line_str(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'line_str' field must be of type 'str'"
        self._line_str = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_RemoteScriptContent_Response(type):
    """Metaclass of message 'RemoteScriptContent_Response'."""

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
                'fairino_msgs.srv.RemoteScriptContent_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__remote_script_content__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__remote_script_content__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__remote_script_content__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__remote_script_content__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__remote_script_content__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RemoteScriptContent_Response(metaclass=Metaclass_RemoteScriptContent_Response):
    """Message class 'RemoteScriptContent_Response'."""

    __slots__ = [
        '_res',
    ]

    _fields_and_field_types = {
        'res': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.res = kwargs.get('res', str())

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
        if self.res != other.res:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def res(self):
        """Message field 'res'."""
        return self._res

    @res.setter
    def res(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'res' field must be of type 'str'"
        self._res = value


class Metaclass_RemoteScriptContent(type):
    """Metaclass of service 'RemoteScriptContent'."""

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
                'fairino_msgs.srv.RemoteScriptContent')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__remote_script_content

            from fairino_msgs.srv import _remote_script_content
            if _remote_script_content.Metaclass_RemoteScriptContent_Request._TYPE_SUPPORT is None:
                _remote_script_content.Metaclass_RemoteScriptContent_Request.__import_type_support__()
            if _remote_script_content.Metaclass_RemoteScriptContent_Response._TYPE_SUPPORT is None:
                _remote_script_content.Metaclass_RemoteScriptContent_Response.__import_type_support__()


class RemoteScriptContent(metaclass=Metaclass_RemoteScriptContent):
    from fairino_msgs.srv._remote_script_content import RemoteScriptContent_Request as Request
    from fairino_msgs.srv._remote_script_content import RemoteScriptContent_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
