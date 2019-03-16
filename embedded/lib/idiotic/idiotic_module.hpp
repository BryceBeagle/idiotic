#pragma once

#include <vector>
#include <map>

#include <Ticker.h>

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <Arduino.h>

#include <WebSocketsClient.h>

#include "idiotic_json_variant.h"


class IdioticModule {

    public:

        String class_type;
        String uuid;

        IdioticModule(String class_type): class_type(class_type) {}

        static void connectWiFi();
        static void connectWiFi(String ssid, String password);

        void beginSocket(String host, uint16_t port);

        // TODO: use implicit null field init to somehow avoid
        // "sorry, unimplemented: non-trivial designated initializers not
        // supported"
        typedef struct {
            std::function<IdioticJsonVariant()> get;
            std::function<void(IdioticJsonVariant)> set;
            std::function<void(String)> behavior;
        } function_map;

        // Map is used for a number of reasons:
        //    Server can request the value of a key, and module knows what to run
        //        to get it
        //    Module can iterate over map and populate and send a Json object with
        //        keys mapped to values
        std::map<String, function_map> funcs;
        void dataLoop();

    private:

        WebSocketsClient *_web_socket = nullptr;
        bool _socket_is_connected = false;
        uint64_t _last_heartbeat = 0;

        String _password;

        void _handleSocketEvent(WStype_t type, uint8_t *payload,
                                size_t length);
        void _sendHelloMessage();

        void _parsePayload(char *payload);

};
