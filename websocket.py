import tornado.ioloop
import tornado.web
import tornado.websocket
import json

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(request):
        request.render("index.html")

clients = [["Player 0", 100]]
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        global clients
        print("WebSocket opened for client " + str(len(clients)))
        clients.append(["Player " + str(len(clients)), 0])
        self.write_message(json.dumps(clients))

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

app = tornado.web.Application([(r'/', IndexHandler), (r'/echo', EchoWebSocket)])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
