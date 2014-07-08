import GameEngine
import json
from player import Player
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket

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
    GameEngine.addPlayer(stiny)
    GameEngine.addPlayer(goojoo)
    return GameEngine.encodePlayers()

if __name__ == "__main__":
    main()
