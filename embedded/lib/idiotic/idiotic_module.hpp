#ifndef ESP8266_IoT_H
#define ESP8266_IoT_H

#include <vector>
#include <map>

#include <Ticker.h>

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <Arduino.h>

#include <WebSocketsClient.h>


#define WEB_SOCKET_HEARTBEAT 25000


class IdioticModule {

    public:

        String ssid, hostname, port;

        IdioticModule() {};

        void connectWiFi(String ssid, String password, String hostname);
        void connectWiFi(String ssid, String password);

        void beginSocket(String host, uint16_t port);
        void socketLoop();

        // Map is used for a number of reasons:
        //    Server can request the value of a key, and module knows what to run
        //        to get it
        //    Module can iterate over map and populate and send a Json object with
        //        keys mapped to values
        std::map<String, std::function<JsonVariant()>> funcs;
        void dataLoop();
        void sendJson(String &buffer);

    private:

        WebSocketsClient *_web_socket;
        bool _socket_is_connected = false;
        uint64_t _last_heartbeat = 0;

        String _password;

        void _handleSocketRequest(WStype_t type, uint8_t * payload, size_t length);

};


#endif // THERMOSTAT_H
