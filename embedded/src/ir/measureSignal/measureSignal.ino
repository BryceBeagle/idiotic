//#include <IRremoteESP8266.h>/
//#include <ESP8266WiFi.h>/

int inputPin  = 3;

void setup() {

    Serial.begin(9600);
    pinMode(inputPin, INPUT);

    Serial.println("Starting");

}

void loop() {

    uint32_t times[100] = {};   
    int currentState = 0;

    while(digitalRead(inputPin)) {}

    Serial.println("Signal detected");

    uint32_t t1 = 0;
    uint32_t dt = 0;

    int i = 0;

    // TODO: Don't crash if something breaks and times[] is overflowed
    while(true) {

        uint32_t t0 = micros();

        while(!digitalRead(inputPin)) {}  // Wait for current dip to rise (signal is active low)
        while( digitalRead(inputPin)) {   // Wait for next dip
            if(micros() - t0 > 100000) {  // 100000 us should be more than enough to determine if signal is done
              goto finish;
            }
        }
        times[i++] = micros() - t0;
    }
    finish:


    for (int j = 0; j < i; j++) {
      Serial.print(String(times[j]) + " ");
    }
    Serial.println();

}
