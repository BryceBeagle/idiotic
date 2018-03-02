#include "idiotic_module.hpp"
#include "thermostat.hpp"

#define SERIAL_BAUD 115200

#define WIFI_SSID "FlipTables"
#define WIFI_PASSWORD "visit umbrella find shame"

const String kServerHost = "192.168.1.108";
const String kServerPort = ":5000";

IdioticModule module(kServerHost + kServerPort);
Thermostat thermostat(12, 14, 13);



void setup() {

    Serial.begin(SERIAL_BAUD);

    module.connectWiFi(WIFI_SSID, WIFI_PASSWORD);

    module.funcs["active_device"] = [&]() -> JsonVariant {thermostat.get_active_device();};

    module.begin(5000);

}


void loop() {
}