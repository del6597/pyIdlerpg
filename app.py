import engine
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

class StatsWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        global clients
        clients.append(self)
        # Send the client JSON stats of players here
        self.write_message(engine.encodePlayers())

    def broadcast(self, message):
        global clients
        for c in clients:
            c.write_message(message)

    def on_message(self, message):
        pass

    def on_close(self):
        global clients
        clients.remove(self)

def main():
    print("-~= Starting pyidlerpg =~-")
    stiny = Player()
    stiny.name = "Stiny"
    stiny.idled = 0
    stiny.ttl = 300
    goojoo = Player()
    goojoo.name = "Goojoo"
    goojoo.idled = 120
    goojoo.ttl = 600
    engine.addPlayer(stiny)
    engine.addPlayer(goojoo)

    # Start Tornado stuff here I guess
    print("Tornado Starting...")
    app = tornado.web.Application([(r'/', IndexHandler),(r'/irpg', StatsWebSocket)])
    app.listen(9999) # Random port for now I guess
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    clients = []
    main()
