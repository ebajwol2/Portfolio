import time

try:
    import board
    import neopixel
except Exception:
    board = None
    neopixel = None


class AlertDriver:
    def __init__(self, num_pixels: int = 12, pin = None):
        self.num_pixels = num_pixels
        if board and neopixel:
            self.pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)
        else:
            self.pixels = None

    def set_level(self, level: float):
        level = max(0.0, min(1.0, level))
        if not self.pixels:
            return
        r = int(255 * level)
        g = int(255 * (1.0 - level))
        for i in range(self.num_pixels):
            self.pixels[i] = (r, g, 0)
        self.pixels.show()


