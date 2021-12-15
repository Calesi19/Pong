#
# Description:
#   The following class only tracks the a score which defaults to zero the first time an instance of this class is created.
# This class holds methods necessary to fetch or change the score.


# OOP Principles Used:
#   Encapsulation is a principle used in this class.
#
# Reasoning:
#   The score attribute is only accessible through methods.
#

class Score:
    def __init__(self):
        self._score = 0

    def set_score(self, score):
        self._score = score

    def add_point(self):
        self._score += 1

    def get_score(self):
        return self._score

    