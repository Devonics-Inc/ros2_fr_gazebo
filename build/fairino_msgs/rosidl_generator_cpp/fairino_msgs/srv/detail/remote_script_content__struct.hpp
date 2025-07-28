// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fairino_msgs:srv/RemoteScriptContent.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__SRV__DETAIL__REMOTE_SCRIPT_CONTENT__STRUCT_HPP_
#define FAIRINO_MSGS__SRV__DETAIL__REMOTE_SCRIPT_CONTENT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Request __attribute__((deprecated))
#else
# define DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Request __declspec(deprecated)
#endif

namespace fairino_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct RemoteScriptContent_Request_
{
  using Type = RemoteScriptContent_Request_<ContainerAllocator>;

  explicit RemoteScriptContent_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->line_str = "";
    }
  }

  explicit RemoteScriptContent_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : line_str(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->line_str = "";
    }
  }

  // field types and members
  using _line_str_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _line_str_type line_str;

  // setters for named parameter idiom
  Type & set__line_str(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->line_str = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Request
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Request
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RemoteScriptContent_Request_ & other) const
  {
    if (this->line_str != other.line_str) {
      return false;
    }
    return true;
  }
  bool operator!=(const RemoteScriptContent_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RemoteScriptContent_Request_

// alias to use template instance with default allocator
using RemoteScriptContent_Request =
  fairino_msgs::srv::RemoteScriptContent_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fairino_msgs


#ifndef _WIN32
# define DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Response __attribute__((deprecated))
#else
# define DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Response __declspec(deprecated)
#endif

namespace fairino_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct RemoteScriptContent_Response_
{
  using Type = RemoteScriptContent_Response_<ContainerAllocator>;

  explicit RemoteScriptContent_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->res = "";
    }
  }

  explicit RemoteScriptContent_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : res(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->res = "";
    }
  }

  // field types and members
  using _res_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _res_type res;

  // setters for named parameter idiom
  Type & set__res(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->res = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Response
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fairino_msgs__srv__RemoteScriptContent_Response
    std::shared_ptr<fairino_msgs::srv::RemoteScriptContent_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RemoteScriptContent_Response_ & other) const
  {
    if (this->res != other.res) {
      return false;
    }
    return true;
  }
  bool operator!=(const RemoteScriptContent_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RemoteScriptContent_Response_

// alias to use template instance with default allocator
using RemoteScriptContent_Response =
  fairino_msgs::srv::RemoteScriptContent_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace fairino_msgs

namespace fairino_msgs
{

namespace srv
{

struct RemoteScriptContent
{
  using Request = fairino_msgs::srv::RemoteScriptContent_Request;
  using Response = fairino_msgs::srv::RemoteScriptContent_Response;
};

}  // namespace srv

}  // namespace fairino_msgs

#endif  // FAIRINO_MSGS__SRV__DETAIL__REMOTE_SCRIPT_CONTENT__STRUCT_HPP_
