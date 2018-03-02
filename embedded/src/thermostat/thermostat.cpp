#include <Arduino.h>
#include "thermostat.hpp"

Thermostat::Thermostat(uint8_t fan_pin, uint8_t ac_pin, uint8_t heat_pin) :
fan_pin(fan_pin), ac_pin(ac_pin), heat_pin(heat_pin) {

    // Turn off all pins during init
    digitalWrite(fan_pin , LOW);
    digitalWrite(ac_pin  , LOW);
    digitalWrite(heat_pin, LOW);
    active_device = kNone;
}

String Thermostat::get_active_device() {
    return String("Test");
//    return active_device;
}


void Thermostat::set_active_device(Device device) {

    // Turn on a device
    digitalWrite(fan_pin , device == kFan  ? HIGH : LOW);
    digitalWrite(ac_pin  , device == kAC   ? HIGH : LOW);
    digitalWrite(heat_pin, device == kHeat ? HIGH : LOW);
    active_device = device;
}

