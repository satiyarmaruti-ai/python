#در این پروژ مساحت و محیط اشکال دایر .مربع و مستطیل یکجا بررسی میشود 
import tkinter as tk
from tkinter import messagebox

def rectangle():
    import shapRectangle
def cercel() :
    import Circl
def squareCommand() :
    import square

window=tk.Tk()
window.title('برنامه مساحت و محیط اشکال ریاضی ')

tk.Label(window, text='پیداکردن مساحت و محیط اشکال ریاضی').grid(row=0, column=1, padx=5, pady=5)

btnRectangale=tk.Button(window, text='مستطیل', command=rectangle)
btnRectangale.grid(row=1, column=0, pady=5, padx=5)

btnCircl=tk.Button(window, text='دایره', command=cercel)
btnCircl.grid(row=1, column=1, pady=5, padx=5)


btnsquare=tk.Button(window, text='مربع', command=squareCommand)
btnsquare.grid(row=1, column=2, pady=5, padx=5)

window.mainloop()