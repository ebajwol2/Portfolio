#include "haptics.h"
#include <Arduino.h>

// Placeholder PWM pins for vibration motors (update per hardware)
static const int PIN_MOTOR_THUMB = 23;
static const int PIN_MOTOR_INDEX = 25;
static const int PIN_MOTOR_MIDDLE = 26;
static const int PIN_MOTOR_RING = 27;
static const int PIN_MOTOR_PINKY = 14;

static void driveMotor(int pin, float intensity01) {
  intensity01 = constrain(intensity01, 0.0f, 1.0f);
  int pwm = (int)(intensity01 * 255.0f);
  analogWrite(pin, pwm);
}

void hapticsInit() {
  pinMode(PIN_MOTOR_THUMB, OUTPUT);
  pinMode(PIN_MOTOR_INDEX, OUTPUT);
  pinMode(PIN_MOTOR_MIDDLE, OUTPUT);
  pinMode(PIN_MOTOR_RING, OUTPUT);
  pinMode(PIN_MOTOR_PINKY, OUTPUT);
}

void applyHaptics(const InferenceResult &r) {
  // Map sizeScore to spatial intensity; textureScore to pulse width (simple placeholder)
  float base = constrain(r.sizeScore, 0.1f, 1.0f);
  float texture = constrain(r.textureScore, 0.0f, 1.0f);

  // Simple spatial pattern: index/middle ring stronger if larger
  driveMotor(PIN_MOTOR_INDEX, base);
  driveMotor(PIN_MOTOR_MIDDLE, base * 0.9f);
  driveMotor(PIN_MOTOR_RING, base * 0.7f);
  driveMotor(PIN_MOTOR_THUMB, 0.3f + 0.7f * texture);
  driveMotor(PIN_MOTOR_PINKY, 0.2f + 0.6f * texture);
}


