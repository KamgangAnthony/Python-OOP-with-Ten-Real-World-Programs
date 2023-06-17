class Circle:

    VALID_COLORS = ("Blue", "Green", "Red")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius

        else:
            print("Please enter a valid radius")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color

        else:
            print("Please enter a valid color.")

    color = property(get_color, set_color)


my_circle = Circle(15, "Blue")
print(my_circle.get_radius())

my_circle.set_radius("What the fuck !!!")
print(my_circle.get_radius())