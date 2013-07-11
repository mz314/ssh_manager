import pygtk
import gtk
import gtk.glade
from db import *

class application:
  me=None
  @staticmethod
  def getMe():
    if application.me==None:
      me=application()
    return me
  
  def dataInit(self):
    self.db=database()
    self.ssh_data=self.db.loadSsh()
  
  def fillModels(self):
    for i in self.ssh_data:
      print i
      self.sshList.append((i[3],i[0]))
  
  def __init__(self):
    self.dataInit()
    self.gladefile="ui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.window = self.builder.get_object("mainwin")
    self.sshList=self.builder.get_object("sshList")
    self.fillModels()
    self.window.show()
    gtk.main()
  