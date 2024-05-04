import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("calculator")
root.iconbitmap('D:\python\git_proj\mini calculator\\cal.ico')
root.geometry('250x250')
root.resizable(False,False)

field__text = " "
Input_text = tk.StringVar()

def on_click(text):
    global field__text
    field__text = field__text+ str(text)
    Input_text.set(field__text)

def button_clear():
    global field__text
    field__text = " "
    Input_text.set("")

def click_equal():
    global field__text
    try:
        result = str(eval(field__text))
        Input_text.set(result)
        field__text = result

    except SyntaxError:
        Input_text.set("syntax error")
        field__text = ""

    except ZeroDivisionError:
        Input_text.set("error! divide by zero")
        field__text = ""

frame1 = ttk.Frame(root, width=245, height=100)
frame1.pack()

frame2 = ttk.Frame(root, width=246, height=200)
frame2.pack()

entry = ttk.Entry(frame1, font=' arial 18',textvariable=Input_text, width=25, background='blue')
entry.pack(pady=10)

frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.columnconfigure(2, weight=1)
frame2.rowconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)
frame2.rowconfigure(2, weight=1)
frame2.rowconfigure(3, weight=1)
frame2.rowconfigure(4, weight=1)
frame2.rowconfigure(5, weight=1)

s = ttk.Style()
s.configure('TButton', font ='arial 18')

button9 = ttk.Button(frame2, text="9", style='TButton', command= lambda: on_click("9"))
button8 = ttk.Button(frame2, text="8", style='TButton', command=lambda:on_click("8"))
button7 = ttk.Button(frame2, text="7", style='TButton', command=lambda:on_click("7"))
button6 = ttk.Button(frame2, text="6", style='TButton', command=lambda:on_click("6"))
button5 = ttk.Button(frame2, text="5", style='TButton', command=lambda:on_click("5"))
button4 = ttk.Button(frame2, text="4", style='TButton', command=lambda:on_click("4"))
button3 = ttk.Button(frame2, text="3", style='TButton', command=lambda:on_click("3"))
button2 = ttk.Button(frame2, text="2", style='TButton', command=lambda:on_click("2"))
button1 = ttk.Button(frame2, text="1", style='TButton', command=lambda:on_click("1"))
button0 = ttk.Button(frame2, text="0", style='TButton', command=lambda:on_click("0"))
buttonpoint = ttk.Button(frame2, text=".", style='TButton', command=lambda:on_click("."))
button_add = ttk.Button(frame2, text="+", style='TButton', command=lambda:on_click("+"))
button_substraction = ttk.Button(frame2, text="-", style='TButton', command=lambda:on_click("-"))
button_equal = ttk.Button(frame2, text="=", style='TButton', command=click_equal)
button_clr = ttk.Button(frame2, text="clr", style='TButton', command=button_clear)
button_multiply = ttk.Button(frame2, text="*", style='TButton', command=lambda:on_click("*"))
button_division = ttk.Button(frame2, text="/", style='TButton', command=lambda:on_click("/"))




button7.grid(row=0 , column=0, sticky='nsew')
button8.grid(row=0 , column=1, sticky='nsew')
button9.grid(row=0 , column=2, sticky='nsew')
button4.grid(row=1 , column=0, sticky='nsew')
button5.grid(row=1 , column=1, sticky='nsew')
button6.grid(row=1 , column=2, sticky='nsew')
button1.grid(row=2 , column=0, sticky='nsew')
button2.grid(row=2 , column=1, sticky='nsew')
button3.grid(row=2 , column=2, sticky='nsew')
button0.grid(row=3 , column=0, sticky='nsew')
buttonpoint.grid(row=3 , column=1, sticky='nsew')
button_add.grid(row=4 , column=1, sticky='nsew')
button_substraction.grid(row=4 , column=2, sticky='nsew')
button_multiply.grid(row=5 , column=1, sticky='nsew')
button_division.grid(row=5 , column=2, sticky='nsew')
button_equal.grid(row=4 , column=0, sticky='nsew', rowspan=2)
button_clr.grid(row=3 , column=2, sticky='nsew')


root.mainloop()