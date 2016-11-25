from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)
redis = Redis(host="redis")

@app.route("/")
def hello():
    visits = redis.incr('counter');
    hostname = socket.gethostname();
    html = "<html><head><title>Hello Page</title></head><body>\nHello World!\n<br>" \
    + "I have seen {times} times.\n<br>I am from {host}\n</body></html>"
    sub = {'times':visits, 'host':hostname};
    return html.format(**sub)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
