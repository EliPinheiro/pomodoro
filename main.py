from tkinter import *
from time import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
voltas = 0


def contar(count):
    global voltas, x
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count >= 0:
        x = window.after(1000,contar, count-1)

    if count < 0:
        start()








def start():
    global voltas
    print(voltas)
    voltas += 1
    if voltas > 8:
        canvas.itemconfig(timer_text, text=f'{WORK_MIN}:00')
        voltas = 0
        done['text'] = ''
    elif voltas == 8:
        time_label['text'] = 'Long Break'
        done['text'] += '✔'
        contar(1200)
    elif voltas % 2 != 0:
        time_label['text'] = 'Work'
        contar(1500)
    elif voltas % 2 == 0:
        time_label['text'] = 'short Break'
        done['text'] += '✔'
        contar(300)

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global contar, timer_text, start,x, voltas
    window.after_cancel(x)
    canvas.itemconfig(timer_text,text= f'{WORK_MIN}:00')
    voltas = 0
    done['text']=''
    time_label['text']= 'TIMER'

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('apple')
# window.geometry('300x300')
window.config(pady=50,padx=50,bg=YELLOW)


time_label = Label(window,text='TIMER',font='Arial 20',bg=YELLOW,fg=GREEN)
time_label.grid(column=1,row=0)

canvas =Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
apple_image = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=apple_image)
timer_text = canvas.create_text(100,130,text= f'{WORK_MIN}:00',font='Arial 30',fill='white')
canvas.grid(column=1,row=1)



reset_photo = PhotoImage(file='reset.png')
reset_button = Button(window,height=25, image=reset_photo, command=reset)
reset_button.grid(column=2,row=2)

done = Label(window,text='',bg=YELLOW,padx=10,pady=20,fg=GREEN)
done.grid(column=1,row=2,rowspan=1)

start_photo = PhotoImage(file='start.png')
start_button = Button(window, image=start_photo, command=start)
start_button.grid(column=0,row=2)



window.mainloop()