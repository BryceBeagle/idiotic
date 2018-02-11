//#include <IRremoteESP8266.h>/
//#include <ESP8266WiFi.h>/

int inputPin  = 3;

uint32_t t0;

void setup() {

    Serial.begin(9600);
    pinMode(inputPin, INPUT_PULLUP);

    Serial.println("Starting");

}

void loop() {

    Serial.println("Starting");

    while(digitalRead(inputPin)) {}

    Serial.println("Signal detected");

    t0 = micros();

    while(!digitalRead(inputPin)) {}

    Serial.println("Duration: " + String(micros() - t0));

}
