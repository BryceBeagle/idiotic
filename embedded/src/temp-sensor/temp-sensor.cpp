#include <Arduino.h>

#include "Adafruit_MCP9808.h"
#include "idiotic_module.hpp"

#define SERIAL_BAUD 115200

const char* kServerHost = "192.168.1.182";
const int   kServerPort = 5000;

IdioticModule module("TempSensor");
Adafruit_MCP9808 tempsensor;

void setup() {

    Serial.begin(SERIAL_BAUD);

	module.connectWiFi();
    module.beginSocket(kServerHost, kServerPort);

    tempsensor.begin(13, 12, 0x18);

    module.funcs["temp"] = IdioticModule::function_map {
            .get = [&] {return tempsensor.readTempC();}
    };
}


void loop() {

    module.dataLoop();

    delay(2000);

}
