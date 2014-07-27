import hashlib
import json
import os.path
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

def create_db():
    print("*** Could not find the \'irpg.db\' file ***")
    print("==> Initializing DB.",end="")
    fout = open("irpg.json", 'a')
    print(".",end="")
    fout.close()
    print(".done\n")
    name = input("- Enter a new name for an admin character: ")
    clazz = input("- Enter the class for said character: ")
    pwd = hashlib.sha512(input("- Finally, enter a password: ").encode()).hexdigest()
    admin = Player()
    admin.name = name
    admin.clazz = clazz
    admin.passwd = pwd
    admin.admin = True
    addPlayer(admin)
    save_players()

def load_players():
    if not os.path.isfile("irpg.json"):
        create_db()
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
