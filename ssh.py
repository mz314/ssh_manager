import os
import libssh2
import socket

class sshClass:
  def command(self,cmd):
    self.channel.execute(cmd)
    print self.channel.read(1024) #beware of the limit
    return False
  
  def setData(self,data):
    self.data=data
  
  def connect(self):
    un,pw,host=self.data
    print "Connection to"
    print un+"@"+host
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((host, 22))
    session = libssh2.Session()
    session.startup(self.sock)
    session.userauth_password(un, pw)
    self.channel = session.open_session()
   
  def disconnect(self):
     print "Disconnecting"
     self.sock.close()
    
    