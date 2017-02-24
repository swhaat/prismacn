import gi
import time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio#, GObject, Gdk

class FlowBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Control usuarios")
        self.set_border_width(2)
        self.set_default_size(800, 400)
        
        #self.notebook = Gtk.Notebook()
        #self.add(self.notebook)
        #grid = Gtk.Grid()
        #self.add(grid)
        

        header = Gtk.HeaderBar(title="Control de Usuarios")
        header.set_subtitle("Vista del controlador")
        header.props.show_close_button = True
        
        self.set_titlebar(header)
        
        button = Gtk.Button()
        button.connect("clicked", self.on_info_clicked)
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)

        header.pack_start(button)

        self.scrolled = Gtk.ScrolledWindow()
        self.scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(20)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
        
        #self.notebook.append_page(flowbox, Gtk.Label('Usuarios'))

        self.create_flowbox(flowbox)
        self.scrolled.add(flowbox)
        self.add(self.scrolled)
        
        
        
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        
        row = Gtk.Label("Automatic Date & Time")
        self.listbox.add(row)
        
        ''' 
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)       
        self.box.pack_start(self.listbox, True, True, 0)
        self.box.pack_start(self.scrolled, True, True, 0)
        
        self.notebook.append_page(self.box, Gtk.Label('Usuarios'))
        #self.notebook.append_page(self.scrolled, Gtk.Label('Usuarios'))
        
        #self.add(self.scrolled)Gtk.ButtonsType.OK, 
        
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)        
        self.page1.set_border_width(5)
        self.page1.add(Gtk.Label('Default Page!'))
        
        self.button = Gtk.ToggleButton.new_with_label("do stuff")
        self.button.connect("clicked", self.on_activity_mode_toggled)
        self.page1.add(self.button)
        self.notebook.append_page(self.page1, Gtk.Label('Mantenimiento'))
        '''
        

        
        
        self.show_all()

    
    def on_activity_mode_toggled(self, button):## mount iso to do PXE boot
        self.activity_mode = self.button.get_active()
        if self.activity_mode:
            print("button do stuff ON clicked")
            #self.progressbar.pulse()
        else:
            print("button do stuff OFF clicked")
            #self.progressbar.set_fraction(0.0)
            #self.progressbar.get_show_text()
    
    def on_info_clicked(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "This is an INFO MessageDialog")
        dialog.format_secondary_text(
            "And this is the secondary text that explains things.")
        dialog.run()
        
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(20)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.create_flowbox(flowbox)
        self.scrolled.add(flowbox)
        self.show_all()
        time.sleep(1.5)
        print("INFO dialog closed")
        

        dialog.destroy()
    
    def color_swatch_new(self, str_color):
        #color = Gdk.color_parse(str_color)

        #rgba = Gdk.RGBA.from_color(color)
        #button = Gtk.Button()
        
        grid = Gtk.Grid()
        label = Gtk.Label()
        label.set_text(str_color)
        switch = Gtk.Switch()
        switch.set_active(False)
        switch.set_tooltip_text(str_color)
        switch.connect("notify::active", self.on_switch_activated)
        switch.set_active(False)
        
        button1 = Gtk.Label("00:00:00  $ Pesos")
        #print(Gtk.Buildable.get_name(button1))
        button1.set_name(str_color)
        #button2 = Gtk.ToggleButton("Conectar")
        
        grid.add(label)
        grid.attach_next_to(switch, label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button1, switch, Gtk.PositionType.BOTTOM, 1, 3)
        #grid.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 1, 4)
        '''

        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.override_background_color(0, rgba)

        button.add(area)
        '''

        return grid

    def on_switch_activated(self, switch, gparam):
        
        if switch.get_active():
            state = "on"
            self.dictMe = {'Name': switch.get_tooltip_text(),
                           'startTime': time.time()}
            #print("Switch was turned", state, switch.get_tooltip_text())
        else:
            state = "off"
            self.dictMe['endTime'] = time.time()
            diff = int(self.dictMe['endTime']- self.dictMe['startTime'])
            minutes, seconds = diff // 60, diff % 60
            tot = str(minutes) + ':' + str(seconds).zfill(2)
            #label = Gtk.Label("Switch was turned")
            #self.listbox.add(label)
            price = self.calPrice(minutes)
            messageClient = ("Cliente en \n"+
                            switch.get_tooltip_text() +"\n"+
                            str(tot) +"\n"+ 
                            str(price))
            
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, 
                            messageClient)
            #dialog.format_secondary_text("And this is the secondary text that explains things.")
            dialog.run()
            dialog.destroy()
            #print("Switch was turned", state, switch.get_tooltip_text(), tot, price)
    
    def create_flowbox(self, flowbox):
        colors = [
        'AliceBlue',
        'AntiqueWhite',
        'AntiqueWhite1',
        'AntiqueWhite2',
        'AntiqueWhite3',
        'AntiqueWhite4',
        'aqua',
        'aquamarine',
        'aquamarine1',
        'aquamarine2',
        'aquamarine3',
        'aquamarine4',
        'azure',
        'azure1',
        'azure2',
        'azure3',
        'azure4',
        'beige',
        'bisque',
        'bisque1',
        'bisque2',
        'bisque3',
        'bisque4',
        'black',
        'BlanchedAlmond',
        'blue',
        'blue1',
        'blue2',
        'blue3',
        'blue4',
        'BlueViolet',
        'brown',
        'brown1',
        'brown2',
        'brown3',
        'brown4',
        'burlywood',
        'burlywood1',
        'burlywood2',
        'burlywood3',
        'burlywood4',
        'CadetBlue',
        'CadetBlue1',
        'CadetBlue2',
        'CadetBlue3',
        'CadetBlue4',
        'chartreuse',
        'chartreuse1',
        'chartreuse2',
        'chartreuse3',
        'chartreuse4',
        'chocolate',
        'chocolate1',
        'chocolate2',
        'chocolate3',
        'chocolate4',
        'coral',
        'coral1',
        'coral2',
        'coral3',
        'coral4'
        ]

        for color in colors:
            button = self.color_swatch_new(color)
            flowbox.add(button)
    
    def calPrice(self, minUser):
        if minUser >= 120:
            price = 2000
        elif minUser >= 80 and minUser <= 120:
            price = 1500
        elif minUser >= 60 and minUser <= 80:
            price = 1250
        elif minUser >= 30 and minUser <= 60:
            price = 1000
        elif minUser >= 15 and minUser <= 30:
            price = 700
        elif minUser >= 5 and minUser <= 15:
            price = 500
        elif minUser >= 1 and minUser <= 5:
            price = 250
        elif minUser <= 1:
            price = 250
        else:
            price = 0
        
        return price
        


builder = Gtk.Builder()
win = FlowBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
