from tkinter import *


def clear():
    calc_screen.config(width=23, height=3, font=("Arial", 20))
    global equation_text

    equation_label.set("")
    equation_text = ""


def compute():
    global equation_text
    total = ""

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("ERROR: Invalid Syntax")

    except Exception as e:    
        calc_screen.config(width=38, height=5, font=("Arial", 12))
        equation_label.set(f"ERROR: {e}")
        

def add_number(num):
    calc_screen.config(width=23, height=3, font=("Arial", 20))

    global equation_text
    
    equation_text = equation_text + str(num)

    equation_label.set(equation_text)


def delete():
    global equation_text

    equation_text = str(equation_text)[:-1]
    equation_label.set(equation_text)


window = Tk()

equation_text = ""
equation_label = StringVar()

calc_frame = Frame(window, highlightbackground = "black", 
                         highlightthickness = 2, bd=0)
calc_frame.pack(side="top")

calc_screen = Label(calc_frame, textvariable=equation_label, fg="black", width=23, height=3, bg="white", font=("Arial", 20))
calc_screen.pack()

frame = Frame(window, bg="black", width=70)
frame.pack()

NUMBER_WIDTH = 4
NUMBER_HEIGHT = 2
FONT_SIZE = 20
paddingy = 1
paddingx = 1

number1 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=1, command= lambda: add_number(1), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number1.grid(pady=paddingy, padx=paddingx, row=1, column=0)

number2 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=2, command= lambda: add_number(2), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number2.grid(pady=paddingy, padx=paddingx, row=1, column=1)

number3 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=3, command= lambda: add_number(3), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number3.grid(pady=paddingy, padx=paddingx, row=1, column=2)

number4 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=4, command= lambda: add_number(4), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number4.grid(pady=paddingy, padx=paddingx, row=2, column=0)

number5 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=5, command= lambda: add_number(5), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number5.grid(pady=paddingy, padx=paddingx, row=2, column=1)

number6 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=6, command= lambda: add_number(6), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number6.grid(pady=paddingy, padx=paddingx, row=2, column=2)

number7 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=7, command= lambda: add_number(7), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number7.grid(pady=paddingy, padx=paddingx, row=3, column=0)

number8 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=8, command= lambda: add_number(8), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number8.grid(pady=paddingy, padx=paddingx, row=3, column=1)

number9 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=9, command= lambda: add_number(9), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number9.grid(pady=paddingy, padx=paddingx, row=3, column=2)

number0 = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=0, command= lambda: add_number(0), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
number0.grid(pady=paddingy, padx=paddingx, row=4, column=0)

decimal = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text=".", command= lambda: add_number("."), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
decimal.grid(pady=paddingy, padx=paddingx, row=4, column=1)

equals = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="=", command=compute, width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
equals.grid(pady=paddingy, padx=paddingx, row=4, column=2, columnspan=2, sticky = W+E)

multiply = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="*", command= lambda: add_number("*"), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
multiply.grid(pady=paddingy, padx=paddingx, row=1, column=3)

divide = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="/", command= lambda: add_number("/"), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
divide.grid(pady=paddingy, padx=paddingx, row=0, column=3)

minus = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="-", command= lambda: add_number("-"), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
minus.grid(pady=paddingy, padx=paddingx, row=3, column=3)

plus = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="+", command= lambda: add_number("+"), width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
plus.grid(pady=paddingy, padx=paddingx, row=2, column=3)

clear_all = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="AC", command=clear,  width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
clear_all.grid(pady=paddingy, padx=paddingx, row=0, column=0, columnspan=2, sticky = W+E)

delete = Button(frame, bg="white", activebackground="#f6f6f6", font=("Arial", FONT_SIZE), text="DEL", command=delete,  width=NUMBER_WIDTH, height=NUMBER_HEIGHT, borderwidth=0)
delete.grid(pady=paddingy, padx=paddingx, row=0, column=2)

window.mainloop()