from __future__ import annotations
import time
from camera import YoloDetector, camera_frames
from radar import RadarReader
from fusion import associate, adaptive_thresholds
from alerts import AlertDriver


def main():
    det = YoloDetector(tflite_path="../models/yolov8n.tflite")
    radar = RadarReader()
    alerts = AlertDriver(num_pixels=12)

    rider_speed_kph = 20.0
    road_type = "urban"

    frames = camera_frames(0)
    while True:
        try:
            frame = next(frames)
        except StopIteration:
            break
        camera_dets = det.detect(frame)
        radar_tracks = radar.read_tracks()

        risk = associate(camera_dets, radar_tracks)
        thr = adaptive_thresholds(rider_speed_kph, road_type)
        level = max(0.0, (risk - thr) / (1.0 - thr))
        alerts.set_level(level)
        time.sleep(0.02)


if __name__ == "__main__":
    main()


