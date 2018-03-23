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
            _parsePayload((char *)payload);
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

    DynamicJsonBuffer jsonBuffer(JSON_OBJECT_SIZE(3));
    JsonObject &helloObject = jsonBuffer.createObject();
    helloObject["hello"] = 0;  // Value doesn't matter and shouldn't be used
    helloObject["class"] = class_type;
    helloObject["uuid"] = uuid;

    // Convert Json into String for printing and sending
    String buffer;
    helloObject.printTo(buffer);

    // Print Json to Serial for debugging
    Serial.println(buffer);

    _web_socket->sendTXT(buffer);

}

void IdioticModule::dataLoop() {

    if (_socket_is_connected) {

        int num_entries = funcs.size(); // TODO: Only size of entries with .get

        DynamicJsonBuffer jsonBuffer(JSON_OBJECT_SIZE(3)
                                     + JSON_OBJECT_SIZE(num_entries));
        JsonObject &root = jsonBuffer.createObject();

        root["uuid"] = uuid;
        root["class"] = class_type;

        JsonObject &setObject = root.createNestedObject("update");

        std::map<String, function_map>::iterator it;
        for (it = funcs.begin(); it != funcs.end(); it++) {

            if (it->second.get != nullptr) {
                setObject[it->first] = it->second.get();
            }
        }

        // Convert Json into String for printing and sending
        String buffer;
        root.printTo(buffer);

        // Print Json to Serial for debugging
        Serial.println(buffer);

        // Send Json using socket
        _web_socket->sendTXT(buffer);

    }

    else {
        Serial.println("Socket not connected. Retrying");
    }
}

void IdioticModule::_parsePayload(char *payload) {

    DynamicJsonBuffer parseBuffer(2*JSON_OBJECT_SIZE(1) + 20);
    JsonObject &root = parseBuffer.parseObject(payload);

    if (root.containsKey("behavior")) {
        JsonObject &behaviors = root["behavior"];
        for (JsonObject::iterator i = behaviors.begin();i != behaviors.end();
             ++i) {
            funcs[i->key].behavior(i->value.as<char *>());
        }
    }
    if (root.containsKey("get")) {
        // TODO
    }

}