from tkinter import *
 
def addNumbers():
    res=int(e1.get())+int(e2.get())+int(e3.get())
    myText.set(res)
    
def avgNumbers():
    res=(int(e1.get())+int(e2.get())+int(e3.get()))/3
    myText.set(res)
 
master = Tk()
myText=StringVar();
Label(master, text="First Game").grid(row=0, sticky=W)
Label(master, text="Second Game").grid(row=1, sticky=W)
Label(master, text="Third Game").grid(row=2, sticky=W)
Label(master, text="Result: ").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)

 
e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
 
b = Button(master, text="Total", command=addNumbers)
b.grid(row=3, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

b2 = Button(master, text="Average", command=avgNumbers)
b2.grid(row=5, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
mainloop()
