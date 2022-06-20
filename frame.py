from textwrap import fill
from tkinter import *
from tkinter.font import BOLD
from turtle import left
root = Tk()
root.geometry('700x700')
#root.geometry("500x500")
root.title("Frame")
# first frame and label
f1=Frame(root,bg='grey',borderwidth=30,relief=SUNKEN)
f1.pack(side=LEFT,fill='y')
#label = first
first_label = Label(f1,text="Explorer")
first_label.pack(padx='30')
# second frame and label
f2=Frame(root,bg='grey',borderwidth=30,relief=SUNKEN)
f2.pack(side=LEFT,fill='y')
seond_label = Label(f2,text="Python Project List",foreground='red',font="bold 15")
seond_label.pack(padx=30)
# third frame and label
f3=Frame(root,bg='grey',borderwidth=30,relief=SUNKEN)
f3.pack(side=LEFT,fill='y')
third_label = Label(f3,text="Text Part")
third_label.pack(padx='30')
root.mainloop()
