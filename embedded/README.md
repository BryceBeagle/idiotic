# Introduction
Each module is built on top of the ESP8266 embedded platform. All devices connect to a local network and communicate with the `idiotic-server`. Json is tranferred using HTTP Requests and can be used to instruct a device to perform and action or respond with information. 

To aid in simplicity, familiarity and library support, the [Arduino core](https://github.com/esp8266/Arduino "Arduino core") is used. This allows easy programming in C++ with access to a number of convient libraries such as Serial, Wire (TWI/I2C), and Servo.

The [ESP8266WiFi library](https://github.com/esp8266/Arduino/tree/master/libraries/ESP8266WiFi "ESP8266WiFi library") is used to connect the module to a local WiFi network. It's very easy to setup, requiring a single method call with the SSID and password.

Json data structures are  [ArduinoJson library](https://github.com/bblanchon/ArduinoJson "ArduinoJson library"). It provides an easy method of constructing Json data structures that can be turned into strings and sent. 

# Creating your own
It is recommended to use PlatformIO toolchain for development and deployment of software to the ESP8266.

1. If you are developing a new device, create a new directory under `$idiotic/embedded/src` with the name of your device
2. Create a new `.cpp` source file in that directory and open it for editing
3. Import `idiotic_module.hpp` to acquire the base IdioticModule class and its functionality
4. Create an instance of `IdioticModule`, passing the device type as a string.

    Note: This string must exactly match the class name of the corresponding device driver
5. In the setup() function:
    1. Connect the module to WiFi using `IdioticModule::connectWiFi()`
    2. Begin the connection to the Idiotic server using `IdioticModule::beginSocket()`
    3. Populate the `Idiotic::funcs` map with attribute set and get functions using `IdioticModule::function_map`
    structs. The key for each item in the map is the attribute name.

    Note:
    * Each key must have an exact match in the corresponding device driver as either an attribute or a behavior
    * The `.get` function supports lambda expressions, but for an unknown technical reason, I was unable to get this
    working for the `.set` function. As a result, only function pointers are accepted. If a class method is required,
    use `std::bind` for now.
    4. If serial debug output is desired, use `Serial.setDebugOutput(true)`
6. In the loop() function:
    1. Run the dataloop using `IdioticModule::dataLoop()`
    2. Delay the thread to for an amount of time to meet a desired period using `delay()`
