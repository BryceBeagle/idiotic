#include "idiotic_module.hpp"

#ifndef SERIAL_BAUD
    #define SERIAL_BAUD 115200
#endif

int Idiotic_Module::connectWiFi(String ssid, String password) {

    this->ssid = ssid;
    this->_password = password;

    Serial.begin(SERIAL_BAUD);
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

int Idiotic_Module::addSendAttr(String attr_name, String attr_value) {

    // NOTE: attr_value does not get strings placed around it automatically.
    // To send a json string, put string characters inside passed String

    // TODO: Support https
    
    this->http.begin("http://" + this->hostname + "/modules/");
    this->http.addHeader("Content-Type", "application/json");

    String message = "{\"" + attr_name + "\" : " + attr_value + "}";

    int httpCode = this->http.POST(message);

    this->http.end();
    
    return httpCode;
    
}

int Idiotic_Module::sendAttrs() {
    
}

