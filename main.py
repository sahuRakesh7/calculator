from tkinter import *

w = Tk()
w.title("My Calculator")
w.config(bg="#1C1C1C")


def clear():
    display.delete(0, END)


def btn_clk(num):
    cur_num = display.get()
    clear()
    final_num = cur_num + num
    display.insert(0, final_num)


first_num = 0
math = ''


def calc(math_type):
    global first_num, math
    math = math_type
    first_num = display.get()
    clear()


def equal():
    result = ''
    global first_num
    second_num = display.get()
    clear()
    if math == 'add':
        result = int(first_num) + int(second_num)
    elif math == 'sub':
        result = int(first_num) - int(second_num)
    elif math == 'mul':
        result = int(first_num) * int(second_num)

    if math == 'div':
        result = int(first_num) / int(second_num)
    display.insert(0, str(result))


# Main dispaly
display = Entry(w, width=15, font=("Arial", 26, "bold"), justify=RIGHT, bg="#1C1C1C", fg="#D4D4D2")

# Button row
Btn_0 = Button(w, text=0, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('0'))
Btn_1 = Button(w, text=1, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('1'))
Btn_2 = Button(w, text=2, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('2'))

Btn_3 = Button(w, text=3, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('3'))
# row 2
Btn_4 = Button(w, text=4, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('4'))
Btn_5 = Button(w, text=5, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('5'))
Btn_6 = Button(w, text=6, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('6'))
# row 1
Btn_7 = Button(w, text=7, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('7'))
Btn_8 = Button(w, text=8, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('8'))
Btn_9 = Button(w, text=9, padx=35, pady=10, font=('Arial', 14), bg="#505050", fg="white", command=lambda: btn_clk('9'))

Btn_Clear = Button(w, text='Clear', padx=68, pady=10, font=('Arial', 14), bg='#D4D4D2', fg="Black", command=clear)
Btn_Div = Button(w, text='/', padx=36, pady=10, font=('Arial', 14), bg='#FF9500', fg="white",
                 command=lambda: calc("div"))
Btn_Mul = Button(w, text='*', padx=36, pady=10, font=('Arial', 14), bg='#FF9500', fg="white",
                 command=lambda: calc("mul"))

Btn_add = Button(w, text='+', padx=36, pady=10, font=('Arial', 14), bg='#FF9500', fg="white",
                 command=lambda: calc("add"))
Btn_sub = Button(w, text='-', padx=36, pady=10, font=('Arial', 14), bg='#FF9500', fg="white",
                 command=lambda: calc("sub"))

Btn_equal = Button(w, text='=', padx=35, pady=39, font=('Arial', 14), bg='#FF9500', fg="white", command=equal)

# dispaly Grid
Btn_equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)

Btn_add.grid(row=6, column=1, padx=2, pady=2)
Btn_sub.grid(row=6, column=0, padx=2, pady=2)

Btn_Mul.grid(row=5, column=1, padx=2, pady=2)
Btn_Div.grid(row=5, column=0, padx=2, pady=2)

Btn_Clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
Btn_0.grid(row=4, column=0, padx=2, pady=2)

Btn_1.grid(row=3, column=0, padx=2, pady=2)
Btn_2.grid(row=3, column=1, padx=2, pady=2)
Btn_3.grid(row=3, column=2, padx=2, pady=2)

Btn_4.grid(row=2, column=0, padx=2, pady=2)
Btn_5.grid(row=2, column=1, padx=2, pady=2)
Btn_6.grid(row=2, column=2, padx=2, pady=2)

Btn_7.grid(row=1, column=0, padx=2, pady=2)
Btn_8.grid(row=1, column=1, padx=2, pady=2)
Btn_9.grid(row=1, column=2, padx=2, pady=2)

display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, )

w.mainloop()
