from tkinter import *

from tkinter import scrolledtext
import textwrap

window = Tk()

window.title("Text Wrap Tool")

window.geometry('600x500')

txt = scrolledtext.ScrolledText(window,width=50,height=20)

def doit():
    data = txt.get(1.0, END).replace('\n', ' ')
    txt.delete(1.0, END)
    txt.insert(INSERT, data)

t = Text()
t.config(wrap=WORD)

txt.grid(column=0,row=0)

btn1 = Button(window,text='Clear', command=lambda: txt.delete(1.0,END))
btn2 = Button(window,text='Wrap', command=lambda: doit())

btn1.grid(column=4, row=15)
btn2.grid(column=8, row=15)

window.mainloop()
