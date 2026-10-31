#برنامه پر کردن فرم 

import tkinter as tk
from tkinter import messagebox
def name():
    lengthEntry1=int(lengthEntry.get().strip())
    widthEntry1=int(widthEntry.get().strip())
    
def call():
    lengthEntry1=int(lengthEntry.get().strip())
    widthEntry1=int(widthEntry.get().strip())
    

window=tk.Tk()
window.title('فرم ثبت نام')
lengthEntry=tk.Entry(window)
lengthEntry.grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text='نام و نام خانوادگی').grid(row=0, column=1, padx=10, pady=10)

widthEntry=tk.Entry(window)
widthEntry.grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, text='شماره تلفن').grid(row=1, column=1, padx=10, pady=10)

btnMasahat=tk.Button(window, text="تکمیل کردن فرم", command=name)
btnMasahat.grid(row=2, column=0, pady=10, padx=10)

window.mainloop()
