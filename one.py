import tkinter as tk
from tkinter import messagebox

def count_maghsum(a):
    # این تابع یک ورودی دارد و مقسوم عیله های آن عدد را بر می گرداند
    list1=list()
    for i in range(1, a//2+1):
        if a%i==0:
            list1.append(i)
    return len(list1)+1
def natiche():
    try:
         num1 = int(numEntry1.get())
         count1=count_maghsum(num1)
         if count1==2:
          messagebox.showinfo(title='عدد اول', message=f"این عدد اول است")
         #labelsaghf.configure(text=f" تعداد مقسوم علیه برابر است با {count1} ")
         else :
            messagebox.showinfo(title='عدد ', message=f"این عدد اول نیست")
    except:
        messagebox.showerror("خطا", "لطفاً فقط اعداد صحیح وارد کنید.")
    
window=tk.Tk()
window.title('برنامه مقسوم علیه')
maqsEntry=tk.Entry(window)

numEntry1=tk.Entry(window)
numEntry1.grid(row=0, column=0, padx=5, pady=5)

tk.Label(window, text='عدد اول').grid(row=0, column=1, padx=10, pady=10)

btn2=tk.Button(window, text='نتیجه', command=natiche)
btn2.grid(row=1, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()
                    