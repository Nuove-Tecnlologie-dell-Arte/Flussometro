#include <math.h>
#define PIR_PIN 2 // Pin del sensore PIR

const int sampleWindow = 50; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;

void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
    pinMode(7, OUTPUT);
}

void loop() {
  unsigned long startMillis= millis();  // Start of sample window
  unsigned int peakToPeak = 0;   // peak-to-peak level

  unsigned int signalMax = 0;
  unsigned int signalMin = 1024;

  // collect data for 50 mS for microphone
  while (millis() - startMillis < sampleWindow)
  {
    sample = analogRead(A0);
    if (sample < 1024)  // toss out spurious readings
    {
      if (sample > signalMax)
      {
        signalMax = sample;  // save just the max levels
      }
      else if (sample < signalMin)
      {
        signalMin = sample;  // save just the min levels
      }
    }
  }
  peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
  double volts = (peakToPeak * 3.3) / 1024;  // convert to volts

  double dB = 20 * log10(volts / 0.0001);
  // send to serial port
  int y = int(dB);
  Serial.print(y);
  Serial.print(",");

  // read data from photoresistor
  int lightLevel = analogRead(A1);
  int lumen = map(lightLevel, 1023, 0, 0, 300);
  Serial.print(lumen);
  Serial.print(",");


int pirValue = digitalRead(PIR_PIN); // Legge il valore del sensore PIR
  if (pirValue == HIGH) { // Se il sensore rileva movimento
    Serial.println("1"); // Invia un messaggio di movimento rilevato alla seriale
  }
  else {
    Serial.println("0"); // Invia un messaggio di nessun movimento rilevato alla serialeint


  }


if (dB>46){
  digitalWrite(7, HIGH);
  }
else{ 
  digitalWrite(7, LOW);
}
}