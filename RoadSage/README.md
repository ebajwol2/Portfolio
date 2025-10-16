RoadSage – Rear Vehicle Detection and Alerts for Cyclists

Overview

RoadSage fuses a rear-facing camera and mmWave radar to detect fast-approaching vehicles and alerts cyclists via vibration and LEDs. It adapts sensitivity to rider speed and road context, and logs near-misses for post-ride analytics in a mobile app.

Key Features

- Lightweight vision with YOLOv8 Nano (TFLite) on Raspberry Pi
- mmWave radar ingest (TI IWR6843AOP) over UART/CAN
- Sensor fusion with relative speed and distance estimation
- NeoPixel LED + vibration motor alerts with graded urgency
- BLE to companion app for ride logs

Repo Structure

- rpi: Python services for camera, radar, fusion, alerts, BLE
- app: React Native app stub for logs and settings
- docs: Architecture, adaptive sensitivity, metrics
- models: TFLite model and label files

Quick Start

1) Set up RPi with camera and Python deps
2) Place YOLOv8n TFLite in models/
3) Run rpi/service.py
4) Start app and connect via BLE

License

MIT


