import tkinter as tk


def chekmzerb():
    num1=int(E1.get().strip())
    num2=int(E2.get().strip())

    if (num1%num2)==0:
        label.configure(text=f"عدد {num1} مضرب عدد {num2} می باشد")
    elif (num2%num1)==0:
        label.configure(text=f"عدد {num2} مضرب عدد {num1} می باشد")
    else:
        label.configure(text=f"عدد {num2} مضرب عدد {num1} همدیگر نمی باشند")



win=tk.Tk()
win.title("بررسی مضرب دو عدد")
# win.geometry("500*500")
E1=tk.Entry(win)
E1.grid(row=0, column=0)
tk.Label(win, text='عدد اول').grid(row=0, column=1,padx=5,pady=5)

E2=tk.Entry(win)
E2.grid(row=1, column=0)
tk.Label(win, text='عدد دوم').grid(row=1, column=1, padx=5,pady=5)

btnlogin1=tk.Button(win, text="بررسی", command=chekmzerb)
btnlogin1.grid(row=2, column=0, pady=5, padx=5)

label=tk.Label(win, text='')
label.grid(row=3, column=0, padx=5, pady=5)


win.mainloop()