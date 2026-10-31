import tkinter as tk
from tkinter import messagebox



def Masahat():
    Ege=int(EagEntry.get().strip())
    m=Ege*Ege
    # messagebox.showinfo(title='تست خروجی', message=f"طول مستطیل برابر است با {lengthEntry1}و عرض مستطیل برابر است با   {widthEntry1}")
    messagebox.showinfo(title='تست خروجی', message=f"مساحت مربع برابر است با:   {m}")

def Mohet():
    Ege=int(EagEntry.get().strip())
    n=(Ege+Ege)*2
    # messagebox.showinfo(title='تست خروجی', message=f"طول مستطیل برابر است با {lengthEntry1}و عرض مستطیل برابر است با   {widthEntry1}")
    messagebox.showinfo(title='تست خروجی', message=f"محیط مربع برابر است با:   {n}")


windowsquare=tk.Tk()
windowsquare.title('برنامه مساحت و محیط  مربع')
EagEntry=tk.Entry(windowsquare)
EagEntry.grid(row=0, column=0, padx=5, pady=5)
tk.Label(windowsquare, text='ظلع مربع').grid(row=0, column=1, padx=10, pady=10)

btnMasahat=tk.Button(windowsquare, text='مساحت', command=Masahat)
btnMasahat.grid(row=2, column=0, pady=10, padx=10)

btnMohet=tk.Button(windowsquare, text='محیط', command=Mohet)
btnMohet.grid(row=2, column=1, pady=10, padx=10)

windowsquare.mainloop()