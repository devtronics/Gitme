from random import randint

board = []
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))
# takes userinput for row and col to "seek" hidden ship



 for number in range(5):
    o = ["O"] * 5
    print o
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

print ship_row
print ship_col

for turn in range(4);
    print "Turn", turn + 1
     if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"

    else:

        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
         else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"

    print_board(board)
