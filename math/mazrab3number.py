import tkinter as tk


def chekmzerb():
    num1=int(E1.get().strip())
    num2=int(E2.get().strip())
    num3=int(E3.get().strip())
    result=""
    if (num1%num2)==0:
        result+=f"عدد {num1} بر عدد {num2} بخش پذیر است\n"
        # label.configure(text=f"عدد و عدد {num3} {num1} مضرب عدد {num2} می باشد")
    if (num1%num3)==0:
        result+=f"عدد {num1} بر عدد {num3} بخش پذیر است\n"
    if  (num2%num3)==0:
        result+=f"عدد {num2} بر عدد {num3} بخش پذیر است\n"
      
    label.configure(text=result) 


win=tk.Tk()
win.title("بررسی مضرب دو عدد")
E1=tk.Entry(win)
E1.grid(row=0, column=0)
tk.Label(win, text='عدد اول').grid(row=0, column=1,padx=5,pady=5)

E2=tk.Entry(win)
E2.grid(row=1, column=0)
tk.Label(win, text='عدد دوم').grid(row=1, column=1, padx=5,pady=5)

E3=tk.Entry(win)
E3.grid(row=2, column=0)
tk.Label(win, text='عدد سوم').grid(row=2, column=1,padx=5,pady=5)


btnlogin1=tk.Button(win, text="بررسی", command=chekmzerb)
btnlogin1.grid(row=3, column=0, pady=5, padx=5)

label=tk.Label(win, text='')
label.grid(row=4, column=0, padx=5, pady=5)




win.mainloop()