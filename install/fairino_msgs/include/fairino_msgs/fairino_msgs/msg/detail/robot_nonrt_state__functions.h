// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fairino_msgs:msg/RobotNonrtState.idl
// generated code does not contain a copyright notice

#ifndef FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__FUNCTIONS_H_
#define FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fairino_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "fairino_msgs/msg/detail/robot_nonrt_state__struct.h"

/// Initialize msg/RobotNonrtState message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fairino_msgs__msg__RobotNonrtState
 * )) before or use
 * fairino_msgs__msg__RobotNonrtState__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
bool
fairino_msgs__msg__RobotNonrtState__init(fairino_msgs__msg__RobotNonrtState * msg);

/// Finalize msg/RobotNonrtState message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
void
fairino_msgs__msg__RobotNonrtState__fini(fairino_msgs__msg__RobotNonrtState * msg);

/// Create msg/RobotNonrtState message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fairino_msgs__msg__RobotNonrtState__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
fairino_msgs__msg__RobotNonrtState *
fairino_msgs__msg__RobotNonrtState__create();

/// Destroy msg/RobotNonrtState message.
/**
 * It calls
 * fairino_msgs__msg__RobotNonrtState__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
void
fairino_msgs__msg__RobotNonrtState__destroy(fairino_msgs__msg__RobotNonrtState * msg);

/// Check for msg/RobotNonrtState message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
bool
fairino_msgs__msg__RobotNonrtState__are_equal(const fairino_msgs__msg__RobotNonrtState * lhs, const fairino_msgs__msg__RobotNonrtState * rhs);

/// Copy a msg/RobotNonrtState message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
bool
fairino_msgs__msg__RobotNonrtState__copy(
  const fairino_msgs__msg__RobotNonrtState * input,
  fairino_msgs__msg__RobotNonrtState * output);

/// Initialize array of msg/RobotNonrtState messages.
/**
 * It allocates the memory for the number of elements and calls
 * fairino_msgs__msg__RobotNonrtState__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
bool
fairino_msgs__msg__RobotNonrtState__Sequence__init(fairino_msgs__msg__RobotNonrtState__Sequence * array, size_t size);

/// Finalize array of msg/RobotNonrtState messages.
/**
 * It calls
 * fairino_msgs__msg__RobotNonrtState__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
void
fairino_msgs__msg__RobotNonrtState__Sequence__fini(fairino_msgs__msg__RobotNonrtState__Sequence * array);

/// Create array of msg/RobotNonrtState messages.
/**
 * It allocates the memory for the array and calls
 * fairino_msgs__msg__RobotNonrtState__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
fairino_msgs__msg__RobotNonrtState__Sequence *
fairino_msgs__msg__RobotNonrtState__Sequence__create(size_t size);

/// Destroy array of msg/RobotNonrtState messages.
/**
 * It calls
 * fairino_msgs__msg__RobotNonrtState__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
void
fairino_msgs__msg__RobotNonrtState__Sequence__destroy(fairino_msgs__msg__RobotNonrtState__Sequence * array);

/// Check for msg/RobotNonrtState message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
bool
fairino_msgs__msg__RobotNonrtState__Sequence__are_equal(const fairino_msgs__msg__RobotNonrtState__Sequence * lhs, const fairino_msgs__msg__RobotNonrtState__Sequence * rhs);

/// Copy an array of msg/RobotNonrtState messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_fairino_msgs
bool
fairino_msgs__msg__RobotNonrtState__Sequence__copy(
  const fairino_msgs__msg__RobotNonrtState__Sequence * input,
  fairino_msgs__msg__RobotNonrtState__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FAIRINO_MSGS__MSG__DETAIL__ROBOT_NONRT_STATE__FUNCTIONS_H_
