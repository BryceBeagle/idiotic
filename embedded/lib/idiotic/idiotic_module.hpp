#ifndef ESP8266_IoT_H
#define ESP8266_IoT_H

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include <Arduino.h>  // Works fine

class Idiotic_Module {

    public:

        String ssid;
        String host;
        String hostname;

        Idiotic_Module(String hostname) : hostname(hostname), http() {}

        int connectWiFi(String ssid, String password);
        int sendJson(String &buffer);

    private:

        HTTPClient http;
        String _password;

};

#endif // THERMOSTAT_H
