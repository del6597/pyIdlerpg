import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open("index.html", 'r') as fin:
            self.write(fin.read())
        #self.write("Hello, world")

application = tornado.web.Application([(r"/", MainHandler),])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()
