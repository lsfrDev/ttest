from threading import Thread
from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def home():
    return "Done"


def run():
    app.run(host="0.0.0.0", port=random.randint(2000, 9000))


Thread(target=run).start()
