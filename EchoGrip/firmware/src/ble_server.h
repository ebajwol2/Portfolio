#pragma once
#include "ml_inference.h"
#include "fusion.h"

void bleInit();
void bleHandle();
void blePublish(const InferenceResult &result, const FeatureVector &fv);


