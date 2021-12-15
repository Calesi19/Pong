#
# Description:
#   The following class holds the methods and attributes necessary to create a window screen for the game to run in. It also
# contains the methods to that describe the windows behavior when the game ends. It also contains the methods that allow the
# window to accept inputs from the users.


# OOP Principles Used:
#   A little of encapsulation is used. A principle used here is inheritance. 
#
# Reasoning:
#   
# The class also features an encapsulation design by making some of its attributes private and only accessible through methods.
#



import turtle
import constants


class Screen:
    def __init__(self, title = constants.SCREEN_TITLE):
        
        self._width = constants.SCREEN_WIDTH
        self._height = constants.SCREEN_HEIGHT
        self._color = constants.SCREEN_BACKGROUND_COLOR
        self._title = title
        self.window = self.create_window()


    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height

    def get_color(self):
        return self._color
    
    def get_title(self):
        return self._title

    def create_window(self):
        wn = turtle.Screen()
        wn.title(self.get_title())
        wn.bgcolor(self.get_color())
        wn.setup(self.get_width(), self.get_height())
        wn.tracer(0)
        return wn

    def end_game(self, score1, score2, overlay):
        self.window.bgcolor('white')
        self.window.setup(width=800, height=600)
        self.window.tracer(0)
        overlay.pen.color('black')
        overlay.pen.goto(0, 0)
        if score1 > score2:
            overlay.pen.write("You win player A", align='center', font=('Meatball', 24))
        else:
            overlay.pen.write("You win player B", align='center', font=('Meatball', 24))
        
        self.window.tracer(0)

    def define_controls(self, player1, player2):
        self.window.onkeypress(player1.paddle.moveUp, constants.PLAYER1_UP_KEY)
        self.window.onkeypress(player1.paddle.moveDown, constants.PLAYER1_DOWN_KEY)

        self.window.onkeypress(player2.paddle.moveUp, constants.PLAYER2_UP_KEY)
        self.window.onkeypress(player2.paddle.moveDown, constants.PLAYER2_DOWN_KEY)
        

    
        


