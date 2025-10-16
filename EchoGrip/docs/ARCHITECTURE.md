EchoGrip Architecture

System Goal

Provide haptic representations of objects’ shape, texture, and size via a smart glove for visually impaired users. End-to-end latency (sensor-to-haptic) target < 60 ms; BLE telemetry for app visualization < 150 ms.

Hardware Overview

- MCU: ESP32 (dual-core), BLE, sufficient RAM/flash for TFLM
- Sensors:
  - Ultrasonic modules around fingers (index, middle, ring) for distance profiles
  - Pressure sensors (FSR) on each fingertip (thumb–pinky)
- Actuators: coin vibration motors at each fingertip + palm
- Power: LiPo + charger + 3D-printed frame wiring channels

Firmware Overview

Dataflow (per 10–20 ms tick):
1. Sample ultrasonic sensors (staggered trigger to avoid crosstalk)
2. Sample fingertip pressure sensors (ADC)
3. Preprocess: low-pass, normalization, feature windows (distance deltas, pressure variance)
4. Feature fusion to fixed-length vector
5. Run TFLM inference → class logits + confidence + size/shape embeddings
6. Haptic mapper → vibration patterns (intensity, duration, spatial pattern)
7. BLE publish (compressed) to app; handle app control commands

On-Device Learning

- Calibration Mode: user selects “add object” in app → glove records labeled sensor windows while user touches object
- Adaptation: maintain a small prototype memory (embedding + class label); few-shot nearest-centroid on top of base model
- Persistence: store prototypes in NVS; export/import via BLE for backup

BLE Interface

- Services: EchoGrip Control, EchoGrip Telemetry
- Characteristics:
  - Control: mode, sampling rate, calibration start/stop, haptic override
  - Telemetry: fused features (optional), class id, confidence, size/shape scores, battery
  - Learning: push/pull prototypes

Mobile App

- BLE client; real-time dashboard of recognized object, confidence, and haptic pattern legend
- Calibration workflow UI
- Local store of prototypes; sync with glove

Benchmarks

- Latency: ISR→fusion→inference→haptic; BLE publish time separate
- Accuracy: per-class precision/recall, confusion matrices
- Robustness: crosstalk scenarios, varied grip force

Security/Privacy

- BLE bonding optional; minimal PII. On-device models and prototypes stored locally.

Future Extensions

- Additional modalities (IMU, microphone), dynamic haptic rendering, multi-glove coordination.


