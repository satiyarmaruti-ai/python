import tkinter as tk
from tkinter import messagebox

def mainFunction():
 from Sakhteman import beton

def mathshap():
  from shapeRectangle import mathshap

def codeMeli():
   from ifProject import p4CodeMeli


def login():
  uesrname=(loginEntry1.get().strip())
  password=(loginEntry2.get().strip())
  if(uesrname=="S" and password=="1"):
    messagebox.showinfo(title='ورود موفقیت آمیز', message='به سیستم خوشم آمدید')
    # mathshap()
    # mainFunction()
    # codeMeli()
    from ifProject import p4CodeMeli
    p4CodeMeli.showName()

  else:
    messagebox.showerror(title='خطا', message='نام کاربری یا کلمه ی عبور اشتباه می باشد')


 
windowlogin=tk.Tk()
loginEntry1=tk.Entry(windowlogin)
loginEntry1.grid(row=0, column=0, padx=10, pady=10)
tk.Label(windowlogin, text='نام کاربری').grid(row=0, column=1, padx=10, pady=10)

loginEntry2=tk.Entry(windowlogin, show='*')
loginEntry2.grid(row=1, column=0, padx=10, pady=10)
tk.Label(windowlogin, text='گذرواژه').grid(row=1, column=1, padx=10, pady=10)


btnlogin1=tk.Button(windowlogin, text='ورود', command=login)
btnlogin1.grid(row=2, column=0, pady=10, padx=10)

windowlogin.mainloop()