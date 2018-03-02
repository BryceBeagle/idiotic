#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "FlipTables";
const char* password = "visit umbrella find shame";
//const char* host = "brycebeagle.com";  // AWS
const char* host = "192.168.1.108:5000"; // griefcake

String mac = "xxxx";

int inPin = 13;

int doorStatus = 0;

WiFiClient client;
HTTPClient http;

void alarmRequest(String statusVal) {

    HTTPClient http;

    Serial.println("TEST");

    http.begin("http://" + String(host) + "/modules/door");
    http.addHeader("Content-Type", "application/json");
    
    String message = "{\"status\":\"" + String(statusVal) + "\"}";
    
    int httpCode = http.POST(message);

    Serial.println(httpCode);

    http.end();
}

void setup() {

//  WiFi.macAddress(mac);
  
  Serial.begin(115200);
  delay(10);

  // prepare LED pin
  pinMode(inPin, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
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
    digitalWrite(LED_BUILTIN, LOW);
  } else if (doorStatus == 1  && digitalRead(inPin) == 1) {
    Serial.println("Door Closed");
    doorStatus = 0;
    alarmRequest("closed");
    digitalWrite(LED_BUILTIN, HIGH);
  }
}

