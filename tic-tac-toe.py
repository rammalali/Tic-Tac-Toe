def create_board(board):
    for i in range(1, 10):
        board[i] = ' ';
    return board;

board = create_board({})


def printBoard(board):
    for i in range(3):
        line = ''
        for j in range(1, 4):
            line = line + '|' + board[j+i*3]
        line += '|'
        print(" - - - ")
        print(line)

printBoard(board)

# def spaceIsFree(position):
#

