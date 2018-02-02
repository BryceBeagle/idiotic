**Introduction**

`iot_server.py` is the entry point of the software portion of this project. It operates as the glue that holds the
Model, View and Controller together. It is run without arguments using Python 3 and has the following dependencies:

Required:
* `flask` -- Runs the webserver


Optional:
* `phue` -- Required to use Phillips Hue lights and bridges


The server listens for HTTP POST and GET requests to query and control different modules connected to the controller.
These requests are sent to \[server IP\]/modules. Commands are embedded in a json object inside the body of the message.
Below is an example JSON object:
```json
{"set" : [
   {
    "id"    : 0x4ab343cd,
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
"get : [
   {
    "id"    : 0x23e4abd4,
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
```json
{[{
    "class" : "DoorSensor",
    "name"  : "Back Door",
    "id"    : 0x4ab343cd,
    "attr"  : "open",
    "value" : false
   },
   {
    "class" : "HueLight",
    "name"  : "Dining Room 2",
    "id"    : 0x4ab353ad,
    "attr"  : "saturation",
    "value" : 30
   }
]}
```
