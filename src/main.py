import sys
import os


import tkinter as tk
from tkinter import *
from tkinter.ttk import *

from frontend import compilemenu as cm

window = tk.Tk()
window.title("SM64LinuxLauncher")
playbutton = tk.Button(window, text="Play", command=lambda : cm.startbuilding(window)).grid(column=0, row=0)
buildbutton = tk.Button(window, text="Build and Install", command=lambda : cm.startbuilding(window)).grid(column=1, row=1)

window.mainloop()
