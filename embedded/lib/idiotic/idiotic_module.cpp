#include <ArduinoJson.h>
#include <Arduino.h>
#include <WiFiManager.h>

#include "idiotic_module.hpp"
#include "idiotic_json_variant.h"

#ifndef SERIAL_BAUD
#define SERIAL_BAUD 115200
#endif


void IdioticModule::connectWiFi() {

	WiFiManager wifiManager;

	wifiManager.setAPCallback([](WiFiManager *myWiFiManager) {
		Serial.print("AP SSID: ");
		Serial.println(myWiFiManager->getConfigPortalSSID());
	});

	if (!wifiManager.autoConnect()) {
		// This should never trigger as we're not using a timeout

		Serial.println("failed to connect and hit timeout");
		//reset and try again, or maybe put it to deep sleep
		ESP.reset();
		delay(1000);
	}

	Serial.print("Connected to ");
	Serial.println(WiFi.SSID());

}


void IdioticModule::connectWiFi(String ssid, String password) {

	// Connect to WiFi network
	Serial.println("");
	Serial.print("Connecting to ");
	Serial.println(ssid);

	WiFi.begin(ssid.c_str(), password.c_str());

	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print("!.!");
	}
	Serial.println("");
	Serial.println("WiFi connected");

}


void IdioticModule::beginSocket(String host, uint16_t port) {

	_web_socket = new WebSocketsClient;
	_web_socket->begin(host, port, "/embedded");

	_web_socket->onEvent(std::bind(&IdioticModule::_handleSocketEvent, this,
	                               std::placeholders::_1,
	                               std::placeholders::_2,
	                               std::placeholders::_3));

	_web_socket->setReconnectInterval(5000);

}


void IdioticModule::_handleSocketEvent(WStype_t type,
                                       uint8_t *payload,
                                       size_t length) {

	switch (type) {

		case WStype_DISCONNECTED: {
			Serial.printf("[WSc] Disconnected!\n");
			_socket_is_connected = false;
			break;
		}
		case WStype_CONNECTED: {
			Serial.printf("[WSc] Connected to url: %s\n", payload);
			_socket_is_connected = true;

			_sendHelloMessage();

			break;
		}
		case WStype_TEXT: {
			Serial.printf("[WSc] Payload received: %s\n", payload);
			_parsePayload((char *) payload);
			break;
		}
		default: {
			Serial.printf("[WSc] Unexpected payload type: %s\n", payload);
		}
	}
}


void IdioticModule::_sendHelloMessage() {

	if (uuid = "") {
		uuid = WiFi.softAPmacAddress();
	}

	// 100 is a buffer for the string copying. Not too concerned with wasted mem
	DynamicJsonDocument jsonDocument(JSON_OBJECT_SIZE(3) + 100);

	jsonDocument["hello"] = 0;  // Value doesn't matter and shouldn't be used
	jsonDocument["uuid"] = uuid;
	jsonDocument["class"] = class_type;

	// Convert Json into String for printing and sending
	String buffer;
	serializeJson(jsonDocument, buffer);

	_web_socket->sendTXT(buffer);

}

void IdioticModule::dataLoop() {

	if (_socket_is_connected) {

		int num_entries = funcs.size(); // TODO: Only size of entries with .get

		// 100 is a buffer for the string copying. Not too concerned with wasted mem
		DynamicJsonDocument jsonDocument(JSON_OBJECT_SIZE(3)
		                                 + JSON_OBJECT_SIZE(num_entries)
		                                 + 100);

		jsonDocument["uuid"] = uuid;
		jsonDocument["class"] = class_type;

		JsonObject setObject = jsonDocument.createNestedObject("update");

		std::map<String, function_map>::iterator it;
		for (it = funcs.begin(); it != funcs.end(); it++) {

			if (it->second.get != nullptr) {

				IdioticJsonVariant idioticVariant = it->second.get();
				String updateKey = it->first;

                JsonVariant jsonVariant;
                switch (idioticVariant.variantType) {
                    case IdioticJsonVariant::BOOL: {
	                    setObject[updateKey] = idioticVariant.variant.asBool;
	                    break;
                    }
                    case IdioticJsonVariant::DOUBLE: {
	                    setObject[updateKey] = idioticVariant.variant.asDouble;
	                    break;
                    }
                    case IdioticJsonVariant::INTEGER: {
	                    setObject[updateKey] = idioticVariant.variant.asInteger;
	                    break;
                    }
                    case IdioticJsonVariant::STRING: {
	                    setObject[updateKey] = idioticVariant.variant.asString;
	                    break;
                    }
                    default:
                        // TODO: FIXME
                        break;
                }
			}
		}

		// Convert Json into String for printing and sending
		String buffer;
		serializeJson(jsonDocument, buffer);

		// Print Json to Serial for debugging
		Serial.println(buffer);

		// Send Json using socket
		_web_socket->sendTXT(buffer);

	} else {
		Serial.println("Socket not connected. Retrying");
	}
}

void IdioticModule::_parsePayload(char *payload) {

	DynamicJsonDocument parseDocument(2 * JSON_OBJECT_SIZE(1) + 20);
	deserializeJson(parseDocument, payload);

	JsonObject behaviors = parseDocument["behavior"];
	if (!behaviors.isNull()) {
		for (JsonObject::iterator i = behaviors.begin(); i != behaviors.end(); ++i) {
			// TODO
//			funcs[i->key].behavior(i->value.as<char *>());
		}
	}

//	if (parseDocument.containsKey("get")) {
//		// TODO
//	}

}