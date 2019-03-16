#include <Arduino.h>

#include "Adafruit_TSL2591.h"
#include "Adafruit_MCP9808.h"
#include "idiotic_module.hpp"

#define SERIAL_BAUD 115200

const char *kServerHost = "192.168.1.182";
const int kServerPort = 5000;

IdioticModule module("Gardenometer");
Adafruit_MCP9808 tempSensor;
Adafruit_TSL2591 lightSensor(2591);


void setup() {
    Serial.begin(SERIAL_BAUD);

    module.connectWiFi();
    module.beginSocket(kServerHost, kServerPort);

    tempSensor.begin(13, 12, 0x18);

    if (!lightSensor.begin()) {
        Serial.println("Light sensor not found");
        while (1);
    }

    sensor_t sensor;
    lightSensor.getSensor(&sensor);
    Serial.println(F("------------------------------------"));
    Serial.print(F("Sensor:       "));
    Serial.println(sensor.name);
    Serial.print(F("Driver Ver:   "));
    Serial.println(sensor.version);
    Serial.print(F("Unique ID:    "));
    Serial.println(sensor.sensor_id);
    Serial.print(F("Max Value:    "));
    Serial.print(sensor.max_value);
    Serial.println(F(" lux"));
    Serial.print(F("Min Value:    "));
    Serial.print(sensor.min_value);
    Serial.println(F(" lux"));
    Serial.print(F("Resolution:   "));
    Serial.print(sensor.resolution, 4);
    Serial.println(F(" lux"));
    Serial.println(F("------------------------------------"));
    Serial.println(F(""));

    // Set the gain to low for outside use
    lightSensor.setGain(TSL2591_GAIN_LOW);

    module.funcs["temp"] = IdioticModule::function_map{
            .get = [&] {
                return tempSensor.readTempC();
            }
    };
    module.funcs["lux"] = IdioticModule::function_map{
            .get = [&] {
                uint16_t bothChannels = lightSensor.getLuminosity(TSL2591_VISIBLE);
                uint16_t infrared = lightSensor.getLuminosity(TSL2591_INFRARED);

                return lightSensor.calculateLux(bothChannels, infrared);
            }
    };
}

void loop() {
    module.dataLoop();

    delay(2000);
}
