#include <ArduinoJson.h>
#include <Arduino.h>

#include "idiotic_module.hpp"

#ifndef SERIAL_BAUD
    #define SERIAL_BAUD 115200
#endif


void IdioticModule::connectWiFi(String ssid, String password, String hostname) {

    WiFi.hostname(hostname);
    connectWiFi(ssid, password);

}


void IdioticModule::connectWiFi(String ssid, String password) {

    this->ssid = ssid;
    this->_password = password;

    Serial.begin(SERIAL_BAUD);  // TODO: Serial only during a debug mode
    WiFi.begin(ssid.c_str(), password.c_str());

    // Connect to WiFi network
    Serial.print("Connecting to ");
    Serial.println(ssid);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi connected");

}


void IdioticModule::sendJson(String &buffer) {

//    // TODO: Support https
//
//    HTTPClient* http = new HTTPClient();
//
//    http->begin("http://" + hostname + port + "/modules");
//    http->addHeader("Content-Type", "application/json");
//
//    int httpCode = http->POST(buffer);
//    http->end();
//
//    return httpCode;

    Serial.println("Sending: 42[\"json\"," + buffer + "]");
    _web_socket->sendTXT("42[\"json\"," + buffer + "]");

}


void IdioticModule::dataLoop() {

    if (_socket_is_connected) {

        int num_entries = funcs.size();
        DynamicJsonBuffer jsonBuffer(JSON_ARRAY_SIZE(num_entries)
                                     + (num_entries + 1) * JSON_OBJECT_SIZE(1));
        JsonObject &setObject = jsonBuffer.createObject();
        JsonArray &setArray = setObject.createNestedArray("set");

        std::map < String, std::function < JsonVariant() >> ::iterator
        it;

        for (it = funcs.begin(); it != funcs.end(); it++) {
            JsonObject &tempObj = setArray.createNestedObject();
            tempObj[it->first] = it->second();
        }

        // Convert Json into String for printing and sending
        String buffer;
        setObject.printTo(buffer);

        // Print Json to Serial for debugging
        //    Serial.println(buffer);

        // Send Json as body of HTTP POST Request
        sendJson(buffer);

    }

    else {
        Serial.println("Socket not connected. Retrying");
    }

}

void testCallback(WStype_t type, uint8_t *payload, size_t length) {

    switch (type) {

        case WStype_DISCONNECTED: {
            Serial.printf("[WSc] Disconnected!\n");
            break;
        }
        case WStype_CONNECTED: {
            Serial.printf("[WSc] Connected to url: %s\n", payload);
            break;
        }
        case WStype_TEXT: {
            Serial.printf("[WSc] Payload received: %s\n", payload);
            break;
        }
        default: {
            Serial.printf("[WSc] Unexpected payload type: %s\n", payload);
        }
    }

}



void IdioticModule::beginSocket(String host, uint16_t port) {

    _web_socket = new WebSocketsClient;
    _web_socket->beginSocketIO(host, port);

    delay(5000);

//    _web_socket->onEvent(testCallback);
    _web_socket->onEvent(std::bind(&IdioticModule::_handleSocketRequest, this,
                                   std::placeholders::_1,
                                   std::placeholders::_2,
                                   std::placeholders::_3));
}


void IdioticModule::socketLoop() {

//    _web_socket->loop();

    if (_socket_is_connected) {

        // TODO: Is this necessary with the messages being sent?
        // Send heartbeat
        uint64_t now = millis();
        if ((now - _last_heartbeat) > WEB_SOCKET_HEARTBEAT) {
            _last_heartbeat = now;
            _web_socket->sendTXT("2");
        }
    }
}


void IdioticModule::_handleSocketRequest(WStype_t type, uint8_t *payload, size_t length) {

    switch (type) {

        case WStype_DISCONNECTED: {
            Serial.printf("[WSc] Disconnected!\n");
            _socket_is_connected = false;
            break;
        }
        case WStype_CONNECTED: {
            Serial.printf("[WSc] Connected to url: %s\n", payload);
            _socket_is_connected = true;
            break;
        }
        case WStype_TEXT: {
            Serial.printf("[WSc] Payload received: %s\n", payload);
            break;
        }
        default: {
            Serial.printf("[WSc] Unexpected payload type: %s\n", payload);
        }
    }
}
