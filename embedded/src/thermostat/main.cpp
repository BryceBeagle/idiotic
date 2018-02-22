#include "idiotic_module.hpp"
#include "thermostat.hpp"

#define SERIAL_BAUD 115200

Idiotic_Module module("192.168.1.108:5000");
Thermostat thermostat(12, 14, 13);

void setup() {

    Serial.begin(SERIAL_BAUD);
    Serial.println("MCP9808 Init");

    module.connectWiFi("FlipTables", "visit umbrella find shame");

}

void loop() {

    // Create and populate Json object
    // http://arduinojson.org/assistant/ --> {"set":[{"temp":27.375}]}
    DynamicJsonBuffer jsonBuffer(JSON_ARRAY_SIZE(1) + 2*JSON_OBJECT_SIZE(1));
    JsonObject& setObject = jsonBuffer.createObject();
    JsonArray& setArray = setObject.createNestedArray("set");
    JsonObject& tempObj = setArray.createNestedObject();
//    tempObj["temp"] = temp;

    // Convert Json into String for printing and sending
    String buffer;
    setObject.printTo(buffer);

    // Print Json to Serial for debugging
    Serial.println(buffer);

    // Send Json as body of HTTP POST Request
    module.sendJson(buffer);

    delay(500);

}