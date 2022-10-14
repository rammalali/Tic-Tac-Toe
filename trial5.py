from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import os
import sys

# Creation de la fenetre d'Accueil

master = Tk()
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
master.minsize(screen_width, screen_height)
master.title("Tic Tac Toe")
bgcolor1 = "#E2FFDE"
master['background'] = bgcolor1
# for i in range(2):
#             master.rowconfigure(i,weight=1)
#             master.columnconfigure(i,weight=1)
s = ttk.Style()
s.theme_use('clam')
s = ttk.Style()
s.configure('mod0.TFrame', background=bgcolor1)  # "light slate gray"
frame1 = ttk.Frame(master, style='mod0.TFrame')
frame1.grid(row=0, column=0, padx=570, pady=30)
frame2 = ttk.Frame(master, style='mod0.TFrame')
frame2.grid(row=1, column=0, pady=70)
s.configure('mod0.TLabel', font=("Bold", 42), background=bgcolor1, foreground="LightBlue4")
s.configure('mod1.TLabel', font=("Silkscreen", 18), background=bgcolor1, foreground="LightBlue4")
ttk.Label(frame1, text='TIC TAC TOE', style="mod0.TLabel").grid(row=0, column=1, columnspan=3, sticky=N)
ttk.Label(frame1, text='AI:Minimax bot', style="mod1.TLabel").grid(row=1, column=1, columnspan=3,
                                                                   sticky=N)

ttk.Button(frame1, text='Change Game Type', style="mod1.TButton", command=lambda: button_type()).grid(
    row=2, column=1, columnspan=3,
    sticky=N)

s2 = ttk.Style()
s2.configure('mod1.TButton', background="LightBlue4", foreground="indian red", borderwidth=5, font=("Bold", 25))

quitterBoutton = ttk.Button(frame2, text="Quit", style="mod1.TButton", command=master.destroy)
quitterBoutton.grid(row=4, column=3, pady=70)

# labelCredits = ttk.Label(frame2, text='Powered by:\n Amjad Chreim \n Karen Lteif \n Ali Rammal' ,
# style="mod1.TLabel").grid(row=4, column=6 ,padx= 20, sticky=(W,N))

s1 = ttk.Style()
s1.configure('mod1.TButton', background="LightBlue3", foreground="LightBlue4", borderwidth=5, font=("Bold", 25))
s2 = ttk.Style()
s2.configure('mod2.TButton', background="LightBlue3", foreground="indian red", borderwidth=5, font=("Bold", 25))

BOT_TURN = False
button_is_minimax = True
someone_won = False
count = 0


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


def create_board(board):
    for i in range(1, 10):
        board[i] = ' '
    return board


board = create_board({})


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def checker(letter):
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


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkWin():
    print("Checking if someone won: ", board)
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
    n = 0
    for key in board.keys():
        if board[key] == ' ':
            n += 1
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
            proba = 1 / n
            # print(proba)
            if board[key] == ' ':
                board[key] = 'O'
                bestScore += proba * expectimax(board, True)
                board[key] = ' '
        # print(bestScore)
        return bestScore


def jouer(index):
    global BOT_TURN, count
    if board[index] != " ":
        print("Button is already clicked!")
        tkinter.messagebox.showwarning(title="Warning!", message="Button already Clicked!")

    elif board[index] == " " and BOT_TURN:
        comMove()

    elif board[index] == " " and BOT_TURN == False:
        board[index] = "O"
        updateButtons()
        playerMove()
        checkWhoWon("X")


# def updateButtons():
#     b1['text'] = board[1]
#     b2['text'] = board[2]
#     b3['text'] = board[3]
#     b4['text'] = board[4]
#     b5['text'] = board[5]
#     b6['text'] = board[6]
#     b7['text'] = board[7]
#     b8['text'] = board[8]
#     b9['text'] = board[9]
def colorChecker(symbol, boutton):
    if symbol == "X":
        boutton['text'] = symbol

    if symbol == "O":
        boutton['text'] = symbol

    if symbol == " ":
        boutton['text'] = symbol
        boutton['state'] = NORMAL


