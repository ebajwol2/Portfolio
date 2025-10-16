#pragma once
#include "sensors.h"

struct FeatureVector {
  // Simple fixed-length features; extend with windows/derivatives
  float distances[3];
  float pressures[5];
};

FeatureVector fuseFeatures(const SensorReadings &sr);


