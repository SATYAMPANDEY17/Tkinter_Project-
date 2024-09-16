from tkinter import *
import random
li=['ROCK','PAPER','SCISSOR']
def ROCK():
    n=random.randint(0,2)
    lbl4.config(text="ROCK")
    lbl3.config(text=li[n])
    if li[n]=='ROCK':
        res.config(text='Match Draw!!!!')    
    else:
        if li[n]=='PAPER':
            res.config(text='YOU LOSE!!!!')
        else:
            res.config(text='YOU WIN!!!!')
def PAPER():
    n=random.randint(0,2)
    lbl4.config(text="PAPER")
    lbl3.config(text=li[n])
    if li[n]=='PAPER':
        res.config(text='Match Draw')    
    else:
        if li[n]=='SCISSOR':
            res.config(text='YOU LOSE!!!!')
        else:
            res.config(text='YOU WIN!!!!')
def SCISSOR():
    n=random.randint(0,2)
    lbl4.config(text="SCISSOR")
    lbl3.config(text=li[n])
    if li[n]=='SCISSOR':
        res.config(text='Match Draw')    
    else:
        if li[n]=='ROCK':
            res.config(text='YOU LOSE!!!!')
        else:
            res.config(text='YOU WIN!!!!')
root=Tk()
root.title("Rock Paper Scissor Game")
root.geometry("500x250+470+130")
root.resizable(False,False)
lbl=Label(root,text="ROCK PAPER SCISSOR GAME",fg="blue",font=("Arial 20 bold"))
lbl.place(x=50,y=10)
lbl1=Label(root,text="Computer",fg="black",font=("Arial 15 bold"))
lbl1.place(x=50,y=50)
lbl2=Label(root,text="Player",fg="black",font=("Arial 15 bold"))
lbl2.place(x=350,y=50)
lbl3=Label(root,text="",fg="black",font=("Arial 15 bold"))
lbl3.place(x=50,y=90)
lbl4=Label(root,text="",fg="black",font=("Arial 15 bold"))
lbl4.place(x=350,y=90)
res=Label(root,text="RESULT",fg="RED",font=("Arial 20 bold"))
res.place(x=170,y=130)
btnrock=Button(root,text="ROCK",font=("Arial 15"),fg="blue",bg="orange",command=ROCK)
btnrock.place(x=50,y=170)
btnpaper=Button(root,text="PAPER",font=("Arial 15"),fg="blue",bg="orange",command=PAPER)
btnpaper.place(x=190,y=170)
btnscissor=Button(root,text="SCISSOR",font=("Arial 15"),fg="blue",bg="orange",command=SCISSOR)
btnscissor.place(x=320,y=170)
root.mainloop()
