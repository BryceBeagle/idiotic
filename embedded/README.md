# Introduction
Each module is built on top of the ESP8266 embedded platform. All devices connect to a local network and communicate with the `idiotic-server`. Json is tranferred using HTTP Requests and can be used to instruct a device to perform and action or respond with information. 

To aid in simplicity, familiarity and library support, the [Arduino core](https://github.com/esp8266/Arduino "Arduino core") is used. This allows easy programming in C++ with access to a number of convient libraries such as Serial, Wire (TWI/I2C), and Servo.

The [ESP8266WiFi library](https://github.com/esp8266/Arduino/tree/master/libraries/ESP8266WiFi "ESP8266WiFi library") is used to connect the module to a local WiFi network. It's very easy to setup, requiring a single method call with the SSID and password.

Json data structures are  [ArduinoJson library](https://github.com/bblanchon/ArduinoJson "ArduinoJson library"). It provides an easy method of constructing Json data structures that can be turned into strings and sent. 

# Creating your own
It is recommended to use PlatformIO toolchain for development and deployment of software to the ESP8266.

1. From within the `idiotic/embedded` (`$EMBEDDED`) directory, initialize Platformio for your editor/IDE of choice by following [these instructions](http://docs.platformio.org/en/latest/userguide/cmd_init.html "these instructions")
2. Create a new directory under `$EMBEDDED/src` with the name of your device.
3. Create a new `.cpp` file inside that directory that will serve as the main file of the program.
4. Edit the $EMBEDDED/platformio.init and change `src_dir` to match the src directory that you just created. Paths are relative to `$EMBEDDED`.