import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
class mostatil:
    def __init__(self):
        # self.L=float(num2Entry.get().strip())
        # self.W=float(num1Entry.get().strip())
        # width=float(num1Entry.get().stirp())
        # length=float(num2Entry.get().stirp())
        pass
    def masahat(self):
        self.L=float(num2Entry.get().strip())
        self.W=float(num1Entry.get().strip())
        sum1=(self.L*self.W)
        messagebox.showinfo(title='', message=f"{sum1}")
    def mohet(self):
        sum2=(self.L+self.W)*2
        messagebox.showinfo(title='', message=f"{sum2}")
        
# ww=float(input('insert width'))
# ll=float(input('insert length'))
# satiar=mostatil(ww,ll)
# print(f'square is:  {satiar.mohet()}')
window=tkinter.Tk()
window.title('طراحی شکل')
oopEntry=tk.Entry(window)
num2Entry=tk.Entry(window)
num2Entry.grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text='طول ').grid(row=0, column=1, padx=10, pady=10)

num1Entry=tk.Entry(window)
num1Entry.grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text='عرض').grid(row=1, column=1, padx=10, pady=10)
mostatil2=mostatil()
btn1=tk.Button(window, text='مساحت', command=mostatil2.masahat)
btn1.grid(row=2, column=0, pady=3, padx=3)

btn1=tk.Button(window, text='محیط', command=mostatil2.mohet)
btn1.grid(row=2, column=1, pady=3, padx=3)
window.mainloop()