class sshWindow:
  def delete_event(self, widget, event, data=None):
    return False
  def destroy(self, widget, data=None):
    #self.window.hide() #WARNING
    return False
  def __init__(self,builder):
    self.builder=builder
    self.window=builder.get_object('sshWindow')
    builder.connect_signals(self)
  def __del__(self):
    pass
  def show(self):
    self.window.show()