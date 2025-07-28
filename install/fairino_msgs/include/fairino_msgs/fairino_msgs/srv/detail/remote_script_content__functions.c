// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fairino_msgs:srv/RemoteScriptContent.idl
// generated code does not contain a copyright notice
#include "fairino_msgs/srv/detail/remote_script_content__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `line_str`
#include "rosidl_runtime_c/string_functions.h"

bool
fairino_msgs__srv__RemoteScriptContent_Request__init(fairino_msgs__srv__RemoteScriptContent_Request * msg)
{
  if (!msg) {
    return false;
  }
  // line_str
  if (!rosidl_runtime_c__String__init(&msg->line_str)) {
    fairino_msgs__srv__RemoteScriptContent_Request__fini(msg);
    return false;
  }
  return true;
}

void
fairino_msgs__srv__RemoteScriptContent_Request__fini(fairino_msgs__srv__RemoteScriptContent_Request * msg)
{
  if (!msg) {
    return;
  }
  // line_str
  rosidl_runtime_c__String__fini(&msg->line_str);
}

bool
fairino_msgs__srv__RemoteScriptContent_Request__are_equal(const fairino_msgs__srv__RemoteScriptContent_Request * lhs, const fairino_msgs__srv__RemoteScriptContent_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // line_str
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->line_str), &(rhs->line_str)))
  {
    return false;
  }
  return true;
}

bool
fairino_msgs__srv__RemoteScriptContent_Request__copy(
  const fairino_msgs__srv__RemoteScriptContent_Request * input,
  fairino_msgs__srv__RemoteScriptContent_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // line_str
  if (!rosidl_runtime_c__String__copy(
      &(input->line_str), &(output->line_str)))
  {
    return false;
  }
  return true;
}

