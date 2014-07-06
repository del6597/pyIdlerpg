import json
from Player import *

players = []

def start(self):
    pass

def stop(self):
    pass

def pause(self):
    pass

def addPlayer(player):
    if isinstance(player, Player):
        players.append(player)
        return True
        return False

def encodePlayers():
    return json.dumps(players, cls=PlayerJsonEncoder)
