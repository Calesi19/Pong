#
# Description:
#   The following class creates the ball for the game. 
# Within it, we specify the balls physical attributes like its shape, color, and speed.
#This class also includes the methods that controls the balls movements and behaviors when interacting
#with the paddles and the game's boundaries.


# OOP Principles Used:
#   A principle used here is inheritance. 
#
# Reasoning:
#   Since this classes inherits from the Turtle class. The Turtle class holds methods
# and attributes that allow the program to draw the ball and track its position.
#



import constants
import time
from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.speed(0)
        self.shape('circle')
        self.color(constants.BALL_COLOR)
        self.penup()
        self.goto(0, 0)
        self.dx = .1
        self.dy = .1
        
        

    def move_freely(self):
        for i in range(0, constants.BALL_MOVEMENT_SPEED):
            self.setx(self.xcor() + self.dx)
            self.sety(self.ycor() + self.dy)

    def check_collision(self, player1, player2, screen_overlay):
        if self.ycor() > 290:
            self.sety(290)
            self.dy *= -1
            
        if self.ycor() < -290:
            self.sety(-290)
            self.dy *= -1

        if self.xcor() > 390:
            self.goto(0, 0)
            self.dx *= -1
        
            player1.add_point()
    
            screen_overlay.pen.clear()
            screen_overlay.update_text(player1, player2)
            time.sleep(1)
                    

        if self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1
        
            player2.add_point()

            screen_overlay.pen.clear()
            screen_overlay.update_text(player1, player2)
            time.sleep(1)
            

        if self.xcor() > 335 and (self.ycor() < player1.paddle.ycor() + 40 and self.ycor() > player1.paddle.ycor() - 40):
            self.setx(335)
            self.dx *= -1

        if self.xcor() < -335 and (self.ycor() < player2.paddle.ycor() + 40 and self.ycor() > player2.paddle.ycor() - 40):
            self.setx(-335)
            self.dx *= -1
            
        
        