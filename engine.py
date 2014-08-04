import getpass
import hashlib
import json
import math
import os.path
from player import *
import random
import threading
from time import sleep

players = []
paused = False
stopped = False
clock = threading.Barrier(2)

def pause():
    global paused
    paused = True

def unpause():
    global paused
    paused = False
    clock.wait()

def stop():
    global stopped
    stopped = True

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
    clazz = input("- Enter the class for this character: ")
    pwd = hashlib.sha512(getpass.getpass("- Finally, enter a password: ").encode()).hexdigest()
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
    try:
        fin = open("irpg.json", "r")
        for player in json.loads(fin.read()):
            p = Player()
            p.__dict__ = player
            addPlayer(p)
        return True
    except:
        print("*** DB is corrupt or non-existant ***")
        return False

def addPlayer(*args):
    for p in args:
        if isinstance(p, Player):
            if p not in players:
                # We only want to add unique player names
                players.append(p)
    save_players()

def removePlayer(p):
    if p in players:
        players.remove(p)
        save_players()
        return True
    return False

def getPlayer(name):
    p = Player()
    p.name = str(name)
    return players[players.index(p)]

def encodePlayers():
    return json.dumps(players, cls=PlayerJSONEncoder)

def decodePlayer(p):
    player = Player()
    player.__dict__ = json.loads(p)
    return player

def levelUp(p):
    p.level += 1
    p.ttl = math.floor(600 * (1.16**p.level))
#   TODO: Give them a new item
    item = random.randint(0,len(p.items))
    new_item = 1
    for i in range(1,int(p.level*1.5)):
        if random.uniform(0,1.4**(i/4))<1: # Should properly emulate the PERL version now
            new_item = i
    if new_item > p.items[item]:
        p.items[item] = new_item
#   TODO: Make them fight an opponent

def start(tick):
    if not load_players():
        return False
    while not stopped:
        # Play the game
        if paused:
            # Wait on our barrier
            # It's important that the other party waits on this barrier too 
            # so we get released here
            clock.wait()
        for p in [i for i in players if i.online]:
            p.ttl -= tick
            p.idled += tick
            if p.ttl <= 0:
                levelUp(p)
                print(str(p.name) + " the " + str(p.clazz) + " is now level " + str(p.level) + "! Next level in " + str(p.ttl))
                save_players()
        sleep(tick)
