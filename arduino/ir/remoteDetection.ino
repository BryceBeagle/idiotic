#include <IRremoteESP8266.h>
#include <ESP8266WiFi.h>

const char* ssid = "FlipTables";
const char* password = "visit umbrella find shame";
const char* host = "192.168.1.100";

String mac = "xxxx";

int inputPin = 13;
WiFiClient client;

IRrecv irrecv(inputPin);
decode_results signals;

void setup() {

    Serial.begin(9600);
    irrecv.enableIRIn();

}

void loop() {
  
    if (irrecv.decode(&signals)) {
        Serial.println(signals.value, HEX);
        irrecv.resume();
    }
    delay(100);

}
