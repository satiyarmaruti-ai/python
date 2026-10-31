import tkinter as tk
from tkinter import messagebox


def checkNumber():
    try:
        num1=float(numEntry1.get().strip())
        num2=float(numEntry2.get().strip())
        num3=float(numEntry3.get().strip())
        num4=float(numEntry4.get().strip())
        shmare=int(shmare1.get().strip())
        
        # 1: تعرف لیست
        list1=list()
        
        # درج متغییر ها در لیست2
        list1.append(num1)
        list1.append(num2)
        list1.append(num3)
        list1.append(num4)
        
        print(list1[shmare-1])
        
        plus=sum(list1)
        messagebox.showinfo(title=f'بررسی عدد {num1} و {num2} و عدد {num3} , {num4}', message=f'حاصل جمع = {plus}')
    except:
        messagebox.showerror(title='خطای درج عدد', message='لطفا در وارد عدد دقت نمایید')
    
window=tk.Tk()
window.title('برنامه تشخیص بزرگترین وکوچکترین')
max_minEntry=tk.Entry(window)

numEntry1=tk.Entry(window)
numEntry1.grid(row=0, column=0, padx=5, pady=5)
tk.Label(window, text='عدد اول').grid(row=0, column=1, padx=10, pady=10)

numEntry2=tk.Entry(window)
numEntry2.grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text='عدد دوم').grid(row=1, column=1, padx=10, pady=10)

numEntry3=tk.Entry(window)
numEntry3.grid(row=2, column=0, padx=5, pady=5)
tk.Label(window, text='عدد سوم').grid(row=2, column=1, padx=10, pady=10)

numEntry4=tk.Entry(window)
numEntry4.grid(row=3, column=0, padx=5, pady=5)
tk.Label(window, text='عدد چهارم').grid(row=3, column=1, padx=10, pady=10)

shmare1=tk.Entry(window)
shmare1.grid(row=4, column=0, padx=5, pady=5)
tk.Label(window, text='شماره عدد').grid(row=4, column=1, padx=10, pady=10)




btnmax=tk.Button(window, text="بررسی عدد",command=checkNumber )
btnmax.grid(row=5, column=0, pady=5, padx=5)




window.mainloop()
                    