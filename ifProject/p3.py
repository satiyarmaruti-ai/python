#x=int(input("insert the number:"))
def checkStatus():
    try:
        x=int(number.get().strip())
        print(x<0)
        if (x<=5 and x>=0):
            messagebox.showinfo(title='مشاهده وضعیت', message='وضعیت شما خیلی ضعیف می باشد')
            # print("very weak")
        elif(x<=10 and x>5):
            messagebox.showinfo(title='مشاهده وضعیت', message='وضعیت شما ضعیف می باشد')
            #print("weak")
        elif(x<=15 and x>10):
            messagebox.showinfo(title='مشاهده وضعیت', message='وضعیت شما متوسط می باشد')
            #print("nomral")
        elif(x<=20 and x>15):
            messagebox.showinfo(title='مشاهده وضعیت', message='وضعیت شما خوب می باشد')
            #print("good")
        else:
            messagebox.showerror(title='خطای ورودی ', message='لطفا یک عدد بین 0 تا 20 را درج نمایید')
            #print("please insert the covrect number")
    except:
            messagebox.showerror(title='خطا ی سیستمی', message='لطفا در وارد کردن اطلاعات دقت نمایید.')


import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title('برنامه بررسی نمره')
number=tk.Entry(window)
number.grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text='نمره را وارد نمایید').grid(row=0, column=1, padx=10, pady=10)

btnCheck=tk.Button(window, text='مشاهد وضعیت', command=checkStatus)
btnCheck.grid(row=2, column=0, pady=10, padx=10)

window.mainloop()