import sys
import os

from backend import compiler

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

class LauncherWindow(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.bloxxel64.SM64LinuxLauncher")
        GLib.set_application_name('SM64LinuxLauncher')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="SM64LinuxLauncher")
        windowAspect = Gtk.AspectFrame.new(0, 0, 2, False)
        window.set_child(windowAspect)
        menutabs = Gtk.Notebook.new()
        windowAspect.set_child(menutabs)
        popupwindow = Gtk.Window.new()


        playmenu = Gtk.Grid.new()


        compilemenu = Gtk.Grid.new()

        compilemenu.attach(Gtk.Label.new("Choose a repo:"), 1, 1, 1, 1)
        repolist = Gtk.DropDown.new_from_strings(["sm64coopdx", "sm64ex"])
        compilemenu.attach(repolist, 1, 2, 1, 1)

        compilemenu.attach(Gtk.Label.new("Install Folder (Click to Change):"), 1, 3, 1, 1)
        installpathinput = Gtk.Text.new()
        compilemenu.attach(installpathinput, 1, 4, 1, 1)

        def func_get_install_path():
            installpath = installpathinput.get_buffer()
            compiler.func_clone_repo("https://github.com/coop-deluxe/sm64coopdx", installpath.get_text())
            popupwindow.present()

        compilebutton = Gtk.Button.new_with_label("Build!")
        compilebutton.connect('clicked', lambda x: func_get_install_path())
        compilemenu.attach(compilebutton, 1, 5, 1, 1)


        settingsmenu = Gtk.Grid.new()

        menutabs.append_page(playmenu, Gtk.Label.new("Play"))
        menutabs.append_page(compilemenu, Gtk.Label.new("Build"))
        menutabs.append_page(settingsmenu, Gtk.Label.new("Settings"))

        window.present()
        window.maximize()

app = LauncherWindow()
exit_status = app.run(sys.argv)
sys.exit(exit_status)