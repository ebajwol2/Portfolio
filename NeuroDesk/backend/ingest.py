from __future__ import annotations
from typing import Callable
import asyncio
import numpy as np


async def muse_mock_reader(callback: Callable[[np.ndarray], None]):
    # Produce mock bandpower features: [delta, theta, alpha, beta] both hemispheres
    import math, time
    t0 = time.time()
    while True:
        t = time.time() - t0
        base = 0.5 + 0.3 * math.sin(t / 7.0)
        vec = np.array([
            base*1.1, 0.6, 0.5, 0.4,
            base*0.9, 0.6, 0.5, 0.4,
        ], dtype=np.float32)
        callback(vec)
        await asyncio.sleep(0.2)


