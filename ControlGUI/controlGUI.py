import gi
import os
import time
from time import localtime, strftime
from gi.repository import GObject as gobject
os.chdir("/home/sergio/Downloads/ControlGUI/")

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib




class Handler:
    def salButton(self, *args):
        Gtk.main_quit(*args)

    def ayuButton(self, MenuItem):
        builder.get_object('usr1text').set_text('testMe')
        print("Hello World! ")
    
    def sw1(self, ToggleButton):
        builder.get_object('usr5text').set_text('00:00')
        if self.builder.get_object('usr2button').get_active():
            state = "on"
            self.start = time.time()
            self.builder.get_object('usr1text').set_text('00:00:00')
            #print(self.start)
        else:
            state = "off"
            end = time.time()
            diff = int(end - self.start)
            minutes, seconds = diff // 60, diff % 60
            tot = str(minutes) + ':' + str(seconds).zfill(2)
            self.builder.get_object('usr1text').set_text(tot)
			#print("Button was turned", state)

def countUseTime(self, start):
	timeNow = time.time() - start
	builder.get_object('usr1text').set_text('test2')
	
        
  
builder = Gtk.Builder()
builder.add_from_file('controlGUI.glade')
builder.connect_signals(Handler())
builder.get_object('usr1text').set_text('test2')
window = builder.get_object("main_window")
window.show_all()
Gtk.main()
