'''
Created on 24/09/2013

@author: Melon
'''
from gi.repository import Gtk

class gui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="UGROS")
        names = ["hola","adios","cosa"]
        
        self.box=Gtk.Box(spacing=6)
        self.add(self.box)
        for name in names:
            self.button[name] = Gtk.Button(label=name)
            self.button[name].connect("clicked", self.on_button_clicked)
            self.box.pack_start(self.button[name], True, True, 0)

    def on_button_clicked(self, widget):
        print("Hello World")

if __name__ == '__main__':
    win = gui()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()