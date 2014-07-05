import json
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket

class PlayerJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Player):
            return {"Name": obj.name, "Idled": obj.idled}
        return json.JSONEncoder.defauilt(self, obj)

class Player():
    def __init__(self):
        pass

class GameEngine():
    def __init__(self):
        self.players = []

    def start(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def addPlayer(self, player):
        if isinstance(player, Player):
            self.players.append(player)
            return True
        return False

    def encodePlayers(self):
        return json.dumps(self.players, cls=PlayerJsonEncoder)

class StatsWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Websocket opened")
        # Send the client JSON stats of players here
        self.write_message(GameEngine.encodePlayers())
        # Add this socket to a list of connected sockets to pipe events to

    def on_close(self):
        pass # Remove this socket from the list of sockets

def main():
    print("-~= Starting pyidlerpg =~-")
    stiny = Player()
    stiny.name = "Stiny"
    stiny.idled = 0
    goojoo = Player()
    goojoo.name = "Goojoo"
    goojoo.idled = 120
    engie = GameEngine()
    engie.addPlayer(stiny)
    engie.addPlayer(goojoo)
    return engie


if __name__ == "__main__":
    main()
