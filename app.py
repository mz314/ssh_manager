import pygtk
import gtk
import gtk.glade

from db import *
from ssh import *
from sshwindow import *

class application:
  #signal handlers#
  
  def delete_event(self, widget, event, data=None):
    return False
  
  def destroy(self, widget, data=None):
    gtk.main_quit()
  
  #regular functions
  
  def getLoginById(self,id):
    found=None
    for i in self.ssh_data:
      if i[0]==id:
	found=i
	return found
    return found
  
  
  def connectSsh(self, widget, data=None):
    sshCombo=self.sshCombo
    model=sshCombo.get_model()
    item=model[sshCombo.get_active()]
    #print item[1]
    sshc=sshClass();
    data=self.getLoginById(item[1])
    #print data
    sshw=sshWindow(self.builder)
    sshw.show()
  
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
    self.sshCombo=self.builder.get_object('sshCombo')
    self.connectSigs()
    self.fillModels()
    self.window.show()
    gtk.main()
  