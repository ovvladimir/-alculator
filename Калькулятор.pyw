from tkinter import END, Entry, INSERT, Tk, ttk
from math import sqrt

root = Tk()
root.title('КАЛЬКУЛЯТОР')
style = ttk.Style()
style.configure('TButton', background="#fff", foreground='navy', font='Arial 12')
'''
key_code = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 187, 189, 16, 17, 18, 13]
key_code = [96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
            106, 107, 109, 110, 111, 8, 16, 17, 18, 13]
key_sym = ['Right', 'Left', 'asterisk', 'slash', 'minus', 'plus', 'Return',
           'space', 'Escape', 'BackSpace']
'''
button_list = [
    '%', '√', 'x²', 'C',
    '(', ')', '1/x', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+/-', '0', '.', '=']

for i in range(len(button_list)):
    def com(k=button_list[i]): return calculation(k)
    ttk.Button(root, text=button_list[i], command=com).grid(row=i//4+1,
                                                            column=i % 4,
                                                            ipady=10)

calculator = Entry(root, width=24)
calculator.focus()
calculator.configure(font='Arial 24', insertontime=0,
                     relief='solid', state='normal', fg='navy')
calculator.grid(row=0, column=0, columnspan=4)
"""calculator.configure(insertwidth=1, insertontime=1000,
                     fg='white', bg='black', font='bold')"""


def calculation(key):
    calculator.focus()
    if '=' in calculator.get() or 'error' in calculator.get():
        calculator.delete(0, END)
    elif key == '=':
        try:
            result = eval(calculator.get())
            if type(result) is float:  # if result % 1 != 0:
                r = list(str(result))
                if r[0] == '0' and r[2] == '0' and r[3] != '0':
                    calculator.insert(END, f'={"%.3f" % result}')
                elif r[0] == '0' and r[2] == '0' and r[3] == '0':
                    calculator.insert(END, f'={"%.5f" % result}')
                elif 'e' in r:
                    calculator.insert(END, f'={result}')
                else:
                    calculator.insert(END, f'={"%.1f" % result}')
            else:
                calculator.insert(END, f'={result}')
        except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
            calculator.delete(0, END)
            calculator.insert(0, 'error')
    elif key == 'C':
        calculator.delete(0, END)
    elif key == 'x²':
        try:
            result = float(calculator.get())**2
            num = calculator.get()
            calculator.delete(0, END)
            calculator.insert(0, f'{num}²={result}')
        except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
            calculator.delete(0, END)
    elif key == '1/x':
        try:
            result = 1/float(calculator.get())
            num = calculator.get()
            calculator.delete(0, END)
            calculator.insert(0, f'1/{num}={result}')
        except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
            calculator.delete(0, END)
    elif key == '%':
        try:
            result = eval(calculator.get()) / 100
            calculator.delete(0, END)
            calculator.insert(0, f'{str(result)}')
        except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
            calculator.delete(0, END)
    elif key == '√':
        try:
            result = sqrt(float(calculator.get()))  # math
            num = calculator.get()
            calculator.delete(0, END)
            calculator.insert(0, f'√{num}={result}')
        except (ZeroDivisionError, SyntaxError, IndexError, ValueError, NameError):
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


def sym(e):
    e_key = e.keysym
    # print(e.keycode, e.keysym, len(e_key))
    n = calculator.index(INSERT)
    if e_key not in button_list and len(e_key) <= 2:
        calculator.delete(n-1)
    elif e_key == 'Return':
        calculation('=')
    elif '=' in calculator.get() or 'error' in calculator.get() and len(e_key) <= 2:
        calculator.delete(0, END)


root.bind('<Key>', sym)

root.mainloop()
