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

def addPlayer(*args):
    for p in args:
        if isinstance(p, Player):
            players.append(p)

def encodePlayers():
    return json.dumps(players, cls=PlayerJSONEncoder)

def decodePlayer(p):
    player = Player()
    player.__dict__ = json.loads(p)
    return player
