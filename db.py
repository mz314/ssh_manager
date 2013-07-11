import sqlite3 as sql

#TODO mysql i podlaczyc do serka

class database:
  def __init__(self):
    self.conn=sql.connect("db.db")
    self.cur=self.conn.cursor()
  
  def loadSsh(self):
    query="select * from ssh"
    self.cur.execute(query)
    data=self.cur.fetchall()
    return data
  
  def __del__(self): 
    self.conn.close()