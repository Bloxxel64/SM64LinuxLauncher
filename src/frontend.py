import sys
import os

from backend import compiler

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

window = tk.Tk()
window.title("SM64LinuxLauncher")
tk.Button(window, text="Press Me").grid(column=1, row=1)

window.mainloop()