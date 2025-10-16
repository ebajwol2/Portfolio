#include "sensors.h"

// Pin assignments (placeholder, update per hardware)
static const int PIN_US_INDEX_TRIG = 4;
static const int PIN_US_INDEX_ECHO = 5;
static const int PIN_US_MIDDLE_TRIG = 16;
static const int PIN_US_MIDDLE_ECHO = 17;
static const int PIN_US_RING_TRIG = 18;
static const int PIN_US_RING_ECHO = 19;

static const int PIN_FSR_THUMB = 32;  // ADC1
static const int PIN_FSR_INDEX = 33;  // ADC1
static const int PIN_FSR_MIDDLE = 34; // ADC1
static const int PIN_FSR_RING = 35;   // ADC1
static const int PIN_FSR_PINKY = 36;  // ADC1

static float readUltrasonicCm(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 20000); // timeout 20 ms
  if (duration <= 0) return NAN;
  float cm = duration * 0.034f / 2.0f;
  return cm;
}

void sensorsInit() {
  pinMode(PIN_US_INDEX_TRIG, OUTPUT);
  pinMode(PIN_US_INDEX_ECHO, INPUT);
  pinMode(PIN_US_MIDDLE_TRIG, OUTPUT);
  pinMode(PIN_US_MIDDLE_ECHO, INPUT);
  pinMode(PIN_US_RING_TRIG, OUTPUT);
  pinMode(PIN_US_RING_ECHO, INPUT);
}

SensorReadings sensorsRead() {
  SensorReadings sr{};
  // Stagger to avoid crosstalk
  sr.distances.indexCm = readUltrasonicCm(PIN_US_INDEX_TRIG, PIN_US_INDEX_ECHO);
  delayMicroseconds(500);
  sr.distances.middleCm = readUltrasonicCm(PIN_US_MIDDLE_TRIG, PIN_US_MIDDLE_ECHO);
  delayMicroseconds(500);
  sr.distances.ringCm = readUltrasonicCm(PIN_US_RING_TRIG, PIN_US_RING_ECHO);

  sr.pressures.thumb = analogRead(PIN_FSR_THUMB);
  sr.pressures.index = analogRead(PIN_FSR_INDEX);
  sr.pressures.middle = analogRead(PIN_FSR_MIDDLE);
  sr.pressures.ring = analogRead(PIN_FSR_RING);
  sr.pressures.pinky = analogRead(PIN_FSR_PINKY);
  return sr;
}


