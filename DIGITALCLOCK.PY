from tkinter import *
from time import strftime
root=Tk()
def hide():
    frame=LabelFrame(root,height=100,width=600,bg='blue')
    frame.place(x=0,y=50)
def show():
    frame1=LabelFrame(root,height=100,width=600,bg='blue')
    frame1.place(x=0,y=50)
    lbl=Label(frame1,text="",font=("Arial 20 italic"), fg="white",bg="black")
    lbl.place(x=100,y=30)
    def time():
        global string
        h=strftime("%H")
        m=strftime("%M")
        s=strftime("%S")
        p=strftime("%p")
        string=(h+":"+m+":"+s+" "+p)
        lbl.config(text=string)
        lbl.after(1000,time)
    #string.after(1000,time)
    time()
root.title('clock')
root.geometry("350x150")
frame=LabelFrame(root,height=100,width=600,bg='blue')
frame.place(x=0,y=50)


btn=Button(root,text='Show Time',width=20,bg='green',command=show)
btn.place(x=10,y=10)
btn2=Button(root,text='Hide Time',width=20,bg='red',command=hide)
btn2.place(x=170,y=10)
root.mainloop()