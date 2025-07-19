import sys
import os

from backend import compiler
from backend import confighandler as cfg
from backend import hashcalc as md5
from backend import builder as bldr

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
#import json

listma = cfg.updaterepos()
def downloadbinaries(destroywindow, selectionnum, instancename):
    if destroywindow: destroywindow.destroy()

    print(instancename)
    
    cwindow = tk.Tk()
    tk.Label(cwindow, text="Linux (Desktop) or Steam Deck/SteamOS?", wraplength=350).grid()
  
    issteamdeck = BooleanVar(cwindow)

    tk.Radiobutton(cwindow, text="Linux/Desktop", value=False, variable=issteamdeck).grid()
    tk.Radiobutton(cwindow, text="Steam Deck/SteamOS", value=True, variable=issteamdeck).grid()
    tk.ttk.Button(cwindow, text="Yes", command=lambda : bldr.downloadandinstallbinaries(listma['repos'][selectionnum]['reponame'], listma['repos'][selectionnum]['binarylinklinux'], listma['repos'][selectionnum]['binarylinksteamdeck'], issteamdeck.get(), cwindow, instancename)).grid()



def repocontextmenus(destroywindow, dobinaryprompt, showpatchesmenu, selectionnum, instname):
    if destroywindow: destroywindow.destroy()

    instancename = instname.strip()

    if dobinaryprompt:
        cwindow = tk.Tk()
        tk.Label(cwindow, text="This Repo has precompiled binaries, allowing you to simply download them and get into the game. Do you want to use them or compile from source anyway? (This is mainly aimed at developers and people who want to use the most up-to-date source code.)", wraplength=350).grid()
        tk.ttk.Button(cwindow, text="Yes", command=lambda : downloadbinaries(cwindow, selectionnum, instancename)).grid()
        tk.ttk.Button(cwindow, text="No LOL", command=lambda : repocontextmenus(cwindow, False, showpatchesmenu)).grid()
    elif showpatchesmenu and not dobinaryprompt:
        #TODO: We need patches!
        bldr.cloneandcompilebinaries(listma['repos'][selectionnum]['reponame'], listma['repos'][selectionnum]['link'],listma['repos'][selectionnum]['branch'],None,instancename)
    else:
        bldr.cloneandcompilebinaries(listma['repos'][selectionnum]['reponame'], listma['repos'][selectionnum]['link'],listma['repos'][selectionnum]['branch'],None,instancename)
    

def reposelectmenu():
    listnames = []
    listdesc = []
    for i in listma['repos']:
        listnames.append(i['name'])
        listdesc.append(i['description'])

    
    cwindow = tk.Tk()
    tk.Label(cwindow, text="Instance Name:", wraplength=250, padx=10, pady=10).grid(column=0, row=0)
    namer = tk.Text(cwindow, height=1, width=20)
    namer.grid(row=0, column=1)
    itr = -1
    selectionnum = IntVar(cwindow)
    for n in listnames:
        itr = itr + 1
        tk.Radiobutton(cwindow, text=n, value=itr, variable=selectionnum).grid(column=0, row=itr + 1)
        tk.Label(cwindow, text=listdesc[itr], wraplength=250, padx=10, pady=10).grid(column=1, row=itr +1)
    tk.ttk.Button(cwindow, text="OK", command=lambda : repocontextmenus(cwindow, listma['repos'][selectionnum.get()]['hasbinaries'], listma['repos'][selectionnum.get()]['supportspatches'], selectionnum.get(), namer.get(index1 = 1.0, index2 = END))).grid(column=1, row=itr + 2)
    cwindow.mainloop()

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