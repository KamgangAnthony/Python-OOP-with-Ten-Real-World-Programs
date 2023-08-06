from PIL import Image


class ImageDrawer:

    def __init__(self, data):
        self.data = data

    def export_the_image(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save('canvas.png')
        return ""
