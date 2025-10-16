#include "fusion.h"

static float clampf(float v, float lo, float hi) {
  if (v < lo) return lo;
  if (v > hi) return hi;
  return v;
}

FeatureVector fuseFeatures(const SensorReadings &sr) {
  FeatureVector fv{};
  fv.distances[0] = isfinite(sr.distances.indexCm) ? sr.distances.indexCm : 200.0f;
  fv.distances[1] = isfinite(sr.distances.middleCm) ? sr.distances.middleCm : 200.0f;
  fv.distances[2] = isfinite(sr.distances.ringCm) ? sr.distances.ringCm : 200.0f;

  fv.pressures[0] = sr.pressures.thumb / 4095.0f;
  fv.pressures[1] = sr.pressures.index / 4095.0f;
  fv.pressures[2] = sr.pressures.middle / 4095.0f;
  fv.pressures[3] = sr.pressures.ring / 4095.0f;
  fv.pressures[4] = sr.pressures.pinky / 4095.0f;

  // Normalize distance range to ~0..1 assuming 5cm..150cm
  for (int i = 0; i < 3; ++i) {
    float d = fv.distances[i];
    float norm = (d - 5.0f) / (150.0f - 5.0f);
    fv.distances[i] = clampf(norm, 0.0f, 1.0f);
  }
  return fv;
}


