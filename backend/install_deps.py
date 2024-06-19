import subprocess

aptCmd = '/usr/bin/apt install libsdl2-dev gcc-mips-linux-gnu make build-essential'


def func_install_deps(packageManager, password):
    if packageManager == "apt":
        output = subprocess.call('echo {} | sudo -S {}'.format(password, aptCmd), shell=True)
        return output
