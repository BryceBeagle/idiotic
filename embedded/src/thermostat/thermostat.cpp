#include <Arduino.h>
#include "thermostat.hpp"

Thermostat::Thermostat(uint8_t fan_pin, uint8_t ac_pin, uint8_t heat_pin) :
        fan_pin(fan_pin), ac_pin(ac_pin), heat_pin(heat_pin) {

    pinMode(fan_pin, OUTPUT);
    digitalWrite(fan_pin, kOff);

    pinMode(ac_pin, OUTPUT);
    digitalWrite(ac_pin, kOff);

    pinMode(heat_pin, OUTPUT);
    digitalWrite(heat_pin, kOff);

}

Thermostat::State Thermostat::get_state(Device device) {
    switch (device) {
        case kFan : return (State) digitalRead(fan_pin);
        case kAC : return (State) digitalRead(ac_pin);
        case kHeat : return (State) digitalRead(heat_pin);
    }
}

void Thermostat::set_state(Device device, State state) {
    switch (device) {
        case kFan :
            fan_state = state;
            digitalWrite(fan_pin, state);
        case kAC :
            ac_state = state;
            digitalWrite(ac_pin, state);
        case kHeat :
            heat_state = state;
            digitalWrite(heat_pin, state);
    }
}
