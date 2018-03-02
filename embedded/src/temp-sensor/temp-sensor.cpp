#include "Arduino.h"
#include "Adafruit_MCP9808.h"
#include "idiotic_module.hpp"

#define SERIAL_BAUD 115200

#define WIFI_SSID "FlipTables"
#define WIFI_PASSWORD "visit umbrella find shame"

const char* kServerHost = "192.168.1.108";
const int   kServerPort = 5000;

IdioticModule module;
Adafruit_MCP9808 tempsensor;

void setup() {

    Serial.begin(SERIAL_BAUD);
    Serial.setDebugOutput(true);
    module.connectWiFi(WIFI_SSID, WIFI_PASSWORD);

    module.beginSocket(kServerHost, kServerPort);

    tempsensor.begin(12, 13);

    module.funcs["temp"] = [&]() {return tempsensor.readTempC();};

}


void loop() {

//    module.socketLoop();
//    module.dataLoop();

}
