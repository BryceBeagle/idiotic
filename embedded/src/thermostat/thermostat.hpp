#pragma once

class Thermostat {

    public:

        uint8_t fan_pin, ac_pin, heat_pin;

        Thermostat(uint8_t fan_pin, uint8_t ac_pin, uint8_t heat_pin);

        enum Device {kNone, kFan, kAC, kHeat};
        Device active_device = kNone;

        void setMode(Device device);
        Device getMode();

};
