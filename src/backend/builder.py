from subprocess import call
from pathlib import Path
from backend.confighandler import checkforrom

import tkinter as tk

def cloneandcompilebinaries(name, link, branch, destroywindow, instancename):
    if destroywindow: destroywindow.destroy()

    if instancename == "":
        foldername = name
    else:
        foldername = instancename.strip("\n")

    foldername = foldername.replace(" ", "\ ")

    print(foldername)

    putithere = Path(Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name)
    if not putithere.is_dir():
        call("mkdir -p " " ~/.local/share/sm64linuxlauncher/cache/" + name, shell=True)

    call("git clone " + link + " -b " + branch + " " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name, shell=True)

    if checkforrom() == "us":
        call("cp " + Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.us.z64 " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name, shell=True)
    elif checkforrom() == "jp":
        call("cp " + Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.jp.z64 " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name, shell=True)
    elif checkforrom() == "eu":
        call("cp " + Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.eu.z64 " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name, shell=True)

    call("cd " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name + " && " + "make -j4", shell=True)

    call("cp -r " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name + "/build/us_pc " + Path.home()._str + "/.local/share/sm64linuxlauncher/instances/" + foldername, shell=True)

    call("cd " + Path.home()._str + "/.local/share/sm64linuxlauncher" + " && " + "rm cache -rf",shell=True)


def downloadandinstallbinaries(name, desktoplink, steamoslink, issteamdeck, destroywindow, instancename):
    if destroywindow: destroywindow.destroy()

    print(instancename)

    if instancename == "":
        foldername = name
    else:
        foldername = instancename

    foldername = foldername.replace(" ", "\ ")

    putithere = Path(Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name)
    if not putithere.is_dir():
        call("mkdir -p " " ~/.local/share/sm64linuxlauncher/cache/" + name, shell=True)

    if issteamdeck:
        call("cd " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name + " && " + "wget " + steamoslink + " " + "-O binary.zip", shell=True)
    else:
        call("cd " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name + " && " + "wget " + desktoplink + " " + "-O binary.zip", shell=True)
        

    call("cd " + Path.home()._str + "/.local/share/sm64linuxlauncher/cache/" + name + " && " + "mkdir -p " + "~/.local/share/sm64linuxlauncher/instances/" + foldername + " && " + "unzip binary.zip -d " + Path.home()._str + "/.local/share/sm64linuxlauncher/instances/" + foldername, shell=True)

    call("cd " + Path.home()._str + "/.local/share/sm64linuxlauncher" + " && " + "rm cache -rf",shell=True)
