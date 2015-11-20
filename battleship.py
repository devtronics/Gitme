board = []

for number in range(5):
    o = ["O"] * 5
    print o
    board.append(o)
    """ created 5 rows with 5 Os to
        create the battleship board """

def print_board(board):
    for row in board:
        print " ".join(row)
    # comma's and brackets removed and board cleaned up

print_board(board)

