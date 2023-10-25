#!/usr/bin/python3
""" module documen """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ defenition doc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def documentation """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
