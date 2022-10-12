from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# Creation de la fenetre d'Accueil
root = Tk()
master = root
screen_width = master.winfo_screenwidth()
screen_height = master.winfo_screenheight()
master.minsize(screen_width, screen_height)
master.title("Tic Tac Toe")
bgcolor1 ="NavajoWhite3"
master['background'] = bgcolor1
# for i in range(2):
#             master.rowconfigure(i,weight=1)
#             master.columnconfigure(i,weight=1)
s = ttk.Style()
s.theme_use('clam')
s = ttk.Style()
s.configure('mod0.TFrame',background= bgcolor1) #"light slate gray"
frame1 = ttk.Frame(master , style='mod0.TFrame')
frame1.grid(row=0, column=0, padx= 570, pady= 30)
frame2 = ttk.Frame(master , style='mod0.TFrame')
frame2.grid(row=1, column=0, pady= 70)
s.configure('mod0.TLabel', font=("Bold",42),background= bgcolor1 ,foreground="LightBlue4")
s.configure('mod1.TLabel', font=("Silkscreen",18),background= bgcolor1 ,foreground="LightBlue4")
labelIntro = ttk.Label(frame1, text='TIC TAC TOE' ,style="mod0.TLabel").grid(row=0, column=1, columnspan=3, sticky=(N))
labelMinimax = ttk.Label(frame1, text='AI:Minimax bot' ,style="mod1.TLabel").grid(row=1, column=1, columnspan=3, sticky=(N))

s2 = ttk.Style()
s2.configure('mod1.TButton',background="LightBlue4", foreground ="indian red",borderwidth=5, font=("Bold",25))


quitterBoutton=ttk.Button(frame2,text="Quit", style="mod1.TButton",command=master.destroy)
quitterBoutton.grid(row=4, column=3, pady= 70)
TryAgainBoutton=ttk.Button(frame2,text="Try Again", style="mod1.TButton")
TryAgainBoutton.grid(row=4, column=1, pady= 70)
#labelCredits = ttk.Label(frame2, text='Powered by:\n Amjad Chreim \n Karen Lteif \n Ali Rammal' ,style="mod1.TLabel").grid(row=4, column=6 ,padx= 20, sticky=(W,N))

s1 = ttk.Style()
s1.configure('mod0.TButton',background="LightBlue3", foreground ="LightBlue4",borderwidth=5, font=("Bold",25))

BOT_TURN = False
someone_won = False
count = 0


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


def jouer(index):
    global BOT_TURN, count
    if board[index] != " ":
        print("Button is already clicked!")
        tkinter.messagebox.showwarning(title="Warning!", message="Button already Clicked!")

    elif board[index] == " " and BOT_TURN:
        count += 1
        comMove()


    elif board[index] == " " and BOT_TURN == False:
        count += 1
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
def colorChecker(symbol, boutton) :
    if (symbol=="X"):
        boutton['text'] = symbol
        s1.configure('mod0.TButton',background="LightBlue3", foreground ="indian red",borderwidth=5, font=("Bold",25))
    if (symbol=="O"):
        boutton['text'] = symbol
        s1.configure('mod0.TButton',background="LightBlue3", foreground ="LightBlue4",borderwidth=5, font=("Bold",25))


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


def playerMove():
    global BOT_TURN, someone_won
    BOT_TURN = True
    if checkWhoWon("O"):
        print("player win")
        tkinter.messagebox.showwarning(title="Congrats!", message="Player Win!")
        someone_won = True

    comMove()


def comMove():
    global BOT_TURN, someone_won
    BOT_TURN = False
    bestScore = -1
    bestMove = 0  # will be changed

    for key in board.keys():
        if board[key] == ' ':
            board[key] = 'X'
            score = minimax(board, False)
            board[key] = ' '

            if score > bestScore:
                bestScore = score
                bestMove = key
    # jouer(bestMove, 'X')
    board[bestMove] = "X"
    updateButtons()
    if checkWhoWon("X"):
        print("bot win")
        tkinter.messagebox.showwarning(title="Congrats!", message="Bot Win!")
        someone_won = True

    if count == 9 and someone_won == False:
        tkinter.messagebox.showwarning(title="Fin!", message="Draw!")


b1 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(1))
b2 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(2))
b3 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(3))
b4 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(4))
b5 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(5))
b6 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(6))
b7 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(7))
b8 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(8))
b9 = ttk.Button(frame2, text=' ', style="mod0.TButton", command=lambda: jouer(9))

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

# PROG PRINCIPAL:
# ================


# PROGRAMME PRINCIPALE:
if __name__ == '__main__':
    root.mainloop()
