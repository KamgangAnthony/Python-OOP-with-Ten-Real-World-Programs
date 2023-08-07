class Shape:

    def __init__(self, shape_type, starting_coordinates, width, height, colorRGB):
        self.colorRGB = colorRGB
        self.height = height
        self.width = width
        self.starting_coordinates = starting_coordinates
        self.shape_type = shape_type

    def add_shape_info_to_data(self, data):
        x = self.starting_coordinates[0]
        y = self.starting_coordinates[1]
        r = self.colorRGB[0]
        g = self.colorRGB[1]
        b = self.colorRGB[2]

        if self.shape_type.lower() == "square":
            self.height = self.width

        data[x: (x + self.width + 1), y: (y + self.height + 1)] = [r, g, b]

        return data
