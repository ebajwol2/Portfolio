NeuroDesk – EEG-Driven Personal Productivity

Overview

NeuroDesk monitors attention using a consumer EEG headband and adapts your computer environment in real time (DND, pause music, lock phone). It provides a WebSocket attention stream and an Electron desktop app that applies controls. The system learns your personal brainwave patterns via adaptive calibration.

Key Features

- EEG ingest (Muse/OpenBCI/MindFlex via BLE/SDK)
- Attention classifier (PyTorch) with adaptive calibration
- WebSocket API for live attention stream
- Electron desktop app for DND/automation PoC

Repo Structure

- backend: Python server (EEG ingest, ML inference, WS API)
- ml: Attention model and calibration utilities
- app: Electron app subscribing to WS and applying controls
- docs: Architecture and privacy/calibration docs

Quick Start

1) Backend: python -m NeuroDesk.backend
2) App: yarn && yarn start (within app)

License

MIT


