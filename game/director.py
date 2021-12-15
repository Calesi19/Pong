#
# Description:
#   This is the director class. Its purpose it to control all the other components of the program,
# by creating all the actors and starting the necessary sequences for the program to run.


# OOP Principles Used:
#   No principles are used here. This class stores its actors as attributes. 
#
# Reasoning:
#   It creates the actors using other classes, but it does not inherit the nature of these other classes.
#



import screen
from ball import *
from score import *
from overlay import *
from player import *
import constants
import time


class Director:
    def __init__(self):


        self.screen = screen.Screen()

        self.player1 = Player(True)
        self.player2 = Player(False)

        self.ball = Ball()

        self.screen_overlay = Overlay(self.player1, self.player2)
        self.screen_overlay.update_text(self.player1, self.player2)

        self.screen.window.listen()
        self.screen.define_controls(self.player1, self.player2)

        time.sleep(1)

        


    def start_game(self):
        while True:
            
            self.screen.window.update()
            self.ball.move_freely()
                

            self.ball.check_collision(self.player1, self.player2, self.screen_overlay)

            if self.player1.get_score() == constants.OBJECTIVE or self.player2.get_score() == constants.OBJECTIVE:
                break

    def end_game(self):
        self.screen_overlay.pen.clear()
        self.screen.end_game(self.player1.get_score(), self.player2.get_score(), self.screen_overlay)
        self.screen_overlay.pen.hideturtle()
        while True:
            self.screen.window.update()

