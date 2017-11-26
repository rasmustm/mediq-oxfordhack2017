from gevent.wsgi import WSGIServer
from app import app

http_server = WSGIServer(("localhost", 8080), app)
http_server.serve_forever()
