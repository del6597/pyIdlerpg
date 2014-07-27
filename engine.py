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
    fin = open("irpg.json", "r")
    for player in json.loads(fin.read()):
        p = Player()
        p.__dict__ = player
        addPlayer(p)

def start():
    load_players()
    while (not paused):
        # Play the game
        pass

def stop():
    pass

def addPlayer(*args):
    for p in args:
        if isinstance(p, Player):
            if p not in players:
                # We only want to add unique player names
                players.append(p)

def encodePlayers():
    return json.dumps(players, cls=PlayerJSONEncoder)

def decodePlayer(p):
    player = Player()
    player.__dict__ = json.loads(p)
    return player
