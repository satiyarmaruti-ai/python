import tkinter as tk
from tkinter import messagebox

def betonAndmilgerd ():
 metrazh=int(betonEntry.get().strip())
 beton=(metrazh)
 milgerd=metrazh*50
 labelmilgerd.configure(text=f"میلگرد مورد نیاز برابر است با   {milgerd} کیلوگرم ")
 labelBeton.configure(text=f"بتن مورد نیاز برابر است با   {beton} بتن ")
#  messagebox.showinfo(title='میزان بتن', message=f":   بتن مورد نیاز برابر است با   {beton} ")
 milgerd=metrazh*50
 #messagebox.showinfo(title='میزان lمیلگرد', message=f"میلگرد مورد نیاز برابر است با:  {milgerd} کیلو گرم ")

   
def showPageSaghf():

    newWin=tk.Toplevel(windowbeton)
    saghfMeter=tk.Entry(newWin)
    saghfMeter.grid(row=1, column=0, padx=10, pady=10)
    tk.Label(newWin, text='متراژ سقف را درج نمایید').grid(row=1, column=1, padx=10, pady=10)

    btn1=tk.Button(newWin, text=' سقف', command=lambda:saghf(saghfMeter))
    btn1.grid(row=2, column=0, pady=10, padx=10)

def saghf(saghfMeter):
    meterSaghf=float(saghfMeter.get().strip())
    minMeter=meterSaghf*1.75
    maxMeter=meterSaghf*2
    messagebox.showinfo(title='', message=f"شما به حداقل {minMeter} , حداکثر {maxMeter} تیرچه نیاز دارید")

def showPagedivar():
  newWinDivar=tk.Toplevel(windowbeton)
  divarEntry=tk.Entry(newWinDivar)
  divarEntry.grid(row=1, column=0, padx=10, pady=10)
  tk.Label(newWinDivar, text='متراژ سقف را درج نمایید').grid(row=1, column=1, padx=10, pady=10)

  btn3=tk.Button(newWinDivar, text='محاسبه دیوار 35 سانتی متری ', command=lambda: divar(divarEntry)) 
  btn3.grid(row=2, column=0, pady=10, padx=10)

def divar(divarEntry):
   divar=float(divarEntry.get().strip())
   minMeter1=divar*200
   maxMeter1=divar*250
   messagebox.showinfo(title='', message=f"شما به حداقل {minMeter1} , حداکثر {maxMeter1} اجر 10 الی 20 سانتی متری نیاز دارید")
   
def nokteh():
  messagebox.showinfo(title='نکته', message="برای ساخت هر ساختمان  مختلف (مسکونی و اداری و تجاری و به خصوص ویژه ) وسایل مصالح مورد نیاز فرق میکند  ")


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

btn3=tk.Button(windowbeton, text='محاسبه دیوار 35 سانتی متری ', command= showPagedivar)
btn3.grid(row=6, column=0, pady=10, padx=10)

btn4=tk.Button(windowbeton, text='نکته ', command= nokteh)
btn4.grid(row=5, column=1, pady=10, padx=10)


windowbeton.mainloop()
