import cv2
import numpy as np


class YoloDetector:
    def __init__(self, tflite_path: str, conf_thres: float = 0.4):
        self.conf_thres = conf_thres
        # Placeholder: use OpenCV as a stub; integrate tflite interpreter for YOLOv8n
        self.net = None

    def detect(self, frame: np.ndarray):
        # TODO: run tflite model; stub returns empty detections
        return []


def camera_frames(device: int = 0):
    cap = cv2.VideoCapture(device)
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        yield frame


