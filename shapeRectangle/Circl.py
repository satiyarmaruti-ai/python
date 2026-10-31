import tkinter as tk
from tkinter import messagebox



def Masahat():
    radiousEntry1=int(radiousEntry.get().strip())
    pi=3.14
    m=radiousEntry1*pi
    #messagebox.showinfo(title='تست خروجی', message=f"{radiousEntry1}شعاع دایره برابر است با  ")
    messagebox.showinfo(title='تست خروجی', message=f"مساحت دایره برابر است با:   {m}")

def Mohet():
    radiousEntry1=int(radiousEntry.get().strip())
    pi=3.14
    p=2*radiousEntry1*pi
    #messagebox.showinfo(title='تست خروجی', message=f"{radiousEntry1}شعاع دایره برابر است با  ")
    messagebox.showinfo(title='تست خروجی', message=f"محیط دایره برابر است با:   {p}")

windowCircl=tk.Tk()
windowCircl.title('برنامه مساحت و محیط دایره')
radiousEntry=tk.Entry(windowCircl)
radiousEntry.grid(row=0, column=0, padx=5, pady=5)
tk.Label(windowCircl, text='شعاع دایره').grid(row=0, column=1, padx=10, pady=10)

btnMasahat=tk.Button(windowCircl, text='مساحت', command=Masahat)
btnMasahat.grid(row=2, column=0, pady=10, padx=10)

btnMohet=tk.Button(windowCircl, text='محیط', command=Mohet)
btnMohet.grid(row=2, column=1, pady=10, padx=10)

windowCircl.mainloop()