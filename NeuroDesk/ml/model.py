from __future__ import annotations
import torch
import torch.nn as nn


class AttentionNet(nn.Module):
    def __init__(self, input_dim: int = 8):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 32), nn.ReLU(),
            nn.Linear(32, 16), nn.ReLU(),
            nn.Linear(16, 1), nn.Sigmoid(),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


class AdaptiveCalibrator:
    def __init__(self):
        self.alpha = 0.1
        self.offset = 0.0

    def update(self, score: float, label: int | None):
        # If label provided (1=attend, 0=distract), shift offset to separate states
        if label is None:
            return
        target = 0.8 if label == 1 else 0.2
        self.offset = (1 - self.alpha) * self.offset + self.alpha * (target - score)

    def apply(self, score: float) -> float:
        s = max(0.0, min(1.0, score + self.offset))
        return s


