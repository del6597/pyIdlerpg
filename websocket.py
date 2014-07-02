import tornado.ioloop
import tornado.web
import tornado.websocket

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(request):
        request.render("index.html")

connections = 0
class EchoWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        global connections
        connections = connections + 1
        self.write_message(u"You said: " + message + " " + str(connections))

    def on_close(self):
        print("WebSocket closed")

app = tornado.web.Application([(r'/', IndexHandler), (r'/echo', EchoWebSocket)])

app.listen(8888)
tornado.ioloop.IOLoop.instance().start()
