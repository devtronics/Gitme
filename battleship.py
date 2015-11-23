#!/usr/bin/env python
# Copyright 2015 Chris Heckler <hecklerchris@hotmail.com>
# GNU Affero General Public License version 3 (see the file LICENSE).


from random import randint

board = []


for number in range(5):
    o = ["O"] * 5
    board.append(o)
    # created 5 rows with 5 Os to
    #create the battleship board """

def print_board(board):
    for row in board:
        print " ".join(row)
    # comma's and brackets removed and board cleaned up
print "Let's play Battleship!"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
    # 2 functions to find a random row & column value for ship

ship_row = random_row(board)
ship_col = random_col(board)



for turn in range(4):
    print "Turn", turn + 1

    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break
    else:

        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

    if turn == 3:
        print "Game Over"
        break
    print_board(board)
