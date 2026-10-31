import tkinter as tk
from tkinter import messagebox

def maghsum(a):
    # این تابع یک ورودی دارد و مقسوم عیله های آن عدد را بر می گرداند
    list1=list()
    for i in range(1, a+1):
        if a%i==0:
            list1.append(i)
    return list1
def natiche():
    try:
        num1 = int(numEntry1.get())
        maghsum1=maghsum(num1)
        sum1=sum(maghsum1)
        labelsaghf.configure(text=f"مقسوم علیه برابرست با {maghsum1}  | مجموع برابرست با {sum1}")
    except:
        messagebox.showerror("خطا", "لطفاً فقط اعداد صحیح وارد کنید.")

window=tk.Tk()
window.title('برنامه مقسوم علیه')
maqsEntry=tk.Entry(window)

numEntry1=tk.Entry(window)
numEntry1.grid(row=0, column=0, padx=5, pady=5)

tk.Label(window, text='عدد ').grid(row=0, column=1, padx=10, pady=10)

btn2=tk.Button(window, text='حاصل جمع مقسوم علیه', command=natiche)
btn2.grid(row=3, column=1, pady=10, padx=10)

labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=4, column=0, padx=10, pady=10)

window.mainloop()
                    