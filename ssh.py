import os
import libssh2
import socket
import sys

class sshClass:
  def __init__(self):
      self.conn=False
      
  def read(self):
    ret=self.channel.read(10024)
    ret=ret+self.channel.read(10024)
    return ret
    #else:
    #  return ""
  
  def command(self,cmd):
    #print self.channel
    self.channel.write(cmd+"\n")
    #data_to_disp = self.channel.poll_read(1)
    #print "XX",data_to_disp
    #if data_to_disp > 0:
    
  
  def setData(self,data):
    self.data=data
  
  def connect(self):
    un,pw,host=self.data
    print "Connection to"
    print un+"@"+host
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((host, 22))
    self.sock.setblocking(1)
    self.session = libssh2.Session()
    self.session.startup(self.sock)
    self.session.set_banner()
    self.session.userauth_password(un, pw)
    self.channel = self.session.open_session()
    self.channel.pty('vt100')
    self.channel.shell()
    self.channel.setblocking(1)
    self.conn=True
    
  def disconnect(self):
     print "Disconnecting"
     self.sock.close()
     self.conn=False
     
    
    