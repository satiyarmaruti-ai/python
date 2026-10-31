# مساحت و محیط مستطیل با tkinter
import tkinter as tk
from tkinter import messagebox
def Masahat():
    lengthEntry1=int(lengthEntry.get().strip())
    widthEntry1=int(widthEntry.get().strip())
    m=lengthEntry1*widthEntry1
    # messagebox.showinfo(title='تست خروجی', message=f"طول مستطیل برابر است با {lengthEntry1}و عرض مستطیل برابر است با   {widthEntry1}")
    messagebox.showinfo(title='تست خروجی', message=f"مساحت مستطیل برابر است با:   {m}")

def Mohet():
    lengthEntry1=int(lengthEntry.get().strip())
    widthEntry1=int(widthEntry.get().strip())
    n=(lengthEntry1+widthEntry1)*2
    # messagebox.showinfo(title='تست خروجی', message=f"طول مستطیل برابر است با {lengthEntry1}و عرض مستطیل برابر است با   {widthEntry1}")
    messagebox.showinfo(title='تست خروجی', message=f"محیط مستطیل برابر است با:   {n}")


windowRectangle=tk.Tk()
windowRectangle.title('برنامه مساحت و محیط  مستطیل')
lengthEntry=tk.Entry(windowRectangle)
lengthEntry.grid(row=0, column=0, padx=5, pady=5)
tk.Label(windowRectangle, text='طول مستطیل').grid(row=0, column=1, padx=10, pady=10)

widthEntry=tk.Entry(windowRectangle)
widthEntry.grid(row=1, column=0, padx=10, pady=10)
tk.Label(windowRectangle, text='عرض مستطیل').grid(row=1, column=1, padx=10, pady=10)

btnMasahat=tk.Button(windowRectangle, text='مساحت', command=Masahat)
btnMasahat.grid(row=2, column=0, pady=10, padx=10)

btnMohet=tk.Button(windowRectangle, text='محیط', command=Mohet)
btnMohet.grid(row=2, column=1, pady=10, padx=10)

windowRectangle.mainloop()