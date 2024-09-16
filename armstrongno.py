#armstrong number
from tkinter import *
def armstrong():
 n=int(n1.get())
 s=0
 a=n
 i=n
 c=0
 while a>0:
  c=c+1
  a=a//10
 while n>0:
  rem=n%10
  s=s+rem**c
  n=n//10
 if i==s:
  res.config(text="Number is Armstrong")
 else:
  res.config(text="Number is not a Armstrong")
d=Tk()
d.title("Armstrong Checker")
d.geometry("500x220+440+170")
d.resizable(False,False)
lbl=Label(d,text="Armstrong Checker",fg="red",font=("Arial 20 bold"))
lbl.place(x=140,y=10)
lbl1=Label(d,text="Enter Word:",fg="black",font=("Arial 12 bold"))
lbl1.place(x=20,y=50)
res=Label(d,text="",fg="white",bg="purple",font=("Arial 15 bold"))
res.place(x=150,y=90)
n1=Entry(d,font=("Arial 12 "))
n1.place(x=170,y=50)
btnp=Button(d,text="CHECK",font=("Arial 15"),fg="blue",bg="yellow",command=armstrong)
btnp.place(x=200,y=130)
d.mainloop()