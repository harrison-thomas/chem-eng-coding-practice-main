  #include "DHT.h"
  #define DHT11_PIN 10

  DHT dht11(DHT11_PIN, DHT11);


void setup() {
  // put your setup code here, to run once:

  dht11.begin();
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  delay(2000);
  float tempC = dht11.readTemperature();

  Serial.print("Temperature: ");
  Serial.print(tempC);
  Serial.print("degrees celsius");

}
