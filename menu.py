#!/usr/bin/python

import subprocess
import pygtk
import gtk
import glib
import xdg.Menu
import xdg.DesktopEntry
import xdg.IconTheme


def create_menu(menu, depth = 0):
	def launch(widget, string):
		print "Running %s." % string
		#os.spawnlp(os.P_NOWAIT,string)
		gtk.main_quit()
		subprocess.Popen(string)

	def get_exec(string):
		return string.split()[0]

	def get_icon(iconname):
		if iconname.find('.')<>-1:
			try:
				pixbuf = gtk.gdk.pixbuf_new_from_file(xdg.IconTheme.getIconPath(iconname))
				ick = gtk.IconSet(pixbuf)
				scaled = ick.render_icon(gtk.Style(), gtk.TEXT_DIR_LTR, gtk.STATE_NORMAL, gtk.ICON_SIZE_LARGE_TOOLBAR, None, None)
				img = gtk.image_new_from_pixbuf(scaled)
			except (TypeError, glib.GError):
				img = gtk.image_new_from_stock(gtk.STOCK_MISSING_IMAGE, gtk.ICON_SIZE_LARGE_TOOLBAR)
		else:
			img = gtk.image_new_from_icon_name(iconname, gtk.ICON_SIZE_LARGE_TOOLBAR)
		return img

	themenu = gtk.Menu()
	for entry in menu.getEntries():
		if isinstance(entry, xdg.Menu.Menu):
			item = gtk.ImageMenuItem(stock_id=entry.getName())
			item.set_image(get_icon(entry.getIcon()))
			submenu = create_menu(entry, depth)
			item.set_submenu(submenu)
			themenu.append(item)
			item.set_tooltip_text(entry.getComment())
			item.show()
		elif isinstance(entry, xdg.Menu.MenuEntry):
			item = gtk.ImageMenuItem(entry.DesktopEntry.getName())
			item.set_image(get_icon(entry.DesktopEntry.getIcon()))
			item.connect("activate", launch, get_exec(entry.DesktopEntry.getExec()))
			themenu.append(item)
			item.set_tooltip_text(entry.DesktopEntry.getComment())
			item.show()
	themenu.show()
	return themenu


class MenuExample:
    def __init__(self):
#        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#        window.set_size_request(200, 100)
#        window.set_title("MadMenu")
#        window.connect("delete_event", lambda w,e: gtk.main_quit())

	mainmenu=create_menu(xdg.Menu.parse())
	mainmenu.popup(None, None, None, 0, 0)
#        root_menu = gtk.MenuItem("Root Menu")
#	root_menu.show()
#        root_menu.set_submenu(mainmenu) 
#	vbox = gtk.VBox(False, 0)
#        window.add(vbox)
#        vbox.show()
        # Create a menu-bar to hold the menus and add it to our main window
#        menu_bar = gtk.MenuBar()
#        vbox.pack_start(menu_bar, False, False, 2)
#        menu_bar.show()

        # Create a button to which to attach menu as a popup
#        button = gtk.Button("press me")
#        button.connect_object("event", self.button_press, mainmenu)
#        vbox.pack_end(button, True, True, 2)
#        button.show()

        # And finally we append the menu-item to the menu-bar -- this is the
        # "root" menu-item I have been raving about =)
 #       menu_bar.append(root_menu)

        # always display the window as the last step so it all splashes on
        # the screen at once.
 #       window.show()

    # Respond to a button-press by posting a menu passed in as widget.
    #
    # Note that the "widget" argument is the menu being posted, NOT
    # the button that was pressed.
#    def button_press(self, widget, event):
#        if event.type == gtk.gdk.BUTTON_PRESS:
#            widget.popup(None, None, None, event.button, event.time)
#            # Tell calling code that we have handled this event the buck
#            # stops here.
#            return True
#        # Tell calling code that we have not handled this event pass it on.
#        return False

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    MenuExample()
    main()
