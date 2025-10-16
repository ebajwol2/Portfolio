Latency and Accuracy Benchmarks

Targets

- End-to-end haptic latency: < 60 ms (sensor read → haptic update)
- BLE telemetry latency: < 150 ms median, < 250 ms P95
- Accuracy: > 85% macro F1 across base classes; calibrated classes ≥ 75% with 5-shot

Latency Measurement

- Timestamp at ISR/tick start, post-fusion, post-inference, post-haptic; log over UART
- BLE: app timestamps notification receipt; compute delta from firmware timestamp field (future addition)

Accuracy Evaluation

- Collect labeled sessions per object: varied distances and grip forces
- Split by session (no leakage), compute confusion matrix, precision/recall/F1
- After calibration, evaluate few-shot classes separately

Robustness Tests

- Ultrasonic crosstalk (multiple sensors firing)
- Pressure sensor drift and different users
- Battery levels and motor load effects

Scripts

- ml/scripts/collect_data.py: serial/BLE data capture
- ml/scripts/evaluate.py: offline metrics