fairino_msgs__srv__RemoteScriptContent_Request *
fairino_msgs__srv__RemoteScriptContent_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__srv__RemoteScriptContent_Request * msg = (fairino_msgs__srv__RemoteScriptContent_Request *)allocator.allocate(sizeof(fairino_msgs__srv__RemoteScriptContent_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fairino_msgs__srv__RemoteScriptContent_Request));
  bool success = fairino_msgs__srv__RemoteScriptContent_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fairino_msgs__srv__RemoteScriptContent_Request__destroy(fairino_msgs__srv__RemoteScriptContent_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fairino_msgs__srv__RemoteScriptContent_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fairino_msgs__srv__RemoteScriptContent_Request__Sequence__init(fairino_msgs__srv__RemoteScriptContent_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__srv__RemoteScriptContent_Request * data = NULL;

  if (size) {
    data = (fairino_msgs__srv__RemoteScriptContent_Request *)allocator.zero_allocate(size, sizeof(fairino_msgs__srv__RemoteScriptContent_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fairino_msgs__srv__RemoteScriptContent_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fairino_msgs__srv__RemoteScriptContent_Request__fini(&data[i - 1]);
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
fairino_msgs__srv__RemoteScriptContent_Request__Sequence__fini(fairino_msgs__srv__RemoteScriptContent_Request__Sequence * array)
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
      fairino_msgs__srv__RemoteScriptContent_Request__fini(&array->data[i]);
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

fairino_msgs__srv__RemoteScriptContent_Request__Sequence *
fairino_msgs__srv__RemoteScriptContent_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__srv__RemoteScriptContent_Request__Sequence * array = (fairino_msgs__srv__RemoteScriptContent_Request__Sequence *)allocator.allocate(sizeof(fairino_msgs__srv__RemoteScriptContent_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fairino_msgs__srv__RemoteScriptContent_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fairino_msgs__srv__RemoteScriptContent_Request__Sequence__destroy(fairino_msgs__srv__RemoteScriptContent_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fairino_msgs__srv__RemoteScriptContent_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fairino_msgs__srv__RemoteScriptContent_Request__Sequence__are_equal(const fairino_msgs__srv__RemoteScriptContent_Request__Sequence * lhs, const fairino_msgs__srv__RemoteScriptContent_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fairino_msgs__srv__RemoteScriptContent_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fairino_msgs__srv__RemoteScriptContent_Request__Sequence__copy(
  const fairino_msgs__srv__RemoteScriptContent_Request__Sequence * input,
  fairino_msgs__srv__RemoteScriptContent_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fairino_msgs__srv__RemoteScriptContent_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fairino_msgs__srv__RemoteScriptContent_Request * data =
      (fairino_msgs__srv__RemoteScriptContent_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fairino_msgs__srv__RemoteScriptContent_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fairino_msgs__srv__RemoteScriptContent_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fairino_msgs__srv__RemoteScriptContent_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `res`
// already included above
// #include "rosidl_runtime_c/string_functions.h"

bool
fairino_msgs__srv__RemoteScriptContent_Response__init(fairino_msgs__srv__RemoteScriptContent_Response * msg)
{
  if (!msg) {
    return false;
  }
  // res
  if (!rosidl_runtime_c__String__init(&msg->res)) {
    fairino_msgs__srv__RemoteScriptContent_Response__fini(msg);
    return false;
  }
  return true;
}

void
fairino_msgs__srv__RemoteScriptContent_Response__fini(fairino_msgs__srv__RemoteScriptContent_Response * msg)
{
  if (!msg) {
    return;
  }
  // res
  rosidl_runtime_c__String__fini(&msg->res);
}

bool
fairino_msgs__srv__RemoteScriptContent_Response__are_equal(const fairino_msgs__srv__RemoteScriptContent_Response * lhs, const fairino_msgs__srv__RemoteScriptContent_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // res
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->res), &(rhs->res)))
  {
    return false;
  }
  return true;
}

bool
fairino_msgs__srv__RemoteScriptContent_Response__copy(
  const fairino_msgs__srv__RemoteScriptContent_Response * input,
  fairino_msgs__srv__RemoteScriptContent_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // res
  if (!rosidl_runtime_c__String__copy(
      &(input->res), &(output->res)))
  {
    return false;
  }
  return true;
}

fairino_msgs__srv__RemoteScriptContent_Response *
fairino_msgs__srv__RemoteScriptContent_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__srv__RemoteScriptContent_Response * msg = (fairino_msgs__srv__RemoteScriptContent_Response *)allocator.allocate(sizeof(fairino_msgs__srv__RemoteScriptContent_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fairino_msgs__srv__RemoteScriptContent_Response));
  bool success = fairino_msgs__srv__RemoteScriptContent_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fairino_msgs__srv__RemoteScriptContent_Response__destroy(fairino_msgs__srv__RemoteScriptContent_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fairino_msgs__srv__RemoteScriptContent_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fairino_msgs__srv__RemoteScriptContent_Response__Sequence__init(fairino_msgs__srv__RemoteScriptContent_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__srv__RemoteScriptContent_Response * data = NULL;

  if (size) {
    data = (fairino_msgs__srv__RemoteScriptContent_Response *)allocator.zero_allocate(size, sizeof(fairino_msgs__srv__RemoteScriptContent_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fairino_msgs__srv__RemoteScriptContent_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fairino_msgs__srv__RemoteScriptContent_Response__fini(&data[i - 1]);
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
fairino_msgs__srv__RemoteScriptContent_Response__Sequence__fini(fairino_msgs__srv__RemoteScriptContent_Response__Sequence * array)
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
      fairino_msgs__srv__RemoteScriptContent_Response__fini(&array->data[i]);
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

fairino_msgs__srv__RemoteScriptContent_Response__Sequence *
fairino_msgs__srv__RemoteScriptContent_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fairino_msgs__srv__RemoteScriptContent_Response__Sequence * array = (fairino_msgs__srv__RemoteScriptContent_Response__Sequence *)allocator.allocate(sizeof(fairino_msgs__srv__RemoteScriptContent_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fairino_msgs__srv__RemoteScriptContent_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fairino_msgs__srv__RemoteScriptContent_Response__Sequence__destroy(fairino_msgs__srv__RemoteScriptContent_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fairino_msgs__srv__RemoteScriptContent_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fairino_msgs__srv__RemoteScriptContent_Response__Sequence__are_equal(const fairino_msgs__srv__RemoteScriptContent_Response__Sequence * lhs, const fairino_msgs__srv__RemoteScriptContent_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fairino_msgs__srv__RemoteScriptContent_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fairino_msgs__srv__RemoteScriptContent_Response__Sequence__copy(
  const fairino_msgs__srv__RemoteScriptContent_Response__Sequence * input,
  fairino_msgs__srv__RemoteScriptContent_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fairino_msgs__srv__RemoteScriptContent_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    fairino_msgs__srv__RemoteScriptContent_Response * data =
      (fairino_msgs__srv__RemoteScriptContent_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fairino_msgs__srv__RemoteScriptContent_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          fairino_msgs__srv__RemoteScriptContent_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!fairino_msgs__srv__RemoteScriptContent_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
