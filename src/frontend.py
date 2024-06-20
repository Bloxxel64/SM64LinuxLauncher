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

        playmenu = Gtk.Grid.new()

        compilemenu = Gtk.Grid.new()

        compilemenu.attach(Gtk.Label.new("Choose a repo:"), 1, 1, 1, 1)
        repolist = Gtk.DropDown.new_from_strings(["sm64coopdx", "sm64ex"])
        compilemenu.attach(repolist, 1, 2, 1, 1)

        settingsmenu = Gtk.Grid.new()

        menutabs.append_page(playmenu, Gtk.Label.new("Play"))
        menutabs.append_page(compilemenu, Gtk.Label.new("Build"))
        menutabs.append_page(settingsmenu, Gtk.Label.new("Settings"))

        #button.connect('clicked', lambda x: compiler.func_clone_repo("https://github.com/coop-deluxe/sm64coopdx", os.path.expanduser('~') + "/gexcoop"))
        window.present()
        window.maximize()

app = LauncherWindow()
exit_status = app.run(sys.argv)
sys.exit(exit_status)