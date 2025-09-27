import json
from pathlib import Path
from subprocess import call

def checkforrom():
    usromfile = Path(Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.us.z64")
    jpromfile = Path(Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.jp.z64")
    euromfile = Path(Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.eu.z64")
    if usromfile.is_file():
        return "us"
    elif jpromfile.is_file():
        return "jp"
    elif euromfile.is_file():
        return "eu"
    else:
        return False

def copyrom(region, ROM):
    call("cp " + "'" + ROM + "'" + " " + Path.home()._str + "/.local/share/sm64linuxlauncher/baserom." + region + ".z64", shell=True)

def updaterepos():
    call("curl -o " + Path.home()._str + "/.local/share/sm64linuxlauncher/json/repos.json" + " " + "https://raw.githubusercontent.com/Bloxxel64/SM64LinuxLauncher/refs/heads/repo-json/repos.json", shell=True)
    rawjson = open(Path.home()._str + "/.local/share/sm64linuxlauncher/json/repos.json")
    return json.load(rawjson)