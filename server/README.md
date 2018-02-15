# Introduction

`idiotic_server.py` is the entry point of the software portion of this project. It operates as the glue that holds the
Model, View and Controller together. It is run without arguments using Python 3 and has the following dependencies:

Required:
* `flask` -- Runs the webserver


Optional:
* `phue` -- Required to use Phillips Hue lights and bridges


The server listens for HTTP POST and GET requests to query and control different modules connected to the controller.
These requests are sent to \[server IP\]/modules. Commands are embedded in a json object inside the body of the message.
Below is an example JSON object:
```javascript
{"set" : [
   {
    "id"    : "0x4ab343cd",
    "attr"  : "brightness",
    "value" : 254
   },
   {
    "class" : "HueLight",
    "name"  : "Dining Room 1",
    "attr"  : "on",
    "value" : true
   }
],
"get" : [
   {
    "id"    : "0x23e4abd4",
    "attr"  : "open"
   },
   {
    "class" : "HueLight",
    "name"  : "Dining Room 2",
    "attr"  : "saturation"
   }
]}
```

IotDevices can be referred to either using the Class type and their name, or by just using their global UUID.
`set` commands return their values in another JSON object with Class type and name, and UUID:
```javascript
{[{
    "class" : "DoorSensor",
    "name"  : "Back Door",
    "id"    : "0x4ab343cd",
    "attr"  : "open",
    "value" : false
  },
  {
    "class" : "HueLight",
    "name"  : "Dining Room 2",
    "id"    : "0x4ab353ad",
    "attr"  : "saturation",
    "value" : 30
   }
]}
```

# Creating a new IdioticDevice

Creating a new IdioticDevice is simple. First, create a new python file in the `control/idiotic_devices` directory.
Use the following snippet as a template for the file:
```python
from control.idiotic_device import IdioticDevice
from control.idiotic_device import action, Attribute

class MyDeviceName(IdioticDevice):

    def __init__(opt_param=None, opt_param2=None):
        self.param = opt_param
        self.param2 = opt_param2

    @Attribute
    def my_attribute():

        my_attribute = some_function_to_get_value_from_device_hardware()

        return my_attribute

    @my_attribute.setter
    def my_attribute(value):

        some_function_to_set_value_on_device_hardware(value)

    @Action
    def my_action(param_for_action):

        some_function_to_tell_device_to_do_something(param_for_action)

```

IdioticDevices consist of two main components: Attributes and Actions. Attributes represent singular values and states,
while Actions are meant to be used to perform something a little more in depth. For example, the brightness of a Hue
Light would be an attribute, and a command used to make the bulb strobe between 3 colors would be an Action.

## Attributes

Attributes have a getter and/or a setter function and their definition is meant to mimic that of properties. However,
they are not descriptor objects and set using `my_attribute.set(value)` and queried using `my_attribute.get()`.

To create an attribute, tag a function using the `@Attribute` decorator. This turns the following function into the
getter method for an instance of an Attribute class. To create a setter for the Attribute use a `@my_attribute.setter`
decorator.

Using the `@Attribute` decorator is required to allow IdioticRoutines to access and set the the data inside the attribute.
Attributes are also enumerated on the UI **\[Very much TODO\]**.

## Actions

Actions are not as complicated as as attributes and only have a single method. However, the `@Action` decorator must be
used to tell Idiotic to enumerate the Action and allow Routines to call it.
