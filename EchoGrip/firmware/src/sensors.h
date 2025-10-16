#pragma once
#include <Arduino.h>

struct UltrasonicDistances {
  float indexCm;
  float middleCm;
  float ringCm;
};

struct FingerPressures {
  uint16_t thumb;
  uint16_t index;
  uint16_t middle;
  uint16_t ring;
  uint16_t pinky;
};

struct SensorReadings {
  UltrasonicDistances distances;
  FingerPressures pressures;
};

void sensorsInit();
SensorReadings sensorsRead();


