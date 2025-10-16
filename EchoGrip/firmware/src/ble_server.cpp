#include "ble_server.h"
#include <Arduino.h>
#include <NimBLEDevice.h>

// UUIDs (placeholder, will document in docs/BLE_GATT.md)
static const char* SERVICE_TELEMETRY_UUID = "8f264f10-7d3c-4c8f-9a2e-3b0a0b6c1111";
static const char* CHAR_RESULT_UUID      = "8f264f11-7d3c-4c8f-9a2e-3b0a0b6c1111"; // classId, confidence, size, texture
static const char* SERVICE_CONTROL_UUID  = "8f264f20-7d3c-4c8f-9a2e-3b0a0b6c2222";
static const char* CHAR_CONTROL_UUID     = "8f264f21-7d3c-4c8f-9a2e-3b0a0b6c2222"; // modes

static NimBLEServer* server = nullptr;
static NimBLECharacteristic* charResult = nullptr;
static NimBLECharacteristic* charControl = nullptr;

void bleInit() {
  NimBLEDevice::init("EchoGrip");
  server = NimBLEDevice::createServer();

  NimBLEService* telemetry = server->createService(SERVICE_TELEMETRY_UUID);
  charResult = telemetry->createCharacteristic(CHAR_RESULT_UUID, NIMBLE_PROPERTY::NOTIFY);
  telemetry->start();

  NimBLEService* control = server->createService(SERVICE_CONTROL_UUID);
  charControl = control->createCharacteristic(CHAR_CONTROL_UUID, NIMBLE_PROPERTY::WRITE);
  control->start();

  NimBLEAdvertising* adv = NimBLEDevice::getAdvertising();
  adv->addServiceUUID(SERVICE_TELEMETRY_UUID);
  adv->start();
}

void bleHandle() {
  // Placeholder for write handlers, connection state, etc.
}

void blePublish(const InferenceResult &result, const FeatureVector &fv) {
  if (!charResult) return;
  uint8_t buf[8];
  // Pack: classId (int16), conf (uint16 Q8.8), size (uint16 Q8.8), texture (uint16 Q8.8)
  int16_t cid = (int16_t)result.classId;
  uint16_t conf = (uint16_t)(constrain(result.confidence, 0.0f, 1.0f) * 256.0f);
  uint16_t size = (uint16_t)(constrain(result.sizeScore, 0.0f, 1.0f) * 256.0f);
  uint16_t tex  = (uint16_t)(constrain(result.textureScore, 0.0f, 1.0f) * 256.0f);
  memcpy(buf, &cid, 2);
  memcpy(buf + 2, &conf, 2);
  memcpy(buf + 4, &size, 2);
  memcpy(buf + 6, &tex, 2);
  charResult->setValue(buf, sizeof(buf));
  charResult->notify();
}


