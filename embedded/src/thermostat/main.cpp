#include "idiotic_module.hpp"
#include "thermostat.hpp"

// Debug Serial
#define SERIAL_BAUD 115200

// Idiotic
#define SERVER_HOST "192.168.1.108"
#define SERVER_PORT 5000
IdioticModule module("Thermostat");

// Thermostat
Thermostat thermostat(12, 14, 13);

// Forward declarations
void setThermostatMode(const char *);
const char *getThermostatMode();

// Setup function
void setup() {

    Serial.begin(SERIAL_BAUD);
    module.connectWiFi();

    module.beginSocket(SERVER_HOST, SERVER_PORT);

    // Functions use to set or get thermostat mode
    module.funcs["mode"] = IdioticModule::function_map {
            .get = &getThermostatMode,
            .set = &setThermostatMode
    };
}

// Looping function
void loop() {
    //  Iterate over all functions and send result of .get functions to server
    module.dataLoop();
    delay(2000);
}

// Change which mode thermostat is set to
void setThermostatMode(const char *mode) {

    if (!strcasecmp(mode, "ac"  )) thermostat.setMode(Thermostat::kAC);
    if (!strcasecmp(mode, "fan" )) thermostat.setMode(Thermostat::kFan);
    if (!strcasecmp(mode, "heat")) thermostat.setMode(Thermostat::kHeat);
    if (!strcasecmp(mode, "none")) thermostat.setMode(Thermostat::kNone);

}

// Retrieve current thermostat mode
const char *getThermostatMode() {

    switch (thermostat.getMode()) {
        case Thermostat::kAC  : return "ac"  ;
        case Thermostat::kFan : return "fan" ;
        case Thermostat::kHeat: return "heat";
        case Thermostat::kNone: return "none";
    }
}