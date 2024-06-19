import subprocess


def func_install_deps(packageManager):
    if packageManager == "apt":
        output = subprocess.Popen(['sudo', '/usr/bin/apt', 'install', 'libsdl2-dev', 'gcc-mips-linux-gnu make'])
        return output
