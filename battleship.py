from random import randint
board = []
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)
print len(board)
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

for turn in range (4):
    ship_row = random_row(board)
    ship_col = random_col(board)
    try :
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    except :
        print"enter something valid . "
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print_board(board)
        print "The ship was at " , ship_row , ship_col
        print "Turn ", turn+1 , " over"
        if turn==3 :
            print"Game Over"