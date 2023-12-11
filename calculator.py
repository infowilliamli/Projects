from tkinter import *


def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        equation_text = str(eval(equation_text))
        equation_label.set(equation_text)

    except ZeroDivisionError:
        equation_label.set("Cannot divide by zero")
        equation_text = ""

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text = ""


def clear():
    global equation_text

    equation_text = ""
    equation_label.set(equation_text)


window = Tk()
window.title("Python Calculator")
window.geometry("480x500")
window.config(bg="black")

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Arial', 20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1), relief=RAISED, bd=5)
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2), relief=RAISED, bd=5)
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3), relief=RAISED, bd=5)
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4), relief=RAISED, bd=5)
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5), relief=RAISED, bd=5)
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6), relief=RAISED, bd=5)
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7), relief=RAISED, bd=5)
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8), relief=RAISED, bd=5)
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9), relief=RAISED, bd=5)
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0), relief=RAISED, bd=5)
button0.grid(row=3, column=1)

dot = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'), relief=RAISED, bd=3)
dot.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'), relief=RAISED, bd=3)
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'), relief=RAISED, bd=3)
minus.grid(row=1, column=3)

times = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'), relief=RAISED, bd=3)
times.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'), relief=RAISED, bd=3)
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, command=equals, relief=RAISED, bd=3)
equal.grid(row=3, column=2)

clear_button = Button(window, text='Clear', height=4, width=9*4, font=35, command=clear, relief=RAISED, bd=10)
clear_button.pack()

window.mainloop()
