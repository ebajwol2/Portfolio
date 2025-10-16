EchoGrip – Smart Haptic Object Recognition Glove

Overview

EchoGrip is a hardware–software system that helps users, especially those who are visually impaired, perceive shape, texture, and size of nearby objects through subtle vibration feedback. The glove fuses ultrasonic distance readings and fingertip pressure data, recognizes objects using a TinyML model on an ESP32, and communicates results to a companion mobile app over BLE. Users can add new objects via an on-device calibration workflow.

Key Features

- On-device sensor fusion (ultrasonic + pressure)
- TinyML inference (TensorFlow Lite for Microcontrollers)
- BLE streaming to mobile app (React Native)
- Haptic feedback mapping for shape/texture/size cues
- On-device learning: user-calibrated classes

Repo Structure

- firmware: ESP32 firmware (C++/PlatformIO), BLE, sensor fusion, TinyML hooks
- ml: Training pipeline stubs, TFLite Micro export utilities, dataset format
- app: React Native sample BLE client, UI schema for dashboard
- docs: Architecture, BLE GATT spec, on-device learning, benchmarking

Quick Start

1) Firmware
- Install PlatformIO (VS Code extension or CLI)
- Open firmware and run: build, upload, monitor

2) ML
- Create a Python venv, install ml/requirements.txt
- Run training and export scripts to produce a TFLM model header for firmware

3) App
- Use an existing React Native setup (or Expo Bare)
- Install dependencies listed in app/README.md and run on iOS/Android

Documentation

- See docs/ARCHITECTURE.md for the end-to-end system design
- See docs/BLE_GATT.md for the BLE protocol
- See docs/ON_DEVICE_LEARNING.md for calibration and incremental learning
- See docs/BENCHMARKS.md for latency/accuracy methodology

License

MIT


