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
        num2 = int(numEntry2.get())
        
        maghsum1=maghsum(num1)
        maghsum2=maghsum(num2)
        
        # در این مرحله مقسوم علیه های بدست امده را به مجموعه تبدیل می کنیم
        
        m1=set(maghsum1)
        m2=set(maghsum2)
        
        # حال به کمک تابع اشتراک در مجموعه ها اشتراک اندو را پیدا می کنیم
        
        eshterak=m1.intersection(m2)
        
        # حال در این قسمت برای بدست اوردن بزرگترینمقسوم علیه مشترک کافی ست آن را ابتدا به لیست تبدیل کینم
        # سپس از لیست با تابعmax بزرگترین را پیدا می کنیم
        
        eshterakList=list(eshterak)
        bmm=max(eshterakList)
        kmm=(num1*num2)//bmm
        labelsaghf.configure(text=f" , کوچترین مضرب مشترک برابر است با: {kmm}بزرگترین مقسوم علیه برابرست با {bmm}")
    except:
        messagebox.showerror("خطا", "لطفاً فقط اعداد صحیح وارد کنید.")
    

window=tk.Tk()
window.title('برنامه مقسوم علیه')
maqsEntry=tk.Entry(window)

numEntry1=tk.Entry(window)
numEntry1.grid(row=0, column=0, padx=5, pady=5)

tk.Label(window, text='عدد اول').grid(row=0, column=1, padx=10, pady=10)

numEntry2=tk.Entry(window)
numEntry2.grid(row=1, column=0, padx=5, pady=5)
tk.Label(window, text='عدد دوم').grid(row=1, column=1, padx=10, pady=10)

btn2=tk.Button(window, text='نتیجه', command=natiche)
btn2.grid(row=2, column=0, pady=10, padx=10)
labelsaghf=tk.Label(window, text='')
labelsaghf.grid(row=3, column=0, padx=10, pady=10)


window.mainloop()
                    