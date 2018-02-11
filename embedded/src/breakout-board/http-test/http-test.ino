#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "FlipTables";
const char* password = "visit umbrella find shame";
//const char* host = "192.168.1.100";  // TUBUS
const char* host = "192.168.1.115";  // griefcake
int port = 8008;

HTTPClient http;

void testRequest() {
  
  String addr = "http://" + String(host) + ":" + port + "/alarm";
  Serial.println("Address: `" + addr + "`");
  http.begin(addr);
  
  http.addHeader("Content-Type", "application/json");
  
  String message = "{\"Hello\" : \"World\"}";
  Serial.println("Message: `" + message + "`");
  int response = http.POST(message);
  
//  http.writeToStream(&Serial);
  Serial.println(response);
  
  http.end();
}

void setup() {

  Serial.begin(115200);
  WiFi.begin(ssid, password);

  Serial.println();
  Serial.println();
  Serial.println("Connecting to " + String(ssid));
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Print the IP address
  Serial.println(WiFi.localIP());
  
}

void loop() {
  
    testRequest();
    delay(1000);
    
}

