"""Geometry class
Instance attributes will be x1, y1, x2, y2
Instance methods will be __init__, containsPoint
    containsPoint will take in x and y from the user and determine if they are within the rectangle.
        It will return True if they are and False if they are not.

Game file
import the geometry class
import the random library




create a while loop that will run until the user enters a 0
    print("Welcome to the Geometry Game")
    print("You will be given the four coordinates of a rectangle")
    print("You will be asked to enter a coordinate")
    print("If the coordinate is within the rectangle, you will get a hit")
    print("If the coordinate is not within the rectangle, you will get a miss")
    print("If you want to quit, enter 0, press any key to continue")
    print("Good luck!")
    create a rectangle object
    print("Rectangle Coordinates: x1, y1, x2, y2")
    ask the user for an x and y coordinate
    print("Guess point x coord: ")
    Take his input and store it in a variable
    print("Guess point y coord: ")
    Take his input and store it in a variable
    if the user enters a coordinate that is within the rectangle,
    print("Your point was inside the rectangle")
    if the user enters a coordinate that is not within the rectangle, print "miss"
    print("Your point was outside the rectangle")
    print("Do you want to play again? Press any key to continue or 0 to quit")
    if the user enters a 0, break out of the loop"""

class geometry:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def containsPoint(self, x, y):
        if self.x1 < x < self.x2 and self.y1 < y < self.y2:
            return True
        else:
            return False