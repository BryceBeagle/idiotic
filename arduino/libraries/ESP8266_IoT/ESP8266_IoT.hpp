#ifndef ESP8266_IoT_H
#define ESP8266_IoT_H

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>


class ESP8266_Module {

    public:

        String ssid;
        String host;
        String hostname;

        ESP8266_Module(String hostname) : hostname(hostname), http() {}
        
        int connectWiFi(String ssid, String password);
        int sendAttr(String attr_name, String attr_value);

    private:
    
        HTTPClient http;
        String _password;
    
};



#endif
