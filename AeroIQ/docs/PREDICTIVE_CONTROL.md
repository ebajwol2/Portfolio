Predictive Control – Air Aging

Concept

Model the short-term trend of CO₂/VOC (15–30 min horizon) using time-of-day, weekday, recent levels, and optional contextual signals (cooking, occupancy). Trigger ventilation before thresholds are exceeded.

Policy

1) Forecast future CO₂/VOC: \~30 min ahead
2) If forecast crosses thresholds (e.g., CO₂ > 900 ppm, VOC > 300 ppb), start fan with speed schedule
3) Apply hysteresis and cooldown to avoid oscillation
4) Respect quiet hours; allow user override

Features

- hour_of_day (0..23), is_weekend
- recent co2 mean/gradient, voc mean/gradient
- external window state (optional)

KPIs

- Time above threshold per day
- Control actuation count and runtime


