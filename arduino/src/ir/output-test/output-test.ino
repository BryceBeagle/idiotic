int outputPin = 2;

uint32_t t0;

void setup() {

    Serial.begin(9600);
    pinMode(outputPin, OUTPUT);

    Serial.println("Starting");

}

void loop() {

    for (int i = 0; i < 10; i++) {
        digitalWrite(outputPin, HIGH);
        delayMicroseconds(1000);
        digitalWrite(outputPin, LOW);
        delayMicroseconds(1000);
    }
    delay(100);

}
