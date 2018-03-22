import os

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello Worlds'


if __name__ == '__main__':
    host = os.getenv("IP", "0.0.0.0")
    port = int(os.getenv("PORT", 3000))
    app.run(host=host, port=port)