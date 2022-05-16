from tkinter import *
from datetime import *
import datetime

endTime = datetime.datetime(2022,12,30,9)
root = Tk()
lb = Label(root, font=('arial',80), anchor='center',bg="black",fg='white')
txt = StringVar()

def cant_wait():
    timeLeft = endTime - datetime.datetime.now()
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
    txt.set(timeLeft)
    lb.config(textvariable=txt)
    lb.after(1000, cant_wait)


root.title('CountDown')
root.geometry('600x600')
lb.pack(anchor='center',fill='both',expand=1)

cant_wait()

mainloop()

