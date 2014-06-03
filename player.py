class player:
  def __init__(self, name, passwd, role, ttl):
    self.name = name
    self.passwd = passwd
    self.admin = 0
    self.role = role
    self.items = [0,0,0,0,0,0,0,0,0,0]
    self.idletime = 0
    self.level = 0
    self.ttl = ttl
    self.create = time.time()
    self.last_login = time.time()
    self.align = 0
    self.idled = 0
    self.uhost = ""
    self.online = 0
    self.xpos = 0
    self.ypos = 0
    self.penalties = [0, 0, 0, 0, 0, 0, 0]