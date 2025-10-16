EchoGrip BLE GATT Profile (Draft)

Advertising Name: EchoGrip

Services

1) Telemetry Service
- UUID: 8f264f10-7d3c-4c8f-9a2e-3b0a0b6c1111
- Characteristics:
  - Result (Notify)
    - UUID: 8f264f11-7d3c-4c8f-9a2e-3b0a0b6c1111
    - Payload (8 bytes):
      - classId: int16 (LE)
      - confidence: uint16 Q8.8 (0..1)
      - sizeScore: uint16 Q8.8 (0..1)
      - textureScore: uint16 Q8.8 (0..1)

2) Control Service
- UUID: 8f264f20-7d3c-4c8f-9a2e-3b0a0b6c2222
- Characteristics:
  - Control (Write)
    - UUID: 8f264f21-7d3c-4c8f-9a2e-3b0a0b6c2222
    - Commands (opcode + payload):
      - 0x01: Set Mode (0=Idle,1=Run,2=Calibrate)
      - 0x02: Set Sample Period (ms, uint16)
      - 0x03: Haptic Override (intensity[5] bytes)
      - 0x10: Start Calibration (classId int16)
      - 0x11: Stop Calibration
      - 0x20: Prototypes Export Request
      - 0x21: Prototypes Import Chunk (variable length)

Security

- Optional bonding. No sensitive PII in telemetry. Consider requiring encryption for prototype transfer.


