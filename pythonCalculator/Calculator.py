# Importing everything from tkinter
from tkinter import *
from tkinter.messagebox import showerror

# Creating a GUI
root = Tk()
root.title("Calculator")
root.geometry('265x400')
root.resizable(0, 0)
root.configure(background='#A9A9A9')

# StringVar variables
entry_strvar = StringVar(root)

# Defining the top
eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=26, font=12)
eqn_entry.place(x=10, y=10)


# Creating the functions
def add_text(text, strvar: StringVar):
    current_text = strvar.get()
    if current_text.endswith('='):
        strvar.set(text)
    else:
        strvar.set(f'{current_text}{text}')


def submit(entry: Entry, strvar: StringVar):
    operation = entry.get()
    try:
        result = eval(operation)
        strvar.set(f"{operation}={result}")
    except:
        showerror('Error!', 'Please enter a properly defined equation!')


# Number Buttons
Button(root, height=2, width=5, text='7', font=9, bg='White', command=lambda: add_text("7", entry_strvar)).place(x=5, y=170)
Button(root, height=2, width=5, text='8', font=9, bg='White', command=lambda: add_text('8', entry_strvar)).place(x=65, y=170)
Button(root, height=2, width=5, text='9', font=9, bg='White', command=lambda: add_text('9', entry_strvar)).place(x=125, y=170)
Button(root, height=2, width=5, text='4', font=9, bg='White', command=lambda: add_text('4', entry_strvar)).place(x=5, y=225)
Button(root, height=2, width=5, text='5', font=9, bg='White', command=lambda: add_text('5', entry_strvar)).place(x=65, y=225)
Button(root, height=2, width=5, text='6', font=9, bg='White', command=lambda: add_text('6', entry_strvar)).place(x=125, y=225)
Button(root, height=2, width=5, text='1', font=9, bg='White', command=lambda: add_text('1', entry_strvar)).place(x=5, y=280)
Button(root, height=2, width=5, text='2', font=9, bg='White', command=lambda: add_text('2', entry_strvar)).place(x=65, y=280)
Button(root, height=2, width=5, text='3', font=9, bg='White', command=lambda: add_text('3', entry_strvar)).place(x=125, y=280)
Button(root, height=2, width=5, text='0', font=9, bg='White', command=lambda: add_text('0', entry_strvar)).place(x=5, y=340)

# Operator Buttons
Button(root, height=2, width=5, text='+', font=9,fg='White', bg='Black', command=lambda: add_text('+', entry_strvar)).place(x=195, y=340)
Button(root, height=2, width=5, text='-', font=9,fg='White', bg='Black', command=lambda: add_text('-', entry_strvar)).place(x=195, y=280)
Button(root, height=2, width=5, text='x', font=9,fg='White', bg='Black', command=lambda: add_text('*', entry_strvar)).place(x=195, y=225)
Button(root, height=2, width=5, text='/', font=9,fg='White', bg='Black', command=lambda: add_text('/', entry_strvar)).place(x=195, y=170)
Button(root, height=2, width=5, text='.', font=9,fg='White', bg='Black', command=lambda: add_text('.', entry_strvar)).place(x=65, y=340)
Button(root, height=2, width=5, text='(', font=9,fg='White', bg='Black', command=lambda: add_text('(', entry_strvar)).place(x=65, y=110)
Button(root, height=2, width=5, text=')', font=9,fg='White', bg='Black', command=lambda: add_text(')', entry_strvar)).place(x=125, y=110)

# Equal, C and AC buttons
Button(root, height=2, width=5, text='=', font=9, bg='Blue', command=lambda: submit(eqn_entry, entry_strvar)).place(x=125, y=340)
Button(root, height=2, width=5, text='C', font=9, bg='Green', command=lambda: add_text('', entry_strvar)).place(x=195, y=110)
Button(root, height=2, width=5, text='AC', font=9, bg='Red', command=lambda: entry_strvar.set('')).place(x=5, y=110)

# Updating root
root.update()
root.mainloop()
