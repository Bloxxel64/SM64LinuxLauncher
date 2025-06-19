print("\nHello! This is the terminal debug executible!\n"
      "This can be used for testing various aspects of the launcher, and should only be used for such.\n")

import os

import install_deps
import compiler
import confighandler


def main():
    cmd = input("Please enter a command (e.g. 'help', 'install-depends', etc.): ")

    if cmd == "help":
        print("List of available commands:\n"
            "help (duh),\n"
            "install-depends,\n"
            "clone-repo\n"
            "checkrom\n")
        main()

    if cmd == "install-depends":
        pkgmgr = input("\nApt or Pacman?: ")
        password = input("\nPlease enter your sudo password, as the following command requires superuser privileges: ")
        output = install_deps.func_install_deps(pkgmgr, password)
        print(output)
        main()

    if cmd == "clone-repo":
        output = compiler.func_clone_repo("https://github.com/coop-deluxe/sm64coopdx", os.path.expanduser('~') + "/gexcoop")
        print(main)
        main()

    if cmd == "checkrom":
        output = confighandler.checkforrom()
        print(output)
        main()

main()