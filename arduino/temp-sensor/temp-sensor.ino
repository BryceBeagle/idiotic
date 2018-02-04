
#include "Arduino.h"
#include "Adafruit_MCP9808.h"


Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();

void setup() {

    Serial.begin(9600);
    Serial.println("MCP9808");

    if (!tempsensor.begin(12, 13)) {
        Serial.println("Couldn't find MCP9808");
        while(1);
    }
    
//    Wire.begin(12, 13);
    
}

void loop() {

    float c = tempsensor.readTempC();
    float f = c * 9.0 / 5.0 + 32;
    Serial.print("Temp: "); Serial.print(c); Serial.print("*C\t"); 
    Serial.print(f); Serial.println("*F");

    
}
