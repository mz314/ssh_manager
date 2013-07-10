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
    self.gladexml=gtk.glade.XML("ui.glade")
    gtk.main()
  