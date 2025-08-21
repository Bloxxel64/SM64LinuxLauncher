from subprocess import call

aptCmd = ('/usr/bin/apt install -y libsdl2-dev gcc-mips-linux-gnu make build-essential python3-tk')

pacmanCmd = ('pacman -S sdl2_gfx sdl2_image sdl2_mixer sdl2_net git base-devel tk')


def func_install_deps(packageManager, password):
    if packageManager == "apt":
        output = subprocess.call('echo {} | sudo -S {}'.format(password, aptCmd), shell=True)
        return output

    if packageManager == "pacman":
        output = subprocess.call('echo {} | sudo -S {}'.format(password, pacmanCmd), shell=True)
        return output
