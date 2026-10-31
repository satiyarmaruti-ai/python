import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import turtle
from PIL import Image
t1=turtle.Turtle()

def zhkametUp():
    changeValue=int(progzakhamat['value'])
    progzakhamat['value']=changeValue+3
    # messagebox.showinfo(title='DATA', message=progzakhamat['value'])
    # pass
def kaehsh_zhkamet():
    changeValue=int(progzakhamat['value'])
    if int(progzakhamat['value'])>=5:
        progzakhamat['value']=changeValue-2
    
def speedUp():
    changeValue=int(progspeed['value'])
    progspeed['value']=changeValue+3
    
def kaehsh_speed():
    changeValue=int(progspeed['value'])
    if int(progspeed['value'])>=5:
        progspeed['value']=changeValue-2

def afzaesh_red():
    changeValue=int(prog_red_color['value'])
    prog_red_color['value']=changeValue+10
    
def kaehsh_red():
    changeValue=int(prog_red_color['value'])
    if int(prog_red_color['value'])>=10:
        prog_red_color['value']=changeValue-10

def afzaesh_green():
    changeValue=int(prog_green_color['value'])
    prog_green_color['value']=changeValue+10

def kaehsh_green():
    changeValue=int(prog_green_color['value'])
    if int(prog_green_color['value'])>=10:
        prog_green_color['value']=changeValue-10
def afzaesh_blue():
    changeValue=int(prog_blue_color['value'])
    prog_blue_color['value']=changeValue+10
def kaehsh_blue():
    changeValue=int(prog_blue_color['value'])
    if int(prog_blue_color['value'])>=10:
        prog_blue_color['value']=changeValue-10   
        
def pak_krden():
     screen1=t1.screen
     screen1.clearscreen()
 
def save_photo(): # متغیر pictures را اینجا به عنوان ورودی تعریف کردیم
    # try:
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="temp_draw.eps")
        
        img = Image.open("temp_draw.eps")
        img.save("my_drawing.png", "png")
        
        # print(f"عکس با موفقیت در temp_draw ذخیره شد.")
    # except Exception as e:
        # print(f"خطایی رخ داد: {e}")




def shkl():
            t1.reset()
        #try:
            tedadShape=int(tedadShapeEntry.get())
            azla=int(tehdadAzlaEntry1.get())
            zahkamat=int(progzakhamat['value'])
            speed=int(progspeed['value'])
            redcolor=int(prog_red_color['value'])
            
            greencolor=int(prog_green_color['value'])
            bluecolor=int(prog_blue_color['value'])
            andaze=int(anadezzeleEntry.get())
            zavieh=360/azla
            zavieh2=360/tedadShape
            t1.pensize(zahkamat)
            t1.speed(speed)
            t1.pencolor((redcolor/255,greencolor/255,bluecolor/255))
            for j in range(tedadShape):  
                t1.left(zavieh2)  
                for i in range(azla):
                    t1.forward(andaze)
                    t1.left(zavieh)       
        #except:
            #messagebox.showerror('خطا', 'لطفاً فقط اعداد صحیح وارد کنید.')
            
         
window=tk.Tk()
window.title('طراحی شکل')
resmEntry=tk.Entry(window)

tedadShapeEntry=tk.Entry(window)
tedadShapeEntry.grid(row=0, column=0, padx=5, pady=5)

tk.Label(window, text='تعداد شکل').grid(row=0, column=1, padx=10, pady=10)

tehdadAzlaEntry1=tk.Entry(window)
tehdadAzlaEntry1.grid(row=1, column=0, padx=5, pady=5)

tk.Label(window, text='تعداد ضلغ').grid(row=1, column=1, padx=10, pady=10)

anadezzeleEntry=tk.Entry(window)
anadezzeleEntry.grid(row=2, column=0, padx=5, pady=5)

tk.Label(window, text='اندازه ضلع').grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text='ضخامت').grid(row=3, column=0, padx=10, pady=10)
progzakhamat=ttk.Progressbar(window, orient='horizontal', length=300, mode='determinate')
progzakhamat.grid(row=3, column=1, padx=5, pady=5)
progzakhamat['value']=5
progzakhamat['maximum']=20
# tk.Label(window, text=' سرعت رسم').grid(row=3, column=1, padx=10, pady=10)

tk.Label(window, text='سرعت').grid(row=5, column=0, padx=10, pady=10)
progspeed=ttk.Progressbar(window, orient='horizontal', length=300, mode='determinate')
progspeed.grid(row=5, column=1, padx=5, pady=5)
progspeed['value']=5
progspeed['maximum']=20

tk.Label(window, text='رنگ قرمز').grid(row=7, column=0, padx=10, pady=10)
prog_red_color=ttk.Progressbar(window, orient='horizontal', length=255, mode='determinate')
prog_red_color.grid(row=7, column=1, padx=5, pady=5)
prog_red_color['value']=15
prog_red_color['maximum']=255

tk.Label(window, text='رنگ سبز').grid(row=9, column=0, padx=10, pady=10)
prog_green_color=ttk.Progressbar(window, orient='horizontal', length=255, mode='determinate')
prog_green_color.grid(row=9, column=1, padx=5, pady=5)
prog_green_color['value']=15
prog_green_color['maximum']=255

tk.Label(window, text='رنگ ابی').grid(row=11, column=0, padx=10, pady=10)
prog_blue_color=ttk.Progressbar(window, orient='horizontal', length=255, mode='determinate')
prog_blue_color.grid(row=11, column=1, padx=5, pady=5)
prog_blue_color['value']=15
prog_blue_color['maximum']=255

btn3=tk.Button(window, text='افزایش ضخامت', command=zhkametUp)
btn3.grid(row=4, column=0, pady=3, padx=3)

btn4=tk.Button(window, text='کاهش ضخامت', command=kaehsh_zhkamet)
btn4.grid(row=4, column=1, pady=3, padx=3)

btn5=tk.Button(window, text='افزایش سرعت', command=speedUp)
btn5.grid(row=6, column=0, pady=3, padx=3)

btn6=tk.Button(window, text='کاهش سرعت', command=kaehsh_speed)
btn6.grid(row=6, column=1, pady=3, padx=3)

btn7=tk.Button(window, text='افزایش قرمز', command=afzaesh_red)
btn7.grid(row=8, column=0, pady=3, padx=3)

btn8=tk.Button(window, text='کاهش قرمز', command=kaehsh_red)
btn8.grid(row=8, column=1, pady=3, padx=3)

btn9=tk.Button(window, text='افزایش سبز', command=afzaesh_green)
btn9.grid(row=10, column=0, pady=3, padx=3)

btn10=tk.Button(window, text='کاهش سبز', command=kaehsh_green)
btn10.grid(row=10, column=1, pady=3, padx=3)

btn9=tk.Button(window, text='افزایش ابی', command=afzaesh_blue)
btn9.grid(row=12, column=0, pady=3, padx=3)

btn10=tk.Button(window, text='کاهش ابی', command=kaehsh_blue)
btn10.grid(row=12, column=1, pady=3, padx=3)

btn2=tk.Button(window, text='طراحی', command=shkl)
btn2.grid(row=15, column=0, pady=3, padx=3)
btn11=tk.Button(window, text='پاک کردن', command=pak_krden)
btn11.grid(row=15, column=1, pady=3, padx=3)

btn12=tk.Button(window, text='ذخیره عکس', command=save_photo)
btn12.grid(row=16, column=1, pady=3, padx=3)

window.mainloop()
