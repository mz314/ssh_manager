import pygtk
import gtk
import gtk.glade

class application:
  me=None
  @staticmethod
  def getMe():
    if application.me==None:
      me=application()
    return me
  def __init__(self):
    self.gladefile="ui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.window = self.builder.get_object("mainwin")
    self.window.show()
    gtk.main()
  