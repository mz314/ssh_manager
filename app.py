import pygtk
import gtk
import gtk.glade
from db import *
from ssh import *

class application:
  #signal handlers#
  
  def delete_event(self, widget, event, data=None):
    return False
  
  def destroy(self, widget, data=None):
    gtk.main_quit()
  
  #regular functions
  
  def connectSsh(self, widget, data=None):
    sshc=sshClass();
    sshc.connect('a','b','c')
  
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
      self.sshList.append((i[4],i[0]))
  
  def connectSigs(self):
    self.builder.connect_signals(self)
  
  def __init__(self):
    self.dataInit()
    self.gladefile="ui.glade"
    self.builder = gtk.Builder()
    self.builder.add_from_file(self.gladefile)
    self.window = self.builder.get_object("mainwin")
    self.sshList=self.builder.get_object("sshList")
    self.connectSigs()
    self.fillModels()
    self.window.show()
    gtk.main()
  