Adaptive Sensitivity

Inputs

- Rider speed (kph) from wheel sensor/GPS
- Road type: path, urban, arterial, highway (user setting or map)

Policy

- Base risk threshold = 0.6
- If speed > 25 kph → threshold -0.1 (more sensitive)
- If road type ∈ {arterial, highway} → threshold -0.1
- Clamp threshold to ≥ 0.3

Effects

- Higher sensitivity at faster speeds and busier roads → earlier alerts
- Lower sensitivity in quiet/low-speed contexts → fewer false alarms


