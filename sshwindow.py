import gtk


class sshWindow:
  
  def keypress(self, widget, event):
    if event.keyval == gtk.keysyms.Return:
      print self.cmdbuffer
      ret=self.ssh.command(self.cmdbuffer)
      print ret
      self.cmdbuffer=""
    else:
      self.cmdbuffer=self.cmdbuffer+event.string
  
  def delete_event(self, widget, event, data=None):
    self.ssh.disconnect()
   
  def destroy(self, widget, data=None):
    #self.window.hide() #WARNING
    
    return False
  def __init__(self,builder,ssh):
    self.cmdbuffer=""
    self.builder=builder
    self.window=builder.get_object('sshWindow')
    self.cmdLine=builder.get_object('cmdLine')
    self.cmdLine.connect("key-press-event",self.keypress)
    self.ssh=ssh
    builder.connect_signals(self)
 
  def __del__(self):
    pass
  def show(self):
    self.ssh.connect()
    self.window.show()