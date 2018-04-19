# Introduction

`idiotic_server.py` is the entry point of the software portion of this project. It operates as the glue that holds the
Model and Controller together, plus any potential, future View. It is run without arguments using Python 3 and has the following dependencies:

Required:
* `flask` -- Runs the webserver


Optional:
* `phue` -- Required to use Phillips Hue lights and bridges*

<sub><sup>\* currently required because of some hardcoding -- to be optional in future.<sup><sub>


The devices and the server communicate with each other using websockets. The data is sent on the socket in the form of
string encoded JSON structures. Each JSON structure is an object with one or more of three allowed keys: set, get, and
do. The value associated with the key is an array of tasks of that type for the recipient to perform. Depending on the
intended recipient of the message, these instructions are slightly different.

An IdioticDevice sends a hello message attempting to establish connection to the server, usually during its
initialization sequence. If the message is a hello message, the json structure must contain a class type in the
"class" key to be associated with the uuid.

Below are example JSON objects, for each message type:

hello structure:
```javascript
{
  "hello": null,
  "uuid": "13:8C:14:87:B7:AD",
  "class": "DoorSensor"
}
```
update structure:
```javascript
{
  "uuid": "13:8C:14:87:B7:AD",
  "update": {
    "door_state": 1,
    "some_value": "some string"
  }
}
```
get structure:
```
[unimplemented]
```


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
