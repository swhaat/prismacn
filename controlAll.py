import gi
import time
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio#, Gdk

class FlowBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Control usuarios")
        self.set_border_width(2)
        self.set_default_size(400, 400)

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

        #self.create_flowbox(flowbox)

        #scrolled.add(flowbox)

        #self.add(self.scrolled)Gtk.ButtonsType.OK, 
        self.show_all()

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
        self.add(self.scrolled)
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
        button1 = Gtk.ToggleButton("Conectar")
        button2 = Gtk.Label("something")
        
        grid.add(label)
        grid.attach_next_to(switch, label, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button1, switch, Gtk.PositionType.BOTTOM, 1, 3)
        grid.attach_next_to(button2, button1, Gtk.PositionType.BOTTOM, 1, 4)
        '''

        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.override_background_color(0, rgba)

        button.add(area)
        '''

        return grid

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


win = FlowBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
