from colorsys import rgb_to_hsv
import tkinter as tk
from tkinter import  messagebox
import turtle
import random
t1=turtle.Turtle()


def makshap():
   
    num1=int(numEntry1.get())
    andaze=int(numEntry2.get())
    numShape=int(numEntry3.get().strip())
    zavieh=360/num1
    t1.color(rgb_to_hsv(0.128, 0.250, 0.0))
    for j in range(numShape):
        # t1.left(360/numShape)
        for i in range(num1):
            pSize=random.randint(6,15)
            a1=random.random()
            a2=random.random()
            a3=random.random()
            t1.color(rgb_to_hsv(a1, a2, a3))
            t1.pensize(pSize)
            t1.forward(andaze)
            t1.left(zavieh)
        
                
     
     
window=tk.Tk()
numEntry1=tk.Entry(window)
numEntry1.grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text='تعداد ضلع').grid(row=0, column=1, padx=10, pady=10)

numEntry2=tk.Entry(window)
numEntry2.grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text='اندازه ضلع').grid(row=1, column=1, padx=10, pady=10)

numEntry3=tk.Entry(window)
numEntry3.grid(row=2, column=0, padx=5, pady=5)
tk.Label(window, text='تعداد شکل ').grid(row=2, column=1, padx=10, pady=10)

btn1=tk.Button(window, text='رسم شکل', command=makshap)
btn1.grid(row=3, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=3, column=0, padx=10, pady=10)



window.mainloop()