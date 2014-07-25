import json
from player import *

players = []
paused = False

def start():
    while (not paused):
        # Play the game
        pass

def stop():
    pass

def pause():
    paused = True

def unpause():
    paused = False

def addPlayer(p):
    if isinstance(p, Player):
        players.append(p)
        return True
    return False

def encodePlayers():
    return json.dumps(players, cls=PlayerJSONEncoder)
