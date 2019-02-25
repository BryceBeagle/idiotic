#include "idiotic_module.hpp"

#define SERIAL_BAUD 115200

#define SERVER_ADDRESS "192.168.1.108"
#define SERVER_PORT 5000

#define PERIOD 2000  // 2 seconds

#define HALL_EFFECT_PIN 13

IdioticModule module("DoorSensor");

void setup() {

	Serial.begin(SERIAL_BAUD);
	module.connectWiFi();
	module.beginSocket(SERVER_ADDRESS, SERVER_PORT);

	module.funcs["door_open"] = IdioticModule::function_map{
			.get = [&] { return digitalRead(HALL_EFFECT_PIN); }
	};
}


void loop() {

	module.dataLoop();
	delay(PERIOD);

}
