#ifndef ESP8266_IDIOTIC_H
#define ESP8266_IDIOTIC_H

#include <vector>
#include <map>

#include <Ticker.h>

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <Arduino.h>

#include <WebSocketsClient.h>


class IdioticModule {

    public:

        String ssid, hostname, port;
        String class_type;
        String uuid;

        IdioticModule(String class_type): class_type(class_type) {}

        void connectWiFi(String ssid, String password, String hostname);
        void connectWiFi(String ssid, String password);

        void beginSocket(String host, uint16_t port);

        typedef struct {
            std::function<JsonVariant()> get;
            std::function<void()> set;
            std::function<void()> action;
        } function_map;

        // Map is used for a number of reasons:
        //    Server can request the value of a key, and module knows what to run
        //        to get it
        //    Module can iterate over map and populate and send a Json object with
        //        keys mapped to values
        std::map<String, function_map> funcs;
        void dataLoop();

        const char *get_name();
        void set_name();
        const char *get_class();
        void set_class();

    private:

        WebSocketsClient *_web_socket;
        bool _socket_is_connected = false;
        uint64_t _last_heartbeat = 0;

        String _password;

        void _handleSocketEvent(WStype_t type, uint8_t *payload, size_t length);
        void _send_hello_message();

};


#endif // ESP8266_IDIOTIC_H
