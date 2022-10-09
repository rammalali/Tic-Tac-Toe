from tkinter import *
from tkinter import ttk
fenetre = Tk()
fenetre.title("Tic Tac Toe")
fenetre.minsize(500,300)
frame = Frame(fenetre)
frame.grid(row=0, column=0)
labelIntro = ttk.Label(frame, text='TIC TAC TOE').grid(row=0,column=1,columnspan=3,sticky=(N))

LAST_PLAY=0
BOT_TURN = True
USER_TURN= False
  
    

class Boutton:
    def __init__(self,position):
       self.boutton= ttk.Button(frame, text=' ', command=self.jouer)
       self.position=position


    def jouer(self,symbol='O'):
        self.boutton['text']=symbol
        self.boutton['state']="disabled"
        LAST_PLAY=self.position
        global BOT_TURN
        global USER_TURN
        BOT_TURN=False
        USER_TURN=True
        
        #print(LAST_PLAY)


    def afficher(self,r,c):
        self.boutton.grid(row=r,column=c)
    

        
class Board:
    def __init__(self):
        self.b1=Boutton(1)
        self.b2=Boutton(2)
        self.b3=Boutton(3)
        self.b4=Boutton(4)
        self.b5=Boutton(5)
        self.b6=Boutton(6)
        self.b7=Boutton(7)
        self.b8=Boutton(8)
        self.b9=Boutton(9)
        self.b1.afficher(1,1)
        self.b2.afficher(1,2)
        self.b3.afficher(1,3)
        self.b4.afficher(2,1)
        self.b5.afficher(2,2)
        self.b6.afficher(2,3)
        self.b7.afficher(3,1)
        self.b8.afficher(3,2)
        self.b9.afficher(3,3)
        self.board={}
        def create_board(self):
            for i in range(1, 10):
                self.board[i] =' '
        create_board(self)
        self.liste_bouttons=[self.b1,self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9]
        

        
    def spaceIsFree(self,position):
        if self.board[position] == ' ':
            return True
        else:
            return False

    def insertLetter(self,letter, position):
        if self.spaceIsFree(position):
            self.board[position] = letter
        self.update_board()
        
            

    def update_boutton(self, boutton):
        if (self.board[boutton.position] != " "):
            boutton.jouer(self.board[boutton.position])

    def update_board(self):
        for boutton in self.liste_bouttons:
            self.update_boutton(boutton)
        print("Updated board: ", self.board)


class Game:
    def __init__(self):
        self.GAME_BOARD=Board()
        #self.GAME_BOARD.board=self.GAME_BOARD.get_board()
        
        
        

    def checkDraw(self):
        for key in self.GAME_BOARD.board.keys():
            if self.GAME_BOARD.board[key] == ' ':
                return False
        return True


    def checkWin(self):
        print("Checking if someone won: ", self.GAME_BOARD.board)
        if self.GAME_BOARD.board[1] == self.GAME_BOARD.board[2] and self.GAME_BOARD.board[1] == self.GAME_BOARD.board[3] and self.GAME_BOARD.board[1] != ' ':
            return True
        elif self.GAME_BOARD.board[4] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[4] == self.GAME_BOARD.board[6] and self.GAME_BOARD.board[4] != ' ':
            return True
        elif self.GAME_BOARD.board[7] == self.GAME_BOARD.board[8] and self.GAME_BOARD.board[7] == self.GAME_BOARD.board[9] and self.GAME_BOARD.board[7] != ' ':
            return True
        elif self.GAME_BOARD.board[1] == self.GAME_BOARD.board[4] and self.GAME_BOARD.board[1] == self.GAME_BOARD.board[7] and self.GAME_BOARD.board[1] != ' ':
            return True
        elif self.GAME_BOARD.board[2] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[2] == self.GAME_BOARD.board[8] and self.GAME_BOARD.board[2] != ' ':
            return True
        elif self.GAME_BOARD.board[3] == self.GAME_BOARD.board[6] and self.GAME_BOARD.board[3] == self.GAME_BOARD.board[9] and self.GAME_BOARD.board[3] != ' ':
            return True
        elif self.GAME_BOARD.board[1] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[1] == self.GAME_BOARD.board[9] and self.GAME_BOARD.board[1] != ' ':
            return True
        elif self.GAME_BOARD.board[3] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[3] == self.GAME_BOARD.board[7] and self.GAME_BOARD.board[3] != ' ':
            return True

        else:
            return False

    
    def checkWhoWon(self,letter):
        if self.GAME_BOARD.board[1] == self.GAME_BOARD.board[2] and self.GAME_BOARD.board[1] == self.GAME_BOARD.board[3] and self.GAME_BOARD.board[1] == letter:
            return True
        elif self.GAME_BOARD.board[4] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[4] == self.GAME_BOARD.board[6] and self.GAME_BOARD.board[4] == letter:
            return True
        elif self.GAME_BOARD.board[7] == self.GAME_BOARD.board[8] and self.GAME_BOARD.board[7] == self.GAME_BOARD.board[9] and self.GAME_BOARD.board[7] == letter:
            return True
        elif self.GAME_BOARD.board[1] == self.GAME_BOARD.board[4] and self.GAME_BOARD.board[1] == self.GAME_BOARD.board[7] and self.GAME_BOARD.board[1] == letter:
            return True
        elif self.GAME_BOARD.board[2] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[2] == self.GAME_BOARD.board[8] and self.GAME_BOARD.board[2] == letter:
            return True
        elif self.GAME_BOARD.board[3] == self.GAME_BOARD.board[6] and self.GAME_BOARD.board[3] == self.GAME_BOARD.board[9] and self.GAME_BOARD.board[3] == letter:
            return True
        elif self.GAME_BOARD.board[1] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[1] == self.GAME_BOARD.board[9] and self.GAME_BOARD.board[1] == letter:
            return True
        elif self.GAME_BOARD.board[3] == self.GAME_BOARD.board[5] and self.GAME_BOARD.board[3] == self.GAME_BOARD.board[7] and self.GAME_BOARD.board[3] == letter:
            return True
        else:
            return False

    def playerMove(self):
        print("MY TURN")
        global BOT_TURN
        global USER_TURN
        global LAST_PLAY
        BOT_TURN=True
        USER_TURN=False
        position=LAST_PLAY
        self.GAME_BOARD.insertLetter('O', position)
        #self.GAME_BOARD.board=self.GAME_BOARD.get_board()
        #self.GAME_BOARD.liste_bouttons[position].jouer("O")
        if self.checkWin():
                    print("Player Wins!")
                    exit()
        if self.checkDraw():
                print("Draw!")
                exit()
        return

    def comMove(self):
        print("AI TURN ")
        global BOT_TURN
        global LAST_PLAY
        bestScore = -1
        bestMove = 0  # will be changed
        BOT_TURN=False
        

        for key in self.GAME_BOARD.board.keys():
            if self.GAME_BOARD.board[key] == ' ':
                self.GAME_BOARD.board[key] = 'X'
                score = self.minimax(self.GAME_BOARD.board, False)
                self.GAME_BOARD.board[key] = ' '

                if score > bestScore:
                    bestScore = score
                    bestMove = key
        self.GAME_BOARD.insertLetter('X', bestMove)
        LAST_PLAY=bestMove
        self.GAME_BOARD.liste_bouttons[bestMove].jouer("X")
        #self.board=self.GAME_BOARD.get_board()
        if self.checkWin():
                    print("Bot Win !")
                    exit()
        if self.checkDraw():
                print("Draw!")
                exit()

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
                    score = self.minimax(board, True)
                    board[key] = ' '

                    if score < bestScore:
                        bestScore = score
            return bestScore
    





#PROG PRINCIPAL:
#================

    


a=Game()

# while(a.checkWin()==False):
#     if (USER_TURN):
#         a.playerMove()
#     if (BOT_TURN):
#         a.comMove()

   

a.comMove()
i=int(input("yalla"))
a.comMove()
i=int(input("yalla"))
a.comMove()
i=int(input("yalla"))
a.comMove()
i=int(input("yalla"))
a.comMove()
i=int(input("yalla"))
a.comMove()
fenetre.mainloop()


