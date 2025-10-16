from __future__ import annotations
from typing import List, Dict, Any


def associate(camera_dets: List[Dict[str, Any]], radar_tracks: List[Dict[str, Any]]):
    # TODO: nearest-neighbor association; stub returns risk score 0
    risk = 0.0
    return risk


def adaptive_thresholds(rider_speed_kph: float, road_type: str) -> float:
    base = 0.6
    if rider_speed_kph > 25:
        base -= 0.1
    if road_type in ("highway", "arterial"):
        base -= 0.1
    return max(0.3, base)


