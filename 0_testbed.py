from tkinter import *
from tkinter import ttk

def calculate(*args):
    """does a calculation"""
    pass

root = Tk()
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
button = ttk.Button(mainframe, text="Calculate", command=calculate)
button.grid(column=1, row=1, sticky=W)

root.mainloop()