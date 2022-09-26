def create_board(board_input):
    for i in range(1, 10):
        board_input[i] = ' '
    return board_input


board = create_board({})


def printBoard(board_input):
    for i in range(3):
        line = ''
        for j in range(1, 4):
            line = line + '|' + board_input[j + i * 3]
        line += '|'
        print(" - - - ")
        print(line)



def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == 'X':
                print("Bot Win !")
                exit()
            else:
                print("Player Wins!")
                exit()
        return


    else:
        print("can't Insert there!")
        position = int(input("Enter New position: "))
        insertLetter(letter, position)

def checkDraw():
    pass


def checkWin():
    pass