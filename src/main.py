'''
Created on 24/09/2013

@author: Melon
'''
from gi.repository import Gtk

def gui():

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        names = ["hola","adios","cosa"]
        for name in names:
            self.button = Gtk.Button(label=name)
            self.button.connect("clicked", self.on_button_clicked)
            self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

if __name__ == '__main__':
    pass