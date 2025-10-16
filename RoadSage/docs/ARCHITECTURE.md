RoadSage Architecture

Goal

Warn cyclists of fast-approaching vehicles using rear camera + mmWave radar with low latency and high precision. Log events to a mobile app.

Hardware

- Raspberry Pi 4/5 + Camera Module
- mmWave radar (TI IWR6843AOP) via UART/CAN
- NeoPixel LED strip and vibration motor (GPIO/PWM)
- BLE module (onboard)

Software Components

- camera.py: captures frames; runs YOLOv8n (TFLite) to detect vehicles
- radar.py: parses radar point cloud/tracks (TI demo protocol)
- fusion.py: associates detections with radar tracks; computes approach rate
- alerts.py: drives LEDs/motor based on risk score
- ble.py: streams events to app
- service.py: orchestrates pipeline

Adaptive Sensitivity

- Adjust thresholds by rider speed (from wheel sensor/GPS) and road type (user profile)
- Lower sensitivity at low speeds in quiet streets; raise on highways

Metrics

- Detection latency, false alert rate, true proximity warnings


