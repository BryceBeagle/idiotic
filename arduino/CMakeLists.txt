cmake_minimum_required(VERSION 3.9.6)
project(IotHouse)

add_subdirectory(libraries/ESP8266_IoT)
add_subdirectory(libraries/ESP8266WiFi)
add_subdirectory(temp-sensor)

#add_custom_target(temp-sensor DEPENDS )