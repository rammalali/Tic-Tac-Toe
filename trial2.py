from tkinter import *
from tkinter import ttk

liste_bouttons=[]
board={}
LAST_PLAY=int

class FenetreAccueil():
    def __init__(self, master):
        #Creation de la fenetre d'Accueil
        self.master=master
        self.screen_width =self.master.winfo_screenwidth()
        self.screen_height =self.master.winfo_screenheight()
        self.master.minsize(self.screen_width,self.screen_height)
        self.master.title("Tic Tac Toe")
        self.master['background']="dark slate gray"
        self.frame = Frame(self.master)
        self.frame.grid(row=0, column=0)
        self.labelIntro = ttk.Label(self.frame, text='TIC TAC TOE').grid(row=0,column=1,columnspan=3,sticky=(N))
        self.b1=ttk.Button(self.frame, text=' ', command=self.jouer(1))
        self.b2=ttk.Button(self.frame, text=' ', command=self.jouer(2))
        self.b3=ttk.Button(self.frame, text=' ', command=self.jouer(3))
        self.b4=ttk.Button(self.frame, text=' ', command=self.jouer(4))
        self.b5=ttk.Button(self.frame, text=' ', command=self.jouer(5))
        self.b6=ttk.Button(self.frame, text=' ', command=self.jouer(6))
        self.b7=ttk.Button(self.frame, text=' ', command=self.jouer(7))
        self.b8=ttk.Button(self.frame, text=' ', command=self.jouer(8))
        self.b9=ttk.Button(self.frame, text=' ', command=self.jouer(9))
        global liste_bouttons
        liste_bouttons=[self.b1,self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        self.b1.grid(row=1,column=1)
        self.b2.grid(row=1,column=2)
        self.b3.grid(row=1,column=3)
        self.b4.grid(row=2,column=1)
        self.b5.grid(row=2,column=2)
        self.b6.grid(row=2,column=3)
        self.b7.grid(row=3,column=1)
        self.b8.grid(row=3,column=2)
        self.b9.grid(row=3,column=3)
        
        def create_board(self):
            global board
            for i in range(1, 10):
                board[i] =' '
        create_board(self)
        print(liste_bouttons)
    def jouer(self, index, symbol="O"):
        global liste_bouttons
        global board
        global LAST_PLAY
        (liste_bouttons[index])['text']=symbol
        (liste_bouttons[index])['state']="disabled"
        board[index]=symbol
        LAST_PLAY=index
        BOT_TURN=False
        USER_TURN=True
        #print (board)
        self.playerMove()

    def spaceIsFree(self,position):
        global board
        if board[position] == ' ':
            return True
        else:
            return False

    def checker(self, letter, position):
        if self.checkWin():
             if letter == 'X':
                print("Bot Win !")
                exit()
             else:
                print("Player Wins!")
                exit()
        if self.checkDraw():
            print("Draw!")
            exit()
        return

    def checkDraw(self):
        for key in board.keys():
            if board[key] == ' ':
                return False
        return True


    def checkWin(self):
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

    
    def checkWhoWon(self,letter):
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

    def playerMove(self):
        global LAST_PLAY
        print("MY TURN")
        self.BOT_TURN=True
        self.USER_TURN=False
        position=LAST_PLAY
        self.checker()
        self.comMove()
              


    def comMove(self):
        self.BOT_TURN=False
        self.USER_TURN=True
        bestScore = -1
        bestMove = 0  # will be changed

        for key in board.keys():
            if board[key] == ' ':
                board[key] = 'X'
                score = self.minimax(board, False)
                board[key] = ' '

                if score > bestScore:
                    bestScore = score
                    bestMove = key
        self.jouer( bestMove,'X')


    def minimax(self,board, isMaximizing):
        if self.checkWhoWon('X'):
            return 1
        elif self.checkWhoWon('O'):
            return -1
        elif self.checkDraw():
            return 0

        if isMaximizing:
            bestScore = -1

            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'X'
                    score = self.minimax(board, False)
                    board[key] = ' '

                    if score > bestScore:
                        bestScore = score
            return bestScore
        else:

            bestScore = 1

            for key in board.keys():
                if board[key] == ' ':
                    board[key] = 'O'
                    score =self.minimax(board, True)
                    board[key] = ' '

                    if score < bestScore:
                        bestScore = score
            return bestScore   

        
    
        



        


#PROG PRINCIPAL:
#================

    




#PROGRAMME PRINCIPALE:
if __name__ == '__main__':
    root = Tk()
    FenetreAccueil(root)
    root.mainloop()

