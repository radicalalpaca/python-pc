"""
Tic tac toe game vs ai with OOP.
"""

import random


def is_number(list_input):
    """
    Checks if list contains only integers.
    :param list_input:
    :return: Boolean
    """
    for number in list_input:
        try:
            int(number)
            return True
        except ValueError:
            return False


class Board:
    """Board"""

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def draw_board(self):
        print("---------")
        for i in range(3):
            print("| " + self.board[i][0] + " " + self.board[i][1] + " " + self.board[i][2] + " |")
        print("---------")
