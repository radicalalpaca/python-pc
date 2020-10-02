"""
Simple tic-tac-toe game vs computer.
"""

import random
from collections import deque

crosses = True
num_X = 0
num_O = 0


def input_board_check(list_input):
    """
    Checks if user-inputted board is valid, i.e. it contains only
    "O", "X" or "_".
    :param list_input:
    :return: True
    """
    for character in list_input:
        if character != "_" and character != "O" and character != "X":
            return True
        else:
            continue


def user_input_check(list_input):
    """
    Checks if users input is valid, i.e. it contains only
    numbers 1, 2 or 3.
    :param list_input:
    :return: True
    """
    for number in list_input:
        if int(number) > 3 or int(number) < 1:
            return True
        else:
            continue


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


def input_board():
    """
    User-inputted board. Must contain exactly 9 characters; "_", "X" or "O".
    :return: [board_input, board_input_list]
    """
    while True:
        board_input = input("Enter cells: ")
        board_input_list = deque([i for i in board_input])
        if len(board_input_list) != 9:
            print("Must contain 9 characters.")
            continue
        elif input_board_check(board_input_list):
            print("Invalid character(s).")
            continue
        else:
            for row in range(3):
                for element in range(3):
                    if board_input_list[0] == "_":
                        board_input_list.popleft()
                        board_input[row].append(" ")
                    else:
                        board_input[row].append(board_input_list.popleft())
            break
    return [board_input, board_input_list]


def draw_board(board_input):
    """
    Outputs board in a pretty way.
    :param board_input:
    """
    print("---------")
    for i in range(3):
        print("| " + board_input[i][0] + " " + board_input[i][1] + " " + board_input[i][2] + " |")
    print("---------")


def next_move():
    """
    Takes user's next move and adds it to the board. Checks input is
    valid. If user inputted board, then decides whether to use "X" or "O".
    :return: board
    """
    global num_X
    global num_O

    for character in board[1]:
        if character == "X":
            num_X += 1
        elif character == "O":
            num_O += 1

    while True:
        user_move = [i for i in input("Enter the coordinates: ").split()]
        if not is_number(user_move):
            print("You should enter numbers!")
            continue
        elif user_input_check(user_move):
            print("Coordinates should be from 1 to 3!")
            continue
        elif board[abs(int(user_move[1]) - 3)][int(user_move[0]) - 1] == " ":
            if crosses:
                board[abs(int(user_move[1]) - 3)][int(user_move[0]) - 1] = "X"
                break
            else:
                board[abs(int(user_move[1]) - 3)][int(user_move[0]) - 1] = "O"
                break
        else:
            print("This cell is occupied! Choose another one!")
            continue
    return board


def win_check(board_input):
    """
    Checks if board satisfies win condition.

    :param board_input:
    :return: True
    """
    for row in range(3):
        for col in range(3):
            if board_input[col][0] == board_input[col][1] == board_input[col][2] != " ":
                return True
            elif board_input[0][row] == board_input[1][row] == board_input[2][row] != " ":
                return True
            elif board_input[0][0] == board_input[1][1] == board_input[2][2] != " ":
                return True
            elif board_input[2][0] == board_input[1][1] == board_input[0][2] != " ":
                return True
            else:
                continue


def computer_move():
    """
    Generates random move for the computer, and adds it to the board.

    :return: board
    """
    global crosses
    crosses = False
    print('Making move level "easy"')
    while True:
        computer_input = random.sample(range(3), 2)
        if board[computer_input[0]][computer_input[1]] == " ":
            board[computer_input[0]][computer_input[1]] = "O"
            break
        else:
            continue
    return board


if __name__ == '__main__':
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while True:
        draw_board(board)
        board = next_move()
        if win_check(board) and crosses:
            draw_board(board)
            print("X wins")
            break
        elif win_check(board) and not crosses:
            draw_board(board)
            print("O wins")
            break
        elif num_X + num_O == 8:
            draw_board(board)
            print("Draw")
            break
        else:
            draw_board(board)
            board = computer_move()
            continue
