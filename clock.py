from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    date_string = strftime("%A %d %B %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

time_label = Label(window, font=("Arial", 50), fg="#AF15E8", bg="black")
time_label.pack()

date_label = Label(window, font=("Silkscreen", 60), fg="#15DBE8", bg="black")
date_label.pack()

update()

window.mainloop()
