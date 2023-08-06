import numpy as np


class Canvas:

    def __init__(self, width, height, color_black_or_white):
        self.color_black_or_white = color_black_or_white
        self.width = width
        self.height = height

    def send_data(self):
        data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        if self.color_black_or_white.lower() == "black":
            data[:] = [0, 0, 0]

        elif self.color_black_or_white.lower() == "white":
            data[:] = [255, 255, 255]

        return data
