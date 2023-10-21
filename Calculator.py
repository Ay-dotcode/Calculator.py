from tkinter import *
from my_math import sin, cos, tan, sqrt



def buttons():
    Button(calculator, bg="black", height=2, width=30, activebackground="black", border=0,
           command=more_buttons).grid(row=0, columnspan=4)

    Button(calculator, text="C", bg="black", fg="brown", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.delete(0, END)).grid(row=2, column=0)
    Button(calculator, text="(", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "(")).grid(row=2, column=1)
    Button(calculator, text=")", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, ")") if user_input.get() else None).grid(row=2, column=2)
    Button(calculator, text="÷", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "/") if user_input.get() else None).grid(row=2, column=3)

    Button(calculator, text="7", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "7")).grid(row=3, column=0)
    Button(calculator, text="8", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "8")).grid(row=3, column=1)
    Button(calculator, text="9", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "9")).grid(row=3, column=2)
    Button(calculator, text="x", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "*") if user_input.get() else None).grid(row=3, column=3)

    Button(calculator, text="4", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "4")).grid(row=4, column=0)
    Button(calculator, text="5", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "5")).grid(row=4, column=1)
    Button(calculator, text="6", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "6")).grid(row=4, column=2)
    Button(calculator, text="-", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "-")).grid(row=4, column=3)

    Button(calculator, text="1", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "1")).grid(row=5, column=0)
    Button(calculator, text="2", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "2")).grid(row=5, column=1)
    Button(calculator, text="3", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "3")).grid(row=5, column=2)
    Button(calculator, text="+", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "+")).grid(row=5, column=3)

    Button(calculator, text="+/-", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "(-")).grid(row=6, column=0)
    Button(calculator, text="0", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "0")).grid(row=6, column=1)
    Button(calculator, text=".", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, ".")).grid(row=6, column=2)
    Button(calculator, text="=", bg="green", fg="white", width=3, font="none 16 bold", activebackground="lime",
           command=equal).grid(row=6, column=3)


def more_buttons():
    Button(calculator, text="del", bg="white", fg="black", width=3, font="algerian 12", activebackground="black",
           activeforeground="white", command=lambda: user_input.delete(len(user_input.get()) - 1)).grid(row=1, column=4)
    Button(calculator, text="sin", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "sin(")).grid(row=2, column=4)
    Button(calculator, text="cos", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "cos(")).grid(row=3, column=4)
    Button(calculator, text="tan", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "tan(")).grid(row=4, column=4)
    Button(calculator, text="sqrt", bg="black", fg="green", width=3, font="none 16 bold", activebackground="grey",
           command=lambda: user_input.insert(END, "sqrt(")).grid(row=5, column=4)
    Button(calculator, text="Pre", bg="black", fg="white", width=3, font="none 16 bold", activebackground="grey",
           command=pre).grid(row=6, column=4)


def pre():
    user_input.delete(0, END)
    try:
        user_input.insert(END, ans[-1])
        ans.remove(ans[-1])
    except IndexError:
        user_input.insert(END, "End of list")


def equal():
    expression = user_input.get()
    try:
        answer = eval(expression)
        user_input.delete(0, END)
        user_input.insert(END, answer)
        ans.extend([expression, answer])
        print(ans)
    except Exception as error:
        if str(error) == "'(' was never closed (<string>, line 1)":
            user_input.insert(END, ")")
        else:
            user_input.delete(0, END)
            user_input.insert(END, "Error")
            print(str(error))


calculator = Tk()
calculator.title("Calculator")
calculator.configure(bg="black")
calculator.minsize(245, 300)
calculator.maxsize(300, 300)
ans = []

user_input = Entry(calculator, fg="black", font="none 16 bold", borderwidth=3)
user_input.grid(row=1, columnspan=4)
buttons()

calculator.mainloop()
