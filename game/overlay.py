#
# Description:
#   The following class creates the ball for the game. 
# Within it, we specify the balls physical attrites like its shape, color, and speed.
#This class also includes the methods that controls the balls movements and behaviors when interacting
#with the paddles and the game's boundaries.


# OOP Principles Used:
#   A little of encapsulation is used.
#
# Reasoning:
#   
#The class also features an encapsulation design by making some of its attributes private and only accessible through methods.
#
#This class stores some actors as attributes.It creates the actors using other classes, but it does not inherit the nature of these other classes.



import turtle
import constants

class Overlay:
    def __init__(self, player1, player2):
        self._color = constants.TEXT_COLOR
        self._font = constants.TEXT_FONT
        #self.text = self.create_text(player1, player2)
        self.divider = self.create_divider()
        self.pen = self.create_pen()

    def create_pen(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color('white')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        return pen

    def create_divider(self):
        lines = turtle.Turtle()
        lines.speed(0)
        lines.shape('square')
        lines.color('white')
        lines.shapesize(stretch_wid=1, stretch_len=.5)
        lines_dy = -300
        for i in range(0, 100):
            lines.penup()
            lines.sety(lines_dy)
            lines.stamp()
            lines_dy += 40


    def get_color(self):
        return self._color

    def get_font(self):
        return self._font

    def update_text(self, player1, player2):
        self.pen.write('Player A: {}                  Player B: {}'.format(player1.get_score(), player2.get_score()), align='center', font=(self.get_font(), 24))