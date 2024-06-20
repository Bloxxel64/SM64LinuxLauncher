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
        button = Gtk.Button.new_with_label("Push Me!")
        button.connect('clicked', lambda x: compiler.func_clone_repo("https://github.com/coop-deluxe/sm64coopdx", os.path.expanduser('~') + "/gexcoop"))
        window.set_child(button)
        window.present()


app = LauncherWindow()
exit_status = app.run(sys.argv)
sys.exit(exit_status)