def updateButtons():
    colorChecker(board[1], b1)
    colorChecker(board[2], b2)
    colorChecker(board[3], b3)
    colorChecker(board[4], b4)
    colorChecker(board[5], b5)
    colorChecker(board[6], b6)
    colorChecker(board[7], b7)
    colorChecker(board[8], b8)
    colorChecker(board[9], b9)


def disable_all():
    b1["state"] = DISABLED
    b2["state"] = DISABLED
    b3["state"] = DISABLED
    b4["state"] = DISABLED
    b5["state"] = DISABLED
    b6["state"] = DISABLED
    b7["state"] = DISABLED
    b8["state"] = DISABLED
    b9["state"] = DISABLED


def playerMove():
    global BOT_TURN, someone_won, count
    BOT_TURN = True
    count += 1
    if checkWhoWon("O"):
        print("player win")
        tkinter.messagebox.showwarning(title="Congrats!", message="Player Win!")
        someone_won = True

    comMove()


def checkWhoWonTkinter(letter):
    if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
        s1.configure
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


def button_type():
    global button_is_minimax

    if button_is_minimax:

        ttk.Label(frame1, text="AI:ExpectiMax bot", style="mod1.TLabel").grid(row=1, column=1, columnspan=3, sticky=N)

        button_is_minimax = False

    else:
        ttk.Label(frame1, text="   AI:Minimax bot   ", style="mod1.TLabel").grid(row=1, column=1, columnspan=3,
                                                                                 sticky=N)

        button_is_minimax = True


def comMove():
    global BOT_TURN, someone_won, count, button_is_minimax
    BOT_TURN = False
    count += 1
    bestScore = -1
    bestMove = 0  # will be changed

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            if button_is_minimax:
                print("mini")
                score = minimax(board, False)
            else:
                print("expct")
                score = expectimax(board, False)
            board[key] = ' '

            if score > bestScore:
                bestScore = score
                bestMove = key
    # jouer(bestMove, 'X')
    board[bestMove] = "X"
    updateButtons()
    if checkWhoWon("X"):
        print("bot win")
        disable_all()
        checkWhoWonTkinter("X")

        tkinter.messagebox.showwarning(title="Congrats!", message="Bot Win!")
        someone_won = True

    # print(count)
    if count == 10 and someone_won == False:
        disable_all()
        tkinter.messagebox.showwarning(title="Fin!", message="Draw!")


def TryAgain(board=board):
    global BOT_TURN
    global someone_won
    global count
    for index in board.keys():
        board[index] = " "
    BOT_TURN = False
    someone_won = False
    count = 0
    updateButtons()


b1 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(1))
b2 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(2))
b3 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(3))
b4 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(4))
b5 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(5))
b6 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(6))
b7 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(7))
b8 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(8))
b9 = ttk.Button(frame2, text=' ', style="mod1.TButton", command=lambda: jouer(9))

liste_bouttons = [b1, b1, b2, b3, b4, b5, b6, b7, b8, b9]

b1.grid(row=1, column=1, ipady=45)
b2.grid(row=1, column=2, ipady=45)
b3.grid(row=1, column=3, ipady=45)
b4.grid(row=2, column=1, ipady=45)
b5.grid(row=2, column=2, ipady=45)
b6.grid(row=2, column=3, ipady=45)
b7.grid(row=3, column=1, ipady=45)
b8.grid(row=3, column=2, ipady=45)
b9.grid(row=3, column=3, ipady=45)

TryAgainBoutton = ttk.Button(frame2, text="Try Again", style="mod1.TButton", command=TryAgain)
TryAgainBoutton.grid(row=4, column=1, pady=70)
# PROG PRINCIPAL:
# ================


# PROGRAMME PRINCIPALE:
if __name__ == '__main__':
    master.mainloop()
