
import tkinter as tk
from tkinter import messagebox


def checkNumber():
    try:
        num1=float(numEntry1.get().strip())
        num2=float(numEntry2.get().strip())
        
        min=num1
        max=num1
        
        if num2<min:
            min=num2
        if num2>max:
            max=num2
        
        messagebox.showinfo(title=f'بررسی عدد {num1} و {num2}', message=f'min= {min}  max={max}')
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


btnmax=tk.Button(window, text="بررسی عدد",command=checkNumber )
btnmax.grid(row=2, column=0, pady=5, padx=5)




window.mainloop()
                    