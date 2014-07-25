import json
from player import *

players = []
paused = False

def pause():
    paused = True

def unpause():
    paused = False

def save_players():
    fout = open("irpg.json", 'w')
    fout.write(encodePlayers())
    fout.close()

def load_players():
    pass

def start():
    while (not paused):
        # Play the game
        load_players()
        pass

def stop():
    pass

def addPlayer(p):
    if isinstance(p, Player):
        players.append(p)
        return True
    return False

def encodePlayers():
    return json.dumps(players, cls=PlayerJSONEncoder)
