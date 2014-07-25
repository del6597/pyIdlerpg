import json
from player import *

players = []

def start(self):
    pass

def stop(self):
    pass

def pause(self):
    pass

def addPlayer(p):
    if isinstance(p, Player):
        players.append(p)
        return True
    return False

def encodePlayers():
    return json.dumps(players, cls=PlayerJSONEncoder)
