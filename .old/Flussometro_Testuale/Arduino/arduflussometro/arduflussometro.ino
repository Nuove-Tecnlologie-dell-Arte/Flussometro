#include <math.h>
#define PIR_PIN 2 // Pin del sensore PIR

void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
}

void loop() {
int pirValue = digitalRead(PIR_PIN); // Legge il valore del sensore PIR
  if (pirValue == HIGH) { // Se il sensore rileva movimento
    Serial.println("1"); // Invia un messaggio di movimento rilevato alla seriale
    delay(1000);
  }
  else {
    Serial.println("0"); // Invia un messaggio di nessun movimento rilevato alla seriale
    
  }
}
