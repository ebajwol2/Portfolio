AeroIQ – Smart Air-Quality Guardian

Overview

AeroIQ monitors indoor air (CO₂, VOC, temperature, humidity) and automatically drives ventilation (fans/purifiers) to keep air quality optimal. It predicts “air aging” based on user habits (cooking, study time) and refreshes air proactively. Data is collected via Python backend (Flask, MQTT) and stored in InfluxDB, visualized with Grafana.

Key Features

- Sensor ingestion via MQTT (ESP32/RPi)
- Adaptive control service to toggle relays for fans/purifiers
- Predictive air-aging model for pre-emptive ventilation
- Web dashboard and Grafana graphs

Repo Structure

- backend: Flask API, MQTT consumer, control loop, InfluxDB client
- device: ESP32/RPi scripts for sensors and relays
- ml: Training stubs for prediction (TensorFlow/Sklearn)
- docs: Architecture and control strategy
- dashboard: Grafana provisioning

Quick Start

1) Start services: docker-compose up -d (InfluxDB, Grafana)
2) Run backend: python -m backend
3) Start device script or firmware to publish MQTT
4) Open Grafana and configure dashboards

License

MIT


