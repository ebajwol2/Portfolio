On-Device Learning (Calibration Mode)

Concept

Allow users to add new objects using a few-shot approach: capture fused feature windows while touching the object; compute an embedding using the base model; store class prototype(s) for nearest-centroid classification.

Workflow

1) App sends Set Mode: Calibrate and Start Calibration(classId)
2) Firmware buffers N windows (e.g., 100 windows at 50 Hz ≈ 2 s)
3) For each window, compute embedding via TFLM head; aggregate (mean) into prototype
4) Store prototype in NVS with label metadata
5) Normal Run: classify by nearest prototype in embedding space; fall back to base logits if unknown
6) Export/Import prototypes via BLE for backup or sharing

Data Management

- Max prototypes per class: 3 (median-of-means for robustness)
- Storage: NVS, versioned
- Eviction: LRU when space limited

UI Guidance

- Voice or haptic prompts for start/stop; progress indicator in app
- Require steady grip during capture; reject high-variance segments

Safety

- Limit motor intensity during calibration; avoid fatigue


