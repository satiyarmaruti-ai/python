import tkinter as tk
from tkinter import  messagebox
import turtle

def scoar():
    
    t1=turtle.Turtle()
    t1.pencolor('red')
    t1.forward(100)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(100)
    t1.left(90)
    t1.forward(100)

def peng():
     
     t1=turtle.Turtle()
     t1.pencolor('blue')
     t1.forward(100)
     t1.left(72)
     t1.forward(100)
     t1.left(72)
     t1.forward(100)
     t1.left(72)
     t1.forward(100)
     t1.left(72)
     t1.forward(100)
def shish():
         
     t1=turtle.Turtle()
     t1.pencolor('yellow')
     t1.forward(100)
     t1.left(60)
     t1.forward(100)
     t1.left(60)
     t1.forward(100)
     t1.left(60)
     t1.forward(100)
     t1.left(60)
     t1.forward(100)
     t1.left(60)
     t1.forward(100)
def mesles():
      
      t1=turtle.Turtle()
      t1.pencolor('red')
      t1.forward(100)
      t1.left(120)
      t1.forward(100)
      t1.left(120)
      t1.forward(100)  
      t1.left(120)
   
window=tk.Tk()
btn1=tk.Button(window, text='مربع', command=scoar)
btn1.grid(row=1, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=2, column=0, padx=10, pady=10)

btn2=tk.Button(window, text='پنج ضلعی', command=peng)
btn2.grid(row=3, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=4, column=0, padx=10, pady=10)

btn3=tk.Button(window, text='شیش ضلعی', command=shish)
btn3.grid(row=5, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=6, column=0, padx=10, pady=10)

btn4=tk.Button(window, text='مثلث', command=mesles)
btn4.grid(row=7, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=8, column=0, padx=10, pady=10)


window.mainloop()