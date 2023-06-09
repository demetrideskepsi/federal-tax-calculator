from cProfile import label 
import tkinter as tk 
from tkinter import * 
import fed_tax_calc

window = tk.Tk() 

window.geometry("600x200")

window.title("Federal Tax Calculator")

calc = fed_tax_calc

options = [
	"Single",
	"Married"
]

clicked = StringVar() 
clicked.set(options[0]) 
dropDown = OptionMenu(window,clicked,*options) 
input = Entry(window,width=100,text=0) 
output = Text(window, height=1, borderwidth=0) 
income_label = Label(window, text='Income:')
tax_label = Label(window, text='Federal Income Taxes:')
net_income_label = Label(window, text='Net Income:')
net_income_result = Text(window, height=1,borderwidth=0)

def calculate(event): 
    c = clicked.get() 
    if c == options[0]: 
        output.delete(1.0,END) 
        calculated = calc.run_check('single',int(input.get())) 
        output.insert(1.0,calculated[0])
        net_income_result.delete(1.0,END)
        net_income_result.insert(1.0,calculated[1])
    elif c == options[1]: 
        output.delete(1.0,END) 
        calculated = calc.run_check('married',int(input.get())) 
        output.insert(1.0,calculated[0])
        net_income_result.delete(1.0,END)
        net_income_result.insert(1.0,calculated[1])

input.bind('<Return>',calculate) 
dropDown.pack()
income_label.pack()
input.pack() 
tax_label.pack()
output.pack() 
net_income_label.pack()
net_income_result.pack()
window.mainloop() 