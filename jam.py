import tkinter as tk
from tkinter import messagebox

def maghsum(a):
    list1=list()
    for i in range(1, a+1):
        if a%i==0:
            list1.append(i)
    return list1
def natiche():
    try:
        
        num1=int(numEntry1.get())
        num2=int(numEntry2.get())
        list1=list()
        for i in range(num1,num2+1):
                    if len(maghsum(i))==2:
                        list1.append(i)
        
        sum1=sum(list1)       
        messagebox.showinfo(title='نتیجه', message=f"{list1} | {sum1} ")
          
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
                    