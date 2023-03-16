from random import *
from tkinter import *
from sys import *
from threading import *
from time import *

class Case:
    round = 1
    def __init__(self,id,button):
        self.id = id
        self.gaveTheWin = False
        self.button = button
        self.color = "White"
        self.button.configure(command=lambda: self.clickButton())

    def reconfigureButton(self):
        self.button.configure(command=lambda: self.clickButton())

    def clickButton(self):
        if self.color == "White":
            if Case.round == 1:
                self.color = "#DC0D0D"
            else:
                self.color = "#FFF000"
            self.button.configure(bg=self.color)
            Case.round *= -1
            board.stackCase()

class Board:
    def __init__(self,window,height,width):
        self.lstCase = []
        self.window = window
        self.height = height
        self.width = width
        
    def initScore(self):
        self.scorePlayer1 = 0
        self.scorePlayer2 = 0
        self.textPlayer1 = Label(self.window,text="Joueur 1 : " + str(self.scorePlayer1), bg="#DC0D0D", font=("Arial", 25))
        self.textPlayer2 = Label(self.window,text="Joueur 2 : " + str(self.scorePlayer2), bg="#FFF000", font=("Arial", 25))
        self.textPlayer1.grid(row=1, column=self.width +1, padx=0, pady=0)
        self.textPlayer2.grid(row=2, column=self.width +1, padx=0, pady=0)

    def stackCase(self):
        for i in range(self.height):
            for j in range(self.width):
                if i < height-1:
                    if self.lstCase[i+1][j].color == "White":
                        self.lstCase[i+1][j].button.configure(bg = self.lstCase[i][j].color)
                        self.lstCase[i+1][j].color = self.lstCase[i][j].color
                        self.lstCase[i][j].button.configure(bg = "White")
                        self.lstCase[i][j].color = "White"
                        window.update()

        self.isWin()

    def updateScoreEndGame(self,color):
            if color == "#DC0D0D":
                self.scorePlayer1 += 1
                self.textPlayer1.configure(text="Joueur 1 : " + str(self.scorePlayer1))
            else:
                self.scorePlayer2 += 1
                self.textPlayer2.configure(text="Joueur 2 : " + str(self.scorePlayer2))

            for i in range(self.height):
                for j in range(self.width):
                    self.lstCase[i][j].button.configure(command=lambda: self.doNothing())
                    if self.lstCase[i][j].gaveTheWin == False:
                        if self.lstCase[i][j].color == "#DC0D0D":
                            self.lstCase[i][j].color = "#F89A9A"
                            self.lstCase[i][j].button.configure(bg="#F89A9A")
                        
                        elif self.lstCase[i][j].color == "#FFF000":
                            self.lstCase[i][j].color = "#FFFAA8"
                            self.lstCase[i][j].button.configure(bg="#FFFAA8")
                        
    def doNothing(self):
        pass
                    
    def isWin(self):
        for i in range(self.height):
            for j in range(self.width-3):
                if self.lstCase[i][j].color != "White":
                    if self.lstCase[i][j].color == self.lstCase[i][j+1].color:
                        if self.lstCase[i][j+1].color == self.lstCase[i][j+2].color:
                            if self.lstCase[i][j+2].color == self.lstCase[i][j+3].color:
                                self.lstCase[i][j].gaveTheWin = True
                                self.lstCase[i][j+1].gaveTheWin = True
                                self.lstCase[i][j+2].gaveTheWin = True
                                self.lstCase[i][j+3].gaveTheWin = True
                                self.updateScoreEndGame(self.lstCase[i][j].color)
        for i in range(self.height-3):
            for j in range(self.width):
                if self.lstCase[i][j].color != "White":
                    if self.lstCase[i][j].color == self.lstCase[i+1][j].color:
                        if self.lstCase[i+1][j].color == self.lstCase[i+2][j].color:
                            if self.lstCase[i+2][j].color == self.lstCase[i+3][j].color:
                                self.lstCase[i][j].gaveTheWin = True
                                self.lstCase[i+1][j].gaveTheWin = True
                                self.lstCase[i+2][j].gaveTheWin = True
                                self.lstCase[i+3][j].gaveTheWin = True
                                self.updateScoreEndGame(self.lstCase[i][j].color)
        for i in range(self.height-3):
            for j in range(self.width-3):
                if self.lstCase[i][j].color != "White":
                    if self.lstCase[i][j].color == self.lstCase[i+1][j+1].color:
                        if self.lstCase[i+1][j+1].color == self.lstCase[i+2][j+2].color:
                            if self.lstCase[i+2][j+2].color == self.lstCase[i+3][j+3].color:
                                self.lstCase[i][j].gaveTheWin = True
                                self.lstCase[i+1][j+1].gaveTheWin = True
                                self.lstCase[i+2][j+2].gaveTheWin = True
                                self.lstCase[i+3][j+3].gaveTheWin = True
                                self.updateScoreEndGame(self.lstCase[i][j].color)
        for i in range(3,self.height):
            for j in range(self.width-3):
                if self.lstCase[i][j].color != "White":
                    if self.lstCase[i][j].color == self.lstCase[i-1][j+1].color:
                        if self.lstCase[i-1][j+1].color == self.lstCase[i-2][j+2].color:
                            if self.lstCase[i-2][j+2].color == self.lstCase[i-3][j+3].color:
                                self.lstCase[i][j].gaveTheWin = True
                                self.lstCase[i-1][j+1].gaveTheWin = True
                                self.lstCase[i-2][j+2].gaveTheWin = True
                                self.lstCase[i-3][j+3].gaveTheWin = True
                                self.updateScoreEndGame(self.lstCase[i][j].color)

    def initLst(self):
        for i in range(self.height):
            self.lstCase.append([])

    def initButtonTkinter(self):

        for i in range(self.height):
            for j in range(self.width):
                self.lstCase[i].append(Case(int(str(i)+str(j)),Button(height=7, width=14, font=("Helvetica", 12),bg="white", bd=1)))
                self.lstCase[i][j].button.grid(row=i, column=j, padx=0, pady=0)

        self.buttonNewGame = Button(text="Nouvelle Partie",font=("Arial", 25), command=lambda: self.newGame(),bd=0, bg="#5BC131",fg="#373737",activebackground="#C1FFA8",activeforeground="#373737")
        self.buttonNewGame.grid(row=0, column=width +1, padx=0, pady=0)
        self.buttonResetScore = Button(text="Score à 0",font=("Arial", 25), command=lambda: self.initScore(),bd=0, bg="#5BC131",fg="#373737",activebackground="#C1FFA8",activeforeground="#373737")
        self.buttonResetScore.grid(row=3, column=width +1, padx=0, pady=0)

    def initWindow(self):
        self.window.title('Puissance4')

    def newGame(self):
        for i in range(self.height):
            for j in range(self.width):
                self.lstCase[i][j].reconfigureButton()
                self.lstCase[i][j].gaveTheWin = False
                self.lstCase[i][j].button.configure(bg="White")
                self.lstCase[i][j].color = "White"
           
height = 6 #int(input("nb de lignes"))
width = 7 #int(input("nb de colones"))
window=Tk()
board = Board(window,height,width)

board.initLst()
board.initButtonTkinter()
board.initScore()
board.initWindow()
board.window.mainloop()

