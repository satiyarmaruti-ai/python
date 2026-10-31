import tkinter as tk

def press(key):
    if key == "=":
        try:
            
            nuumbers = float(entry.get().strip())
            label_res.config(text=f" {nuumbers}")
        except:
            
            label_res.config(text="")
    elif key == "C":
        
        entry.delete(0, tk.END)
        label_res.config(text=" ")
    else:
        
        entry.insert(tk.END, key)

root = tk.Tk()
root.title("")
root.geometry("")


entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10, padx=10)


label_res = tk.Label(root, text=" ", font=("", 12))
label_res.pack(pady=5)


btns = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

frame = tk.Frame(root)
frame.pack()


for i, char in enumerate(btns):
    btn = tk.Button(frame, text=char, width=5, height=2, 
                    command=lambda c=char: press(c))
    btn.grid(row=i//4, column=i%4, padx=2, pady=2)

root.mainloop()