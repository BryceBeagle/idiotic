#file(GLOB libraries RELATIVE "libraries" "*.cpp" "*.h")

add_executable(temp-sensor temp-sensor.cpp)
target_link_libraries(temp-sensor LINK_PUBLIC ESP8266_IoT)
target_link_libraries(temp-sensor LINK_PUBLIC ESP8266WiFi)