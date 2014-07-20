import json
import time

class PlayerJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return {"Name": obj.name, "Idled": obj.idled, "TTL": obj.ttl}
        return json.JSONEncoder.default(self, obj)

class Player():

  def __init__(self):
    self.name = ""
    self.passwd = ""
    self.admin = 0
    self.role = ""
    self.items = [0,0,0,0,0,0,0,0,0,0]
    self.idletime = 0
    self.level = 0
    self.ttl = 0
    self.create = time.time()
    self.last_login = time.time()
    self.align = 0
    self.idled = 0
    self.uhost = ""
    self.online = 0
    self.xpos = 0
    self.ypos = 0
    self.penalties = [0, 0, 0, 0, 0, 0, 0]
