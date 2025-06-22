import sys
import os

from backend import compiler
from backend import confighandler as cfg
from backend import hashcalc as md5

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *


def reposelectmenu():
    cwindow = tk.Tk()

def showRomMenuIfNeeded(destroywindow):
    if destroywindow: destroywindow.destroy()
    if cfg.checkforrom():
        reposelectmenu()
    else:
        popup = tk.Tk()
        tk.Label(text="No ROM detected in sm64ll's appdata folder. Please select your .z64 format Unmodified SM64 ROM.").grid(column=0, row=0)
        tk.ttk.Button(popup, text="OK", command=lambda : popup.destroy()).grid(column=0, row=1)

        popup.mainloop()

        selectfile = tk.filedialog.askopenfile(mode='r')
        if md5.checkromhash(selectfile.name):
            cfg.copyrom(md5.checkromhash(selectfile.name), selectfile.name)
            reposelectmenu()
        else:
            popup = tk.Tk()
            tk.Label(text="Invalid File. Please select your .z64 format Unmodified SM64 ROM.").grid(column=0, row=0)
            tk.ttk.Button(popup, text="OK", command=lambda : popup.destroy()).grid(column=0, row=1)

            popup.mainloop()

            showRomMenuIfNeeded(None)
        

def backtomain(destroywindow):
    destroywindow.destroy()
    import main

def startbuilding(destroywindow):
    destroywindow.destroy()
    cwindow = tk.Tk()
    cwindow.title("Compile and Install")
    tk.Label(text="Welcome to the Guided Builder!\nThis will simplify the process of compiling and installing any version of SM64PC.").grid(column=0, row=0)
    tk.ttk.Button(cwindow, text="Continue", command=lambda : showRomMenuIfNeeded(cwindow)).grid(column=0, row=1)
    tk.Button(cwindow, text="Exit", command=lambda : backtomain(cwindow)).grid(column=1, row=1)

    cwindow.mainloop()