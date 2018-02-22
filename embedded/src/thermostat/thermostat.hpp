#ifndef THERMOSTAT_H
#define THERMOSTAT_H

class Thermostat {

    public:

        uint8_t fan_pin, ac_pin, heat_pin;

        Thermostat(uint8_t fan_pin, uint8_t ac_pin, uint8_t heat_pin);

        enum Device {kFan, kAC, kHeat};
        enum State {kOff, kOn};

        State fan_state = kOff;
        State ac_state = kOff;
        State heat_state = kOff; // When heat is on, fan is on

        void set_state(Device device, State state);
        State get_state(Device device);

};

#endif // THERMOSTAT_H
