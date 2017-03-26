#include <ESP8266WiFiAP.h>
#include <ESP8266WiFiSTA.h>
#include <WiFiClientSecure.h>
#include <ESP8266WiFiScan.h>
#include <ESP8266WiFiMulti.h>
#include <WiFiUdp.h>
#include <WiFiClient.h>
#include <WiFiServer.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiGeneric.h>
#include <ESP8266WiFiType.h>

#include <ESP8266wifi.h>

const char* ssid = "FlipTables";
const char* password = "visit umbrella find shame";
const char* host = "192.168.1.100";

String mac = "xxxx";

int inPin = 13;

int doorStatus = 0;

WiFiClient client;

void alarmRequest(String statusVal) {
  if (client.connect(host, 80)) {

    Serial.println("Connected to server"); 
  
    String URI = String("/alarm?id=") + mac + "&status=" + statusVal;
    
    // Make a HTTP request
    client.println("GET " + URI + " HTTP/1.1");
    client.println("Host: " + String(host));
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Unable to connect to server");
  }
}

void setup() {

//  WiFi.macAddress(mac);
  
  Serial.begin(115200);
  delay(10);

  // prepare LED pin
  pinMode(inPin, INPUT);
  digitalWrite(2, 0);
  
  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Print the IP address
  Serial.println(WiFi.localIP());

  Serial.println("Using pin " + inPin);
  
}

void loop() {

  if (doorStatus == 0  && digitalRead(inPin) == 0) {
    Serial.println("Door Opened");
    doorStatus = 1;
    alarmRequest("open");
  } else if (doorStatus == 1  && digitalRead(inPin) == 1) {
    Serial.println("Door Closed");
    doorStatus = 0;
    alarmRequest("closed");
  }
}

