import sys
import os

from backend import compiler

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def startbuilding(destroywindow):
    destroywindow.destroy()
    cwindow = tk.Tk()
    cwindow.title("Compile and Install")
    tk.Button(cwindow, text="Dies", command=cwindow.destroy).grid(column=1, row=1)

    cwindow.mainloop()