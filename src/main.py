'''
Created on 24/09/2013

@author: Melon
'''

from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf


class gui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="UGROS")
        
        #Gtk.Settings.set_string_property(gtk-button-images)
        #gtk-button-images
      
        names = ["hola","adios","cosa","cosa fea","otra cosa","bieeen"]
        #GtkWidget *img;
        pb = Pixbuf.new_from_file('../res/ugr_logo.jpg')
        #self.box=Gtk.Box(spacing=6)
        #self.add(self.box)
        #self.add(img)
        self.table=Gtk.Table(2,2,True)
        self.add(self.table)
        i=0
        j=0
        for name in names:        
            img = Gtk.Image()
            img.set_from_pixbuf(pb)
            box = Gtk.Box(spacing=6) 
            box.connect("button-press-event",self.on_img_click_event)
            box.pack_start(img,True,True,0)
            #button = Gtk.Button(label=name)
            #button.connect("clicked", self.on_button_clicked)
            #Gtk.gtk_button_set_image(button,img)
            #button.set_image(img)
            #button.set_image(img)
            #self.box.pack_start(self.button, True, True, 0)
            #box.pack_start(button,True,True,0)
            self.table.attach(box,i,i+1,j,j+1)
            i=i+1
            if(i%2==0):
                j=j+1
                i=0
    def on_img_click_event(self,widget):
        print("Hello IMG")
        print (widget)
    def on_button_clicked(self, widget):
        print("Hello World")
        print (widget)

if __name__ == '__main__':
    win = gui()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()