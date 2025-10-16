AeroIQ Architecture

Goal

Maintain healthy indoor air by sensing CO₂/VOC/temperature/humidity and automatically controlling ventilation. Predict air quality degradation and refresh proactively.

Hardware

- MCU: ESP32 or host: Raspberry Pi
- Sensors: CO₂ (e.g., SCD41), VOC (e.g., SGP30/CCS811), Temperature/Humidity (SHT31/DHT22)
- Actuators: smart relays for fans/purifiers; optional LCD for live readings

Software Components

- Device (ESP32/RPi): reads sensors, publishes MQTT topics, accepts control commands
- Backend (Python/Flask): MQTT consumer, writes to InfluxDB, exposes REST API, runs control policy
- ML (air-aging): time-series prediction of CO₂/VOC; schedules ventilation before thresholds crossed
- Dashboard: Grafana (InfluxDB datasource) + minimal web frontend for controls

Data Model (MQTT)

- topics:
  - aeroiq/sensors/{deviceId}
    - payload: { ts, co2_ppm, voc_ppb, temp_c, rh_pct }
  - aeroiq/control/{deviceId}
    - payload: { fan_on: bool, speed: 0..100 }

Control Strategy

- Threshold-based hysteresis + predictive boost
- Safety limits: min/max runtime, cooldown
- Quiet hours profile

Benchmarks

- Control reaction < 1 s from threshold or prediction
- Forecast horizon: 15–30 min


