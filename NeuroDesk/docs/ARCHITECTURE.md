NeuroDesk Architecture

Goal

Provide live attention monitoring and environment control. Learn user-specific EEG patterns for robust attention vs distraction detection.

Hardware

- EEG headset (Muse/OpenBCI/MindFlex)
- BLE or USB link to host (Raspberry Pi or PC)

Backend

- EEG ingest: via SDK/OSC/BLE
- Signal processing: band power (delta/theta/alpha/beta), artifacts
- ML: attention classifier (PyTorch), adaptive calibration
- WebSocket server: /ws/attention broadcasting {score: 0..1}

Desktop App (Electron)

- Connects to WS, renders dashboard, triggers DND/OS actions

Adaptive Learning

- Calibration sessions: label attention/distraction while performing tasks
- Continual update: per-user thresholds and domain adaptation layer

Privacy

- Local processing; no raw EEG leaves machine by default


