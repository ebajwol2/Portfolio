import serial
import time


class RadarReader:
    def __init__(self, port: str = "/dev/ttyUSB0", baud: int = 921600):
        self.ser = serial.Serial(port, baudrate=baud, timeout=0.1)

    def read_tracks(self):
        # TODO: parse TI demo protocol; stub yields empty list
        time.sleep(0.05)
        return []


