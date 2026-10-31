import tkinter as tk
from tkinter import messagebox

def showName():
   print("Satiar")

def betonAndmilgerd ():
 metrazh=int(betonEntry.get().strip())
 beton=(metrazh)
 milgerd=metrazh*50
 labelmilgerd.configure(text=f"میلگرد مورد نیاز برابر است با   {milgerd} کیلوگرم ")
 labelBeton.configure(text=f"بتن مورد نیاز برابر است با   {beton} ")
#  messagebox.showinfo(title='میزان بتن', message=f":   بتن مورد نیاز برابر است با   {beton} ")
 milgerd=metrazh*50
 #messagebox.showinfo(title='میزان lمیلگرد', message=f"میلگرد مورد نیاز برابر است با:  {milgerd} کیلو گرم ")

   
def showPageSaghf():

    newWin=tk.Toplevel(windowbeton)
    saghfEntry=tk.Entry(newWin)
    saghfEntry.grid(row=1, column=0, padx=10, pady=10)
    tk.Label(newWin, text='متراژ سقف را درج نمایید').grid(row=1, column=1, padx=10, pady=10)

    btn1=tk.Button(newWin, text=' سقف', command=lambda: saghf(saghfEntry))
    btn1.grid(row=2, column=0, pady=10, padx=10)

def saghf(saghfMeter):
    
    meterSaghf=saghfMeter.get().strip()
    messagebox.showinfo(title='', message=meterSaghf)

    
 

windowbeton=tk.Tk()
betonEntry=tk.Entry(windowbeton)
betonEntry.grid(row=1, column=0, padx=10, pady=10)
tk.Label(windowbeton, text='متراژ بنا را وراد نمایید').grid(row=1, column=1, padx=10, pady=10)

btnbeton2=tk.Button(windowbeton, text='محاسب زیر بنا', command=betonAndmilgerd)
btnbeton2.grid(row=2, column=0, pady=10, padx=10)

labelBeton=tk.Label(windowbeton, text='')
labelBeton.grid(row=3, column=0, padx=10, pady=10)

labelmilgerd=tk.Label(windowbeton, text='')
labelmilgerd.grid(row=4, column=0, padx=10, pady=10)

btn2=tk.Button(windowbeton, text='محاسبه سقف', command=showPageSaghf)
btn2.grid(row=5, column=0, pady=10, padx=10)
labelsaghf=tk.Label(windowbeton, text='')
labelsaghf.grid(row=4, column=0, padx=10, pady=10)


windowbeton.mainloop()