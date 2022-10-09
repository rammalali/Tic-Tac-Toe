from tkinter import *
from tkinter import ttk


#Creation de la fenetre d'Accueil
root = Tk()
master=root
screen_width =master.winfo_screenwidth()
screen_height =master.winfo_screenheight()
master.minsize(screen_width,screen_height)
master.title("Tic Tac Toe")
master['background']="dark slate gray"
frame = Frame(master)
frame.grid(row=0, column=0)
labelIntro = ttk.Label(frame, text='TIC TAC TOE').grid(row=0,column=1,columnspan=3,sticky=(N))



BOT_TURN= True
USER_TURN=False
LAST_PLAY=int

def create_board(board):
    for i in range(1, 10):
        board[i] =' '
    return board

board=create_board({})



def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def checker( letter, position):
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
                score =minimax(board, True)
                board[key] = ' '

                if score < bestScore:
                    bestScore = score
        return bestScore   
def jouer( index, symbol="O"):
        (liste_bouttons[index])['text']=symbol
        (liste_bouttons[index])['state']="disabled"
        board[index]=symbol
        LAST_PLAY=index
        BOT_TURN=False
        USER_TURN=True
        playerMove()

b1=ttk.Button(frame, text=' ', command=jouer(1))
b2=ttk.Button(frame, text=' ', command=jouer(2))
b3=ttk.Button(frame, text=' ', command=jouer(3))
b4=ttk.Button(frame, text=' ', command=jouer(4))
b5=ttk.Button(frame, text=' ', command=jouer(5))
b6=ttk.Button(frame, text=' ', command=jouer(6))
b7=ttk.Button(frame, text=' ', command=jouer(7))
b8=ttk.Button(frame, text=' ', command=jouer(8))
b9=ttk.Button(frame, text=' ', command=jouer(9))

liste_bouttons=[b1,b1,b2,b3,b4,b5,b6,b7,b8,b9]
b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
b4.grid(row=2,column=1)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)
b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=3,column=3)

def playerMove():
    print("MY TURN")
    BOT_TURN=True
    USER_TURN=False
    position=LAST_PLAY
    checker(position,  'O')
    comMove()
            
def jouer( index, symbol="O"):
        (liste_bouttons[index])['text']=symbol
        (liste_bouttons[index])['state']="disabled"
        board[index]=symbol
        LAST_PLAY=index
        BOT_TURN=False
        USER_TURN=True
        playerMove()

def comMove():
    BOT_TURN=False
    USER_TURN=True
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
    jouer( bestMove,'X')


    

    



    


#PROG PRINCIPAL:
#================






#PROGRAMME PRINCIPALE:
if __name__ == '__main__':
    root.mainloop()

