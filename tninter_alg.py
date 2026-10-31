import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import turtle
t1=turtle.Turtle()
def alg():
    x=int(xEntry.get().strip())
    tehdadechrkhesh=int(cherkheshEntry.get().strip())
    for x in range(tehdadechrkhesh):
        y=x^3+60
        t1.goto(x,y)
        t1.penup()
        t1.goto(0,0)
        t1.pendown()
        t1.left(10)
        
window=tkinter.Tk()
window.title('طراحی شکل')
algEntry=tk.Entry(window)
xEntry=tk.Entry(window)
xEntry.grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text='توان تابع ').grid(row=0, column=1, padx=10, pady=10)

cherkheshEntry=tk.Entry(window)
cherkheshEntry.grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text='تعداد چرخش').grid(row=1, column=1, padx=10, pady=10)

btn1=tk.Button(window, text='طراحی', command=alg)
btn1.grid(row=2, column=0, pady=3, padx=3)

window.mainloop()