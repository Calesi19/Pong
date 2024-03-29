#
# Description:
#   The following class creates a paddle for the game. 
# Within it, we specify the paddle's physical attributes like its shape, color, and speed.
# This class also includes the methods that controls the paddles movements.


# OOP Principles Used:
#   A little of encapsulation is used. A principle used here is inheritance. Some slighlty insignificant polymorphysm is used.
#   Abstraction is used.
#
# Reasoning:
#   
#The class also features an encapsulation design by making some of its attributes private and only accessible through methods.
#This classes inherits from the Turtle class. The Turtle class holds methods
# and attributes that allow the program to draw the paddle and track its position.
# You could consider the methods moveUp and moveDown an application of polymorphysm; alot of actors use have the attributes neccessary
# for these methods to work on them. In this case, they are only restricted to the paddle class since only the paddle class needs them.
# These methods work on any paddle regardless of its shape, color, or size.
# These same methods that allow of the paddles to move are an example of abstractions. The coordinates of these paddles are being
# manipulated, yet the user only needs to call either the moveUp() or moveDown() methods to control the paddles; the math involved in this is hidden.




import constants
from turtle import *

class Paddle(Turtle):
    def __init__(self, isPlayer1):
        super().__init__()
        
        self._speed = constants.PADDLE_MOVEMENT_SPEED
        self._shape = constants.PADDLE_SHAPE
        self._border_color = constants.PADDLE_BORDER_COLOR

        if isPlayer1:
            self._fill_color = constants.PLAYER1_PADDLE_FILL_COLOR
        else:
            self._fill_color = constants.PLAYER2_PADDLE_FILL_COLOR

        self._width = constants.PADDLE_WIDTH
        self._height = constants.PADDLE_HEIGHT

        if isPlayer1:
            self._inverter = 1
        else:
            self._inverter = -1


        self.speed(0)
        self.shape(self.get_shape())
        self.color(self.get_border_color())
        self.shapesize(self.get_width(), self.get_height())
        self.penup()
        self.goto(350 * self._inverter, 0)
        self.fillcolor(self.get_fill_color())

    def get_speed(self):
        return self._speed

    def get_shape(self):
        return self._shape

    def get_border_color(self):
        return self._border_color

    def get_fill_color(self):
        return self._fill_color

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def moveUp(self):
        self.sety(self.ycor() + 20)

    def moveDown(self):
        self.sety(self.ycor() - 20)


