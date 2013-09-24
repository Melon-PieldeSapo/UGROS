'''
Created on 24/09/2013

@author: Melon
'''
from gi.repository import Gtk

class gui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="UGROS")
        
        #Gtk.Settings.set_string_property(gtk-button-images)
        #gtk-button-images
      
        names = ["hola","adios","cosa","cosa fea","otra cosa","bieeen"]
        img = Gtk.Image.new_from_file('../res/ugr_logo.jpg')
        #self.box=Gtk.Box(spacing=6)
        #self.add(self.box)
        self.table=Gtk.Table(2,3,True)
        self.add(self.table)
        i=0
        j=0
        for name in names:
            button = Gtk.Button(label=name)
            button.connect("clicked", self.on_button_clicked)
            Gtk.gtk_button_set_image(button,img)
            # button.set_image(img)
            #self.box.pack_start(self.button, True, True, 0)
            self.table.attach(button,i,i+1,j,j+1)
            i=i+1
            if(i%2==0):
                j=j+1
                i=0
    def on_button_clicked(self, widget):
        print("Hello World")
        print (widget)

if __name__ == '__main__':
    win = gui()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()