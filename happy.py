import time
from blinkable import Blinkable
from smiley import Smiley

class Happy(Smiley, Blinkable):
    def __init__(self):
        super().__init__()
        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [41, 46, 50, 51, 52, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()
