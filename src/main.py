import sys
import os


import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from pathlib import Path
from subprocess import call

from frontend import compilemenu as cm

#make the directory for the launcher
basedir = Path("~/.local/share/sm64linuxlauncher")
if not basedir.is_dir():
    call("mkdir" " ~/.local/share/sm64linuxlauncher", shell=True)

#main window
window = tk.Tk()
window.title("SM64LinuxLauncher")
playbutton = tk.Button(window, text="Play", command=lambda : cm.startbuilding(window)).grid(column=0, row=0)
buildbutton = tk.Button(window, text="Build and Install", command=lambda : cm.startbuilding(window)).grid(column=1, row=1)

window.mainloop()
