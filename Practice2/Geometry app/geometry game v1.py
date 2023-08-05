import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, ractangle):
        if (ractangle.lowleft.x < self.x < ractangle.upright.x) and \
                (ractangle.lowleft.y < self.y < ractangle.upright.y):
            return True
        else:
            return False

    def distance_to_point(self, our_point):
        return math.sqrt(math.pow((our_point[0] - self.x), 2) + math.pow((our_point[1] - self.y), 2))

class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

    def has_an_area_of(self):
        return (abs(self.lowleft.x - self.upright.x) * abs(self.lowleft.y - self.upright.y))
import turtle

class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.lowleft.x, self.lowleft.y)
        canvas.pendown()

        canvas.forward(abs(self.upright.x - self.lowleft.x))
        canvas.left(90)
        canvas.forward(abs(self.upright.y - self.lowleft.y))
        canvas.left(90)
        canvas.forward(abs(self.upright.x - self.lowleft.x))
        canvas.left(90)
        canvas.forward(abs(self.upright.y - self.lowleft.y))




class GuiPoint(Point):

    def draw(self, canvas, size = 5, color = 'red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


from random import randint

our_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), Point(randint(10, 400), randint(10, 400)))

print("Our Rectangle coordinates:" ,
      our_rectangle.upright.x , "," ,
      our_rectangle.upright.y , " and " , our_rectangle.lowleft.x , ", " , our_rectangle.lowleft.y)

user_point_x = float(input("X Coordinate : "))
user_point_y = float(input("Y Coordinate : "))
user_point = GuiPoint(user_point_x, user_point_y)
user_area = float(input("Guess the area of the rectangle : "))

print("Is your point inside the rectangle : ", user_point.falls_in_rectangle(our_rectangle))
print("Did you guess the area right ? : ", user_area == our_rectangle.has_an_area_of(), "\nActual area : ",
      our_rectangle.has_an_area_of())

small_turtle = turtle.Turtle()
our_rectangle.draw(small_turtle)

user_point.draw(small_turtle)
turtle.done()