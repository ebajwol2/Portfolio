from __future__ import annotations
import asyncio
import json
import time
from typing import AsyncIterator, Callable
import numpy as np
import websockets
import torch
from NeuroDesk.ml.model import AttentionNet, AdaptiveCalibrator  # type: ignore
from .ingest import muse_mock_reader


class AttentionEngine:
    def __init__(self):
        self.model = AttentionNet(input_dim=8).eval()
        self.calibrator = AdaptiveCalibrator()

    def infer(self, features: np.ndarray) -> float:
        x = torch.from_numpy(features.astype(np.float32)).unsqueeze(0)
        with torch.no_grad():
            y = self.model(x).squeeze().item()
        y = self.calibrator.apply(y)
        return max(0.0, min(1.0, float(y)))


async def ws_server(host: str = "0.0.0.0", port: int = 8765):
    engine = AttentionEngine()
    latest_score: float = 0.0

    def on_features(vec: np.ndarray):
        nonlocal latest_score
        latest_score = engine.infer(vec)

    async def ingest_task():
        await muse_mock_reader(on_features)

    async def handler(websocket):
        while True:
            await websocket.send(json.dumps({"score": latest_score}))
            await asyncio.sleep(0.2)

    asyncio.create_task(ingest_task())
    async with websockets.serve(handler, host, port):
        await asyncio.Future()


def run_ws():
    asyncio.run(ws_server())


