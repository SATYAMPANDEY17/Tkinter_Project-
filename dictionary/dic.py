from difflib import get_close_matches
from tkinter import *
from PyDictionary import PyDictionary
from PIL import ImageTk,Image
from tkinter import messagebox
dictionary = PyDictionary()
root = Tk()
def word():
    x=dictionary.meaning(search.get())['Noun']
    for i in x:
        textarea.insert(END,"*"+i+'\n\n')




root.geometry("800x600+400+50")
i=Image.open('image/2.jpg')
i=i.resize((800,600),Image.LANCZOS)
bg=ImageTk.PhotoImage(i)
lbg=Label(root,image=bg)
lbg.place(x=-2,y=00)
root.resizable(0,0)
lbs=Label(root,text="Enter Word",font=("Helvetica 20 bold"),bd=8,relief=GROOVE,fg='whitesmoke',bg='red3')
lbs.place(x=100,y=40)
lbm=Label(root,text="Meaning",font=("Helvetica 20 bold"),bd=8,relief=GROOVE,fg='whitesmoke',bg='red3')
lbm.place(x=100,y=230)
search=Entry(root,font=("Helvetica 20 bold"),justify='center',bd=8,relief=GROOVE,bg='whitesmoke')
search.place(x=100,y=100 )
searchi=PhotoImage(file='image/search.png')
btns=Button(root,image=searchi,bg='violet',bd=8,cursor='hand2',command=word)
btns.place(x=420,y=100)
textarea=Text(root,height=7,width=41,font=("Helvetica 15 bold"),bd=8,relief=GROOVE,pady=2,padx=2)
textarea.place(x=100,y=290)
root.mainloop()
