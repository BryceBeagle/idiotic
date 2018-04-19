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
```
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

IdioticDevices can be referred to either using the Class type and their name, or by just using their global UUID.
`set` commands return their values in another JSON object with Class type and name, and UUID:
### **TODO: This is not current**
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

Creating a new IdioticDevice is simple. First, create a new python file in the `control/device_drivers` directory.
Use the following snippet as a template for the file:
```python
from control.idiotic_device import IdioticDevice
from control.idiotic_device import Attribute

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
        self.ws.send().send(f'{{"set" : {{"{active_device}"}}}}')

    @my_attribute.update
    def my_attribute(value):
        """Update value of my_attribute in controller's cache"""
        self._my_attribute = value

```

IdioticDevices consist of two main components: Attributes and Behaviors. Attributes represent singular values and states,
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

## Behaviors

Behaviors are Behaviors are not as complicated internally as attributes and only have a single method. However, the `@Behavior` decorator must be
used to tell Idiotic to enumerate the Behavior and allow Routines to call it.
