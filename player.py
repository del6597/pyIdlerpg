class player:
  def __init__(self, name, passwd, role):
    self.name = name
    self.passwd = passwd
    self.role = role
    self.items = [0,0,0,0,0,0,0,0,0,0]
    self.idletime = 0
    self.level = 0
    self.ttl = 600
    