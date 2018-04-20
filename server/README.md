# Introduction

`idiotic_server.py` is the entry point of the software portion of this project. It operates as the glue that holds the
Model and Controller together. In the future the server will serve the View of the system. The server operates as the
communication layer between the devices and the controller. Modules send HTTP PUT requests to the server to notify it of
any changes in the information they measure. Modules also occasionally send the values to the server even if they have
not changes as a way of informing the server that the information is still correct.

It is run without arguments using Python 3 and has the following dependencies:

Required:
* `flask` -- Runs the webserver


Optional:
* `phue` -- Required to use Phillips Hue lights and bridges*

<sub><sup>\* currently required because of some hardcoding -- to be optional in future.<sup><sub>


The devices and the server communicate with each other using websockets. The data is sent on the socket in the form of
string encoded JSON structures. Each JSON structure is an object with one or more of two currently supported keys:
hello and update. The value associated with the key is an array of tasks of that type for the recipient to perform.
Depending on the intended recipient of the message, these instructions are slightly different.

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
