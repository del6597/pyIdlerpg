import GameEngine
import json
from player import Player
import threading
import time
import tornado.ioloop
import tornado.web
import tornado.websocket

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(request):
        request.render("index.html")

open_sockets = []
class StatsWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        global open_sockets
        print("Websocket opened")
        # Send the client JSON stats of players here
        self.write_message(GameEngine.encodePlayers())
        # Add this socket to a list of connected sockets to pipe events to
        open_sockets.append(self)

    def on_close(self):
        # Remove this socket from the list of sockets
        global open_sockets
        open_sockets.remove(self)

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

    # Start Tornado stuff here I guess
    print("Tornado Starting...")
    app = tornado.web.Application([(r'/', IndexHandler),(r'/irpg', StatsWebSocket)])
    app.listen(9999) # Random port for now I guess
    tornado.ioloop.IOLoop.instance().start()
    print("Tornado Started")

    time.sleep(10)
    stiny.idled += 100
    global open_sockets
    for sock in open_sockets:
        sock.write_message(GameEngine.encodePlayers())

if __name__ == "__main__":
    main()
