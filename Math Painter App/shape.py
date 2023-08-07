class Shape:

    def __init__(self, shape_type, starting_coordinates, width, height, colorRGB):
        self.colorRGB = colorRGB
        self.height = height
        self.width = width
        self.starting_coordinates = starting_coordinates
        self.shape_type = shape_type

    def add_shape_info_to_data(self, canvas):
        x = self.starting_coordinates[0]
        y = self.starting_coordinates[1]
        r = self.colorRGB[0]
        g = self.colorRGB[1]
        b = self.colorRGB[2]

        if self.shape_type.lower() == "square":
            self.height = self.width

        canvas.data[x: (x + self.width), y: (y + self.height)] = [r, g, b]


