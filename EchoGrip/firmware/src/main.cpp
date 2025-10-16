#include <Arduino.h>
#include "sensors.h"
#include "fusion.h"
#include "ml_inference.h"
#include "haptics.h"
#include "ble_server.h"

static const uint32_t SENSOR_PERIOD_MS = 20; // 50 Hz
static uint32_t lastTickMs = 0;

void setup() {
  Serial.begin(115200);
  delay(200);
  Serial.println("EchoGrip booting...");

  sensorsInit();
  hapticsInit();
  bleInit();
  mlInit();

  Serial.println("EchoGrip ready.");
}

void loop() {
  const uint32_t now = millis();
  if (now - lastTickMs >= SENSOR_PERIOD_MS) {
    lastTickMs = now;

    SensorReadings readings = sensorsRead();
    FeatureVector features = fuseFeatures(readings);

    InferenceResult result = mlInfer(features);

    applyHaptics(result);
    blePublish(result, features);
  }

  bleHandle();
}


