import os
import libssh2

class sshClass:
  def connect(self,un,pw,host):
    cmd='konsole --hold --noclose -e "sshpass -p '+pw+' ssh '+un+'@'+host+'" '
    print cmd
    