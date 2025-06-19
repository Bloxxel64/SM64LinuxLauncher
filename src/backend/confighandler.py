import configparser as cfgp
from pathlib import Path

def checkforrom():
    usromfile = Path(Path.home()._str + "/.local/share/sm64linuxlauncher/baserom.us.z64")
    if usromfile.is_file():
        return True
    else:
        return False