
#include "Arduino.h"
#include "Adafruit_MCP9808.h"
#include "ESP8266_IoT.hpp"

Adafruit_MCP9808 tempsensor;
ESP8266_Module module("192.168.1.108:5000");

void setup() {

    Serial.begin(115200);
    Serial.println("MCP9808 Init");

    module.connectWiFi("FlipTables", "visit umbrella find shame");

    if (!tempsensor.begin(12, 13)) {
        Serial.println("Couldn't find MCP9808");
        while(1);
    }
    
}

void loop() {

    float temp = tempsensor.readTempC();
    Serial.print(String(temp));
    module.sendAttr("temperature", String(temp));
    Serial.println(" (sent)");
    delay(500);

}
