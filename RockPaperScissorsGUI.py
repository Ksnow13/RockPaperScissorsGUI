
import random

import tkinter.messagebox


def RPS(UserRPS):

    Message = ""

    RandomRPSNum = random.randrange(1, 4)

    RandomRPS = ""

    if RandomRPSNum == 1:

        RandomRPS = "ROCK"

    if RandomRPSNum == 2:

        RandomRPS = "PAPER"

    if RandomRPSNum == 3:

        RandomRPS = "SCISSORS"

    print("The CPU Choose " + RandomRPS + "!")

    if UserRPS.upper() == "R" and RandomRPSNum == 1:

        Message = "DRAW"

    elif UserRPS.upper() == "R" and RandomRPSNum == 2:

        Message = "You Lose"

    elif UserRPS.upper() == "R" and RandomRPSNum == 3:

        Message = "You Win"

    elif UserRPS.upper() == "P" and RandomRPSNum == 1:

        Message = "You Win"

    elif UserRPS.upper() == "P" and RandomRPSNum == 2:

        Message = "DRAW"

    elif UserRPS.upper() == "P" and RandomRPSNum == 3:

        Message = "You Lose"

    elif UserRPS.upper() == "S" and RandomRPSNum == 1:

        Message = "You Lose"

    elif UserRPS.upper() == "S" and RandomRPSNum == 2:

        Message = "You Win"


    elif UserRPS.upper() == "S" and RandomRPSNum == 3:

        Message = "DRAW"

    else:

        Message = "Invalid Input"

    return Message



from tkinter import *


Root = Tk()


TheTitleLabel = Label(Root, text="RPS GAME", font=("Helvetica", 40))
TheTitleLabel.pack(pady=10)

SubTitle = Label(Root, text="Type (R, P, S) to Play", font=("Helvetica", 15))
SubTitle.pack(pady=20)

def submit():

    Answer = RPS(Entry_Box.get())

    if Answer == "DRAW":

        Output_Label.config(text="DRAW")

    if Answer == "You Lose":

        Output_Label.config(text="You Lose")

    if Answer == "You Win":

        Output_Label.config(text="You Win")

    if Answer == "Invalid Input":

        Output_Label.config(text="Invalid Input")




Entry_Box = Entry(Root)
Entry_Box.pack(pady=30)

Entry_Button = Button(Root, text="Submit Choice", command=submit)
Entry_Button.pack(pady=10)

Output_Label = Label(Root, text="", font=("Helvetica", 15))
Output_Label.pack()


FacePhoto = PhotoImage(file="Face.png")
PhotoLabel = Label(Root, image=FacePhoto)

PhotoLabel.pack()


Statusbar = Label(Root, text="Doing Nothing...", bd=1, relief=SUNKEN, anchor=W)
Statusbar.pack(side=BOTTOM, fill=X)


tkinter.messagebox.showinfo("Rock Paper Scissors Game.", " My first attempt implementing a GUI to a program")

MessageAnswer = tkinter.messagebox.askquestion("WAIT", "Press yes to receive good luck!")

if MessageAnswer == "yes":

    print()
    print(" Good Luck :) ")
    print()

if MessageAnswer == "no":

    print()
    print(" No Luck For You Then :( ")


Root.mainloop()
