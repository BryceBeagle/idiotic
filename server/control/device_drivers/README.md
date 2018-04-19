# Creating a new IdioticDevice

Creating a new IdioticDevice is simple. First, create a new python file in the `control/device_drivers` directory.
Use the following snippet as a template/example for the file:
```python
from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute, Behavior

class MyDeviceName(IdioticDevice):

    def __init__(self):
        self._my_attribite = None

    @Attribute
    def my_attribute():
        """Get my_attribute from device or from controller if cached

        Implicit my_attribute.getter
        """
        # In this case, the value is retrieved from cache
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(value):
        """Instruct device to set my_attribute to value"""
        self.ws.get().send(f'{{"set" : {{"{active_device}"}}}}')

    @my_attribute.updater
    def my_attribute(value):
        """Update value of my_attribute in controller's cache"""
        self._my_attribute = value

    @Behavior
    def thing_to_do(param1, param2):
        """Have device do some thing"""
        self.ws.get().send(f'{{"do" : "thing_to_do"}}')

```

IdioticDevices consist of two main components: Attributes and Behaviors. Attributes represent singular values and states,
while Actions are meant to be used to perform something a little more in depth. For example, the brightness of a Hue
Light would be an attribute, and a command used to make the bulb strobe between 3 colors would be an Action.

## Attributes

Attributes represent singular values and states. For example, the brightness of a Hue Light would be an attribute, and
would have a getter and a setter method. Because the HueLights do not ping the server with status information, the
HueLight Attributes would not have updater methods. On the other hand, a temperature sensor whose sole purpose is to
report status would have updater and getter functions for its temp attribute.

Attributes are defined above a function use decorators. The plain @Attribute decorator must be used first and designates
the following function as the getter function for the Attribute. To define a setter or updater function use
`getter_func_name.setter` or `getter_func_name.updater`, where getter_func_name is the name of the function defined as
the getter function.

## Behaviors

Behaviors are abilities that a device can perform, that are slightly more complicated that the setting of a single value
that an attribute setter function provides. An example of a behavior could be a HueLight having a transition ability to
slowly change between two different colors, which would be arguments fort the behavior function. Behaviors are not as
complicated internally as attributes and only have a single method. However, the @Behavior decorator must be used to
tell Idiotic to enumerate the Behavior and allow Routines to call it.
