void setup()
{
  Serial.begin(115200);
  pinMode(D4, INPUT_PULLUP);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(buzzer, OUTPUT);
 
  Serial.begin(9600);
 
  WiFi.begin(ssid, password);
  Wire.begin(D2, D1);
 
  lcd.begin();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("WELCOME TO");
  lcd.setCursor(0, 1);
  lcd.print("SMART TROLLY");
  delay(2000);
  lcd.clear();
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    lcd.setCursor(3, 0);
    lcd.print("WiFi Connecting...  ");
  }
  Serial.print(WiFi.localIP());
  lcd.setCursor(0, 0);
  lcd.print("WiFi Connected");
  lcd.setCursor(0, 1);
  lcd.print(WiFi.localIP());
  delay(2000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" PLZ SCAN ITEMS");
  lcd.setCursor(0, 1);
  lcd.print("    TO CART");
    server.on("/", []() {
    page = "<html><head><title>Smart Shopping Cart</title></head><style type=\"text/css\">";
    page += "table{border-collapse: collapse;}th {background-color: #4444db ;color: white;}table,td {border: 4px solid black;font-size: x-large;";
    page += "text-align:center;border-style: groove;border-color: rgb(255,0,0);}</style><body><center>";
    page += "<h1>Welcome To Smart Cart Trolley</h1><br><br><table style=\"width: 1200px;height: 450px;\"><tr>";
    page += "<th>ITEMS</th><th>QUANTITY</th><th>COST</th></tr><tr><td>Sugar</td><td>" + String(p1) + "</td><td>" + String(c1) + "</td></tr>";
    page += "<tr><td>Milk</td><td>" + String(p2) + "</td><td>" + String(c2) + "</td></tr><tr><td>Biscuits</td><td>" + String(p3) + "</td><td>" + String(c3) + "</td>";
    page += "</tr><tr><td>Dairy Milk</td><td>" + String(p4) + "</td><td>" + String(c4) + "</td></tr><tr><th>Grand Total</th><th>" + String(count_prod) + "</th><th>" + String(total) + "</th>";
    page += "</tr></table><br><input type=\"button\" name=\"Pay Online Now\" value=\"Pay Online Now\" style=\"width: 200px;height: 50px\" onclick=\"window.location='/payment?amount=" + String(total, 2) + "';\">";
    page += "</center></body></html>";
    page += "<meta http-equiv=\"refresh\" content=\"2\">";
    server.send(200, "text/html", page);
    });

server.on("/payment", [](){
  // Extract the total amount from the query parameters
  String amountParam = server.arg("amount");
  float amount = amountParam.toFloat();

  page = "<html><head><title>Payment</title></head><body><center>";
  // Generate QR code for payment using the dynamic amount
  QRCode qrcode;
  uint8_t qrcodeData[qrcode_getBufferSize(1)];
  qrcode_initText(&qrcode, (char*)"Amount: " + String(amount, 2).c_str());
  char qrcodeDisplay[400]; // Adjust buffer size as necessary
  qrcode_toDisplayString(&qrcode, qrcodeDisplay, 1);
  page += "<h1>Scan QR Code to Pay Rs. " + String(amount, 2) + "</h1>";
  page += "<img src='data:image/png;base64, " + String(qrcodeDisplay) + "' />";
  page += "</center></body></html>";
  server.send(200, "text/html", page);
});
  server.begin();
}