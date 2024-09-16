#palindrome
from tkinter import *
def reverse():
 a=n1.get()
 b="".join(reversed(a))
 if a==b:
  res.config(text="Word is Palindrome")
 else:
  res.config(text="Word is Not a Palindrome")
d=Tk()
d.title("Palindrome Checker")
d.geometry("500x220+440+170")
d.resizable(False,False)
lbl=Label(d,text="Palindrome Checker",fg="red",font=("Arial 20 bold"))
lbl.place(x=140,y=10)
lbl1=Label(d,text="Enter Word:",fg="black",font=("Arial 12 bold"))
lbl1.place(x=20,y=50)
res=Label(d,text="",fg="white",bg="purple",font=("Arial 15 bold"))
res.place(x=150,y=90)
n1=Entry(d,font=("Arial 12 "))
n1.place(x=170,y=50)
btnp=Button(d,text="CHECK",font=("Arial 15"),fg="blue",bg="yellow",command=reverse)
btnp.place(x=200,y=130)
d.mainloop()