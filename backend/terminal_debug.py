print("Hello! This is the terminal debug executible!\n"
      "This can be used for testing various aspects of the launcher, and should only be used for such.")

import install_deps

cmd = input("Please enter a command (e.g. 'help', 'install-depends', etc.): ")

if cmd == "help":
    print("List of available commands:\n"
          "'help' (duh),\n"
          "install-depends")

if cmd == "install-depends":
    output = install_deps.func_install_deps("apt")
    print(output)