#ifndef THERMOSTAT_H
#define THERMOSTAT_H

class Thermostat {

    public:

        uint8_t fan_pin, ac_pin, heat_pin;

        Thermostat(uint8_t fan_pin, uint8_t ac_pin, uint8_t heat_pin);

        enum Device {kNone, kFan, kAC, kHeat};
        Device active_device = kNone;

        void set_active_device(Device device);
        Device get_active_device();

};

#endif // THERMOSTAT_H
