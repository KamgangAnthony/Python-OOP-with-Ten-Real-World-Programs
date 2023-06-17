"""A rectangle geometry game.
The classes should be
Point
Point should have two private instance variables, x and y, that represent the coordinates of the point.
It should have a constructor that takes two parameters, x and y, and initializes the instance variables.
It should have a method called distance that takes a Point as a parameter and returns the distance between
the two points as a double. It should have a method called falls_in_rectangle that takes a Rectangle as an attribute and determines
if the point falls in the rectangle.

Rectangle
Rectangle should have two private instance variables, lower_left and upper_right, that represent the corners of the rectangle.

RectangleGame
RectangleGame should have a main method that creates a Point and a Rectangle and then determines if the point falls in the rectangle.

"""

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def falls_in_rectangle(self, other):
        if other.lower_left.x < self.x < other.upper_right.x and other.lower_left.y < self.y < other.upper_right.y:
            return True
        else:
            return False