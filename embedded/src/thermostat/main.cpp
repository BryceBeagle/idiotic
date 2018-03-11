#include "idiotic_module.hpp"
#include "thermostat.hpp"

#define SERIAL_BAUD 115200

#define WIFI_SSID "FlipTables"
#define WIFI_PASSWORD "visit umbrella find shame"

const char* kServerHost = "192.168.1.108";
const int   kServerPort = 5000;

IdioticModule module;
Thermostat thermostat(12, 14, 13);


void setup() {

    Serial.begin(SERIAL_BAUD);
    Serial.setDebugOutput(true);

    module.connectWiFi(WIFI_SSID, WIFI_PASSWORD);

    module.beginSocket(kServerHost, kServerPort);

    module.funcs["active_device"] = {
            .get = [&]() {return thermostat.get_active_device().c_str();}
    };

}


void loop() {
    module.socketLoop();
}