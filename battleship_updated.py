from random import randint

board = []  # empty board
print 'Enter the rows and columns in the board'

row_size = int(raw_input())
column_size = int(raw_input())

for x in range(row_size):
    board.append(["O"] * column_size)


def print_board(boar):
    for row in boar:
        print " ".join(row)


def random_row(boar):
    return randint(1, len(boar))


def random_col(boar):
    return randint(1, len(boar[0]))


print "Let's play Battleship!"
print_board(board)
print 'Length of board is ', len(board), len(board[0])
print 'How many times would you like to play ?'
repeat = int(raw_input())

for turn in range(repeat):
    ship_row = random_row(board)
    ship_col = random_col(board)
    # print ship_row, ship_col
    try:
        guess_row = int(raw_input("Guess Row:"))
        guess_col = int(raw_input("Guess Col:"))
    except:
        print"Please enter something valid."
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        board[guess_row - 1][guess_col - 1] = "X"
        print_board(board)
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print "Oops, that's not even in the ocean."
        else:
            if board[guess_row - 1][guess_col - 1] == "X":
                print "You guessed that one already."
            else:
                board[guess_row - 1][guess_col - 1] = "X"
                print "You missed my battleship!"
        print_board(board)
        print "The ship was at ", ship_row, ship_col
        print "Turn ", (turn + 1), " over"
        if turn == repeat:
            print"Game Over"
