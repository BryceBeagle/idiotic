
# Introduction
Module that acts as a replacement/attachment to a household thermostat

# Background
A standard thermostat attaches to a number of wires that lead to the HVAC system. These wires typically run at ~24 VAC and are usually color coded. The ones we need to worry about are:

|  Marking | Wire Color  | Purpose  |
| :------------ | :------------ | :------------ |
| R  | Red  | 24 VAC  |
| G  | Green  | Fan Relay  |
| W  | White  | Heat Relay  |
| Y  | Yellow  | AC Relay   |

If your current thermostat has a heat anticipator -- [TODO]

# Functionality


# Parts List

# Appendix

**Choosing a current limiting resistor between the ESP and relays**

See [here](https://electronics.stackexchange.com/a/16219/163386 "here") for a great description on how to read the datasheet for a Solid State Relay.

|   |   |
| - | - |
| ESP Supply Voltage  | 3.3 V  |
| SSR LED Voltage Drop  | 1.2 V  |
| Desired SSR Current | 1 mA |

