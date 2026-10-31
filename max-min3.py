import tkinter as tk
from tkinter import messagebox


def checkNumber():
    try:
        num1=float(numEntry1.get().strip())
        num2=float(numEntry2.get().strip())
        num3=float(numEntry3.get().strip())
        num4=float(numEntry4.get().strip())
        
        # 1: تعرف لیست
        list1=list()
        
        # درج متغییر ها در لیست2
        list1.append(num1)
        list1.append(num2)
        list1.append(num3)
        list1.append(num4)
        
        
        min1=min(list1)
        max1=max(list1)
        
        # if num2>max:
        #     max=num2
        
        # if num2<min:
        #     min=num2
            
        # if num3<min:
        #     min=num3    
        # if num3>max:
        #     max=num3  
            
        # if num4<min:
        #     min=num4  
        # if num4>max:
        #     max=num4
        
        # messagebox.showinfo(title='', message=list1)
        
        messagebox.showinfo(title=f'بررسی عدد {num1} و {num2} و عدد {num3} , {num4}', message=f'min= {min1}  max={max1}')
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




btnmax=tk.Button(window, text="بررسی عدد",command=checkNumber )
btnmax.grid(row=4, column=0, pady=5, padx=5)




window.mainloop()
                    