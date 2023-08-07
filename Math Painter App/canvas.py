import os

import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, width, height, color_black_or_white):
        self.color_black_or_white = color_black_or_white
        self.width = width
        self.height = height

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        if self.color_black_or_white.lower() == "black":
            self.data[:] = [0, 0, 0]

        elif self.color_black_or_white.lower() == "white":
            self.data[:] = [255, 255, 255]

    # def send_data(self):
    #     data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
    #
    #     if self.color_black_or_white.lower() == "black":
    #         data[:] = [0, 0, 0]
    #
    #     elif self.color_black_or_white.lower() == "white":
    #         data[:] = [255, 255, 255]
    #
    #     return data

    def export_the_image(self, data):
        img = Image.fromarray(data, 'RGB')
        os.chdir("files")
        img.save('canvas.png')
        return ""
