#
# Description:
#   The following class creates a player for the game; holding information regarding the player's paddle and score. 
# Within it, two objects are stored as attributes: paddle & score.


# OOP Principles Used:
#   A principle used here is inheritance. 
#
# Reasoning:
#   This class inherits all the attributes and methods from the "Score" class.
#


from paddle import *
from score import *



class Player(Score):
    def __init__(self, isPlayer1):
        super().__init__()
        self.paddle = Paddle(isPlayer1)
        


    