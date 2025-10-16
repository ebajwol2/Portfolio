#pragma once
#include "fusion.h"

struct InferenceResult {
  int classId;
  float confidence;
  float sizeScore;   // 0..1
  float textureScore; // 0..1
};

void mlInit();
InferenceResult mlInfer(const FeatureVector &fv);


