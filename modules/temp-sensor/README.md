**Description**

Module that measures and reports temperature.

The MCP9808 sensor is functional from -40°C ~ 125°C with an accuracy of ±0.5°C. The ESP8266 communicates with the sensor
using I2C (TWI). Temperature is measured every 30 seconds and a 5 minute rolling average is reported to the server every
30 seconds.

Temperature is reported in the following JSON format:
```json
{"temp" : "20.5"}
```

**Parts List**

| Purpose             | Component(s)                        | Purchase Link                                |
|---------------------|-------------------------------------|----------------------------------------------|
| Microcontroller     | ESP8266-07 or ESP8266-12E/F/S       | [Link](https://www.adafruit.com/product/2491)|
| Temp Sensor         | MCP9808 in 8-MPOS package           | [Link](https://www.digikey.com/short/q8143w) |
| SMD Female MicroUSB | 609-4613-1-ND                       | [Link](https://www.digikey.com/short/q81438) |
| 3.3 V Voltage Reg   | AZ1117E in SOT-223 package          | [Link](https://www.digikey.com/short/q81489) |
| VReg Caps           | 2 × 1 μF capacitors in 0805 package |                                              |

