ML Pipeline (Stub)

Goals

- Train a lightweight model on fused features to classify objects and produce an embedding for few-shot prototypes. Export a TensorFlow Lite Micro model for the ESP32.

Environment

- Create a Python venv and install requirements once requirements.txt is added.

Data Format

- CSV rows with timestamp, distances[3], pressures[5], label
- Use scripts/collect_data.py to record from serial/BLE

Scripts

- scripts/train.py: trains baseline model and saves SavedModel
- scripts/export_tflm.py: converts to TFLite, quantizes (int8), and emits a C array header

Output

- build/echogrip_model.tflite
- build/echogrip_model_int8.cc (C array for firmware)

Next

- Add requirements.txt and implement the scripts


