import tkinter as tk
from tkinter import messagebox
import random

n="abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789"


def bedast_avardan():

    numRandom=int(add_Entry.get().strip())

    reshteh=''
    for i in range(numRandom):

        numRandom=random.randint(0,len(n)-1)
        charectr=n[numRandom]
        reshteh=reshteh+charectr

    label_result.configure(text=reshteh)


def bedastavardan2():

    win = tk.Toplevel(root)
    win.title("تولید اتوماتیک")
    win.geometry("300x300")

    tk.Label(win, text="تعداد تولید").pack(pady=5)

    tedad = tk.Entry(win)
    tedad.pack(pady=5)

    tk.Label(win, text="تعداد کاراکترهای هر رمز").pack(pady=5)

    tedad_char = tk.Entry(win)
    tedad_char.pack(pady=5)

    label = tk.Label(win, text="")
    label.pack(pady=10)

    def start():

        for i in range(int(tedad.get())):

            reshteh = ""

            for j in range(int(tedad_char.get())):
                reshteh += random.choice(n)

            label.configure(text=reshteh)

            win.update()
            win.after(1000)

    btn = tk.Button(
        win,
        text="شروع اتوماتیک",
        command=lambda: start()
    )
    btn.pack(pady=10)


root=tk.Tk()
root.title('برنامه ی به دست اوردن اعداد و کلمات تصادفی')

tk.Label(root, text="عدد اولی").grid(row=0,column=0,pady=5,padx=5)

add_Entry=tk.Entry(root)
add_Entry.grid(row=0,column=1,pady=5,padx=5)

label_result=tk.Label(root, text="")
label_result.grid(row=4,column=0,pady=5,padx=5)

bedastavardn=tk.Button(root, text='تولید تصادفی', command=bedast_avardan)
bedastavardn.grid(row=2,column=1,pady=5,padx=5)

bedastavardn=tk.Button(root, text='اتوماتیک', command=lambda: bedastavardan2())
bedastavardn.grid(row=2,column=0,pady=5,padx=5)

root.mainloop()