import random


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


def checkWhoWon(letter):
    if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == letter:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == letter:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == letter:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == letter:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == letter:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == letter:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == letter:
        return True

    else:
        return False


def playerMove():
    position = int(input("Position O:"))
    insertLetter('O', position)
    return


def comMove():
    bestScore = -1
    bestMove = 0  # will be changed

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax_alphaBeta(board, False, -100, 100)
            board[key] = ' '

            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter('X', bestMove)


def minimax(board, isMaximizing):
    if checkWhoWon('X'):
        return 1
    elif checkWhoWon('O'):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1

        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, False)
                board[key] = ' '

                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 1
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, True)
                board[key] = ' '

                if score < bestScore:
                    bestScore = score
        return bestScore


def expectimax(board, botturn):
    count = 0
    for key in board.keys():
        if board[key] == ' ':
            count += 1
    if checkWhoWon('X'):
        return 1
    elif checkWhoWon('O'):
        return -1
    elif checkDraw():
        return 0
    if botturn:
        bestScore = -1

        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = expectimax(board, False)
                board[key] = ' '

                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 0
        for key in board.keys():
            proba = 1 / count
            print(proba)
            if board[key] == ' ':
                board[key] = 'O'
                bestScore += proba * expectimax(board, True)
                board[key] = ' '
        print(bestScore)
        return bestScore


def minimax_alphaBeta(board, isMaximizing, alpha, beta):
    if checkWhoWon('X'):
        return 1
    elif checkWhoWon('O'):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax_alphaBeta(board, False, alpha, beta)
                board[key] = ' '

                if score > bestScore:
                    bestScore = score

                if bestScore >= beta:
                    return bestScore
                if bestScore > alpha:
                    alpha = bestScore

        return bestScore
    else:
        bestScore = 100
        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax_alphaBeta(board, True, alpha, beta)
                board[key] = ' '

                if score < bestScore:
                    bestScore = score
                if bestScore <= alpha:
                    return bestScore
                if bestScore < beta:
                    beta = bestScore
        return bestScore


while not checkWin():
    # place = random.randrange(1,10)
    # board[1] = 'X'
    playerMove()
    comMove()

from tkinter import ttk
from tkinter import *

# root = Tk()
# root.minsize(400, 800)
# root.title('Tic-Tac-Toe')
#
# frame1 = ttk.Frame(root, padding=(20, 20), relief=SUNKEN)
# frame1.grid(row=2, column=0)
# button1 = ttk.Button(frame1, text='.')
#
# frame2 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame2.grid(row=2, column=1)
# button2 = ttk.Button(frame1, text='.')
# button2.grid()
#
# frame3 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame3.grid(row=2, column=2)
# button3 = ttk.Button(frame1, text='.')
#
# frame4 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame4.grid(row=3, column=0)
#
# frame5 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame5.grid(row=3, column=1)
#
# frame6 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame6.grid(row=3, column=2)
#
# frame7 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame7.grid(row=4, column=0)
#
# frame8 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame8.grid(row=4, column=1)
#
# frame9 = ttk.Frame(root, padding = (20, 20), relief=SUNKEN)
# frame9.grid(row=4, column=2)
