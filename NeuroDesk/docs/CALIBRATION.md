Calibration and Adaptive Learning

Purpose

Personalize attention detection by learning per-user offsets from labeled mini-sessions.

Workflow

1) Baseline: user sits calmly and focuses for 60 s → label=1
2) Distraction: reading headlines/music for 60 s → label=0
3) Repeat short 20 s boosts during real work; user taps shortcut to mark focus/distraction

Model Update

- Compute current attention score; update AdaptiveCalibrator with label
- Offset is smoothed (EMA) to shift decision boundary

Privacy

- Raw EEG stays local; no cloud uploads by default.


