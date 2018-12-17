from tkinter import *
from tkinter import ttk
import math

root = Tk()
root.title('КАЛЬКУЛЯТОР')
style = ttk.Style()
style.configure('TButton', background='white', foreground='navy',
                font=("Arial", 12))
# keycod = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 187, 189, 16, 17, 18, 13]
keycod = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
          106, 107, 109, 110, 111, 8, 16, 17, 18, 13]
button_list = [
    '%', '√', 'x²', 'C',
    '(', ')', '1/x', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+/-', '0', '.', '='
]
st = 1
for i in range(len(button_list)):
    if i >= st*4:
        st += 1

    def com(x=button_list[i]): return calculation(x)
    ttk.Button(root, text=button_list[i], command=com).grid(row=st, column=i % 4,
                                                            ipady=10)

calculator = Entry(root, width=24, state='normal')
calculator.grid(row=0, column=0, columnspan=4)
calculator.focus()
calculator.configure(font=("Arial", 24), insertontime=0,
                     relief='solid', fg='navy')
# calculator.configure(insertwidth=1, insertontime=1000,
#                      fg='white', bg='black', font='bold')


def calculation(key):
    calculator.focus()
    if '=' in calculator.get():
        calculator.delete(0, END)
    elif key == '=':
        try:
            result = eval(calculator.get())
            calculator.insert(END, f'={str(result)}')
        except:
            calculator.delete(0, END)
            calculator.insert(0, 'ОШИБКА')
    elif key == 'C':
        calculator.delete(0, END)
    elif key == 'x²':
        try:
            result = float(calculator.get())**2
            num = calculator.get()
            calculator.delete(0, END)
            calculator.insert(0, f'{str(num)}² = {str(result)}')
        except:
            calculator.delete(0, END)
    elif key == '1/x':
        try:
            result = 1/float(calculator.get())
            num = calculator.get()
            calculator.delete(0, END)
            calculator.insert(0, f'1 / {str(num)} = {str(result)}')
        except:
            calculator.delete(0, END)
    elif key == '%':
        try:
            result = eval(calculator.get()) / 100
            calculator.delete(0, END)
            calculator.insert(0, f'{str(result)}')
        except:
            calculator.delete(0, END)
    elif key == '√':
        try:
            result = math.sqrt(float(calculator.get()))
            num = calculator.get()
            calculator.delete(0, END)
            calculator.insert(0, f'√{str(num)} = {str(result)}')
        except:
            calculator.delete(0, END)
    elif key == '+/-':
        try:
            if calculator.get()[0] == '-':
                calculator.delete(0)
            elif calculator.get()[0] == '+':
                calculator.delete(0)
                calculator.insert(0, '-')
            else:
                calculator.insert(0, '-')
        except IndexError:
            pass
    else:
        calculator.insert(END, key)


def k(event):
    print(event.keycode)
    ekey = event.keycode
    n = calculator.index(INSERT)
    if ekey not in keycod:
        calculator.delete(n-1)
    elif ekey == 13:
        calculation(key='=')
    elif '=' in calculator.get():
        calculator.delete(0, END)


root.bind('<Key>', k)

root.mainloop()
