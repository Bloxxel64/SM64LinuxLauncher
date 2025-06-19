import sys
import os

from backend import compiler
from backend import confighandler as cfg

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

def reposelectmenu(destroywindow):
    if destroywindow: destroywindow.destroy()
    cwindow = tk.Tk()

def showRomMenuIfNeeded(destroywindow):
    destroywindow.destroy()
    if cfg.checkforrom():
        cwindow = tk.Tk()
        reposelectmenu(cwindow)
    else:
        cwindow = tk.Tk()
        cwindow.title("Compile and Install")
        tk.Button(cwindow, text="Give ROM now you twink", command=lambda : reposelectmenu(cwindow)).grid(column=1, row=1)

        cwindow.mainloop()
        

def backtomain(destroywindow):
    destroywindow.destroy()
    import main

def startbuilding(destroywindow):
    destroywindow.destroy()
    cwindow = tk.Tk()
    cwindow.title("Compile and Install")
    tk.Label(text="Welcome to the Guided Builder!\nThis will simplify the process of compiling and installing any version of SM64PC.").grid(column=0, row=0)
    tk.Button(cwindow, text="Continue", command=lambda : showRomMenuIfNeeded(cwindow)).grid(column=0, row=1)
    tk.Button(cwindow, text="Exit", command=lambda : backtomain(cwindow)).grid(column=1, row=1)

    cwindow.mainloop()