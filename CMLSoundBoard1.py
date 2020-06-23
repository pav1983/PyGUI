from tkinter import *
from playsound import playsound


root = Tk()
root.geometry('500x500')
root.title("Crazy Meijer Lady")

btn1 = Button(root, text='FU!', command=lambda: playsound('FU.mp3'))
btn1.pack()

btn2 = Button(root, text="Betterrepent", command=lambda: playsound('Betterrepent.mp3'))
btn2.pack()

btn3 = Button(root, text="FUINBMT", command=lambda: playsound('FUINBMT.mp3'))
btn3.pack()

btn4 = Button(root, text="FUITTHUMF", command=lambda: playsound('FUITTHUMF.mp3'))
btn4.pack()

btn5 = Button(root, text="FUSIR", command=lambda: playsound('FUSIR.mp3'))
btn5.pack()

btn6 = Button(root, text="GTFAFMYPOS", command=lambda: playsound('GTFAFMYPOS.mp3'))
btn6.pack()

btn7 = Button(root, text="GTFOOHITU", command=lambda: playsound('GTFOOHITU.mp3'))
btn7.pack()

btn8 = Button(root, text="LWOP", command=lambda: playsound('LWOP.mp3'))
btn8.pack()

btn9 = Button(root, text="MothaFucka1", command=lambda: playsound('MothaFucka1.mp3'))
btn9.pack()

btn10 = Button(root, text="MothaFuckaaa", command=lambda: playsound('MothaFuckaaa.mp3'))
btn10.pack()

btn11 = Button(root, text="STFUB", command=lambda: playsound('STFUB.mp3'))
btn11.pack()

btn12 = Button(root, text="USOB", command=lambda: playsound('USOB.mp3'))
btn12.pack()

# Set the position of button on the top of window

root.mainloop()
