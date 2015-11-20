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

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)
    # 2 functions to find a random row & column value for ship

ship_row = random_row(board)
ship_col = random_col(board)

print ship_row
print ship_col

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"

