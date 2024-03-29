#include<ESP8266WiFi.h>
#include<WiFiClient.h>
#include<ESP8266WebServer.h>
#include<LiquidCrystal_I2C.h>
#include<Wire.h>
#include <QRCode.h> 
void printDetail(uint8_t type, int value);
LiquidCrystal_I2C lcd(0x3f, 16, 2);
const char* ssid = "justdo";
const char* password = "@12345";
ESP8266WebServer server(80);
String page = "";
char input[12];
int count = 0;
int a;
int p1 = 0, p2 = 0, p3 = 0, p4 = 0;
int c1 = 0, c2 = 0, c3 = 0, c4 = 0;
 
double total = 0;
int count_prod = 0;

int led1 = D5;
int led2 = D7;
int buzzer = D6;