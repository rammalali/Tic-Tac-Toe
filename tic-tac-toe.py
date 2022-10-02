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
        if checkWin():
            if letter == 'X':
                print("Bot Win !")
                exit()
            else:
                print("Player Wins!")
                exit()
        if checkDraw():
            print("Draw!")
            exit()
        return

    else:
        print("can't Insert there!")
        position = int(input("Enter New position: "))
        insertLetter(letter, position)


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True

    else:
        return False


def playerMore():
    position = int(input("Position O:"))
    insertLetter('O', position)
    return

def comMove():
    position = int(input("Position X:"))
    insertLetter('X', position)
    return
