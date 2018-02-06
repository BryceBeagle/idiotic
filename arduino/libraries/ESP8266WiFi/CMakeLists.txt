file(GLOB library_src "src/*.cpp")
file(GLOB header_src "src/*.h")

#include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)

MESSAGE(STATUS ${library_src})
MESSAGE(STATUS ${header_src})

add_library(ESP8266WiFi ${library_src} ${header_src})
target_include_directories(ESP8266WiFi PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})