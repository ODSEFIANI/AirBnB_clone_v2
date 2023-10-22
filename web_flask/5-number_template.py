#!/usr/bin/python3
""" module pydocumentation """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def pydocumentation """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def pydocumentation """
    return "HBNB"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ def doc """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ def pydocumentation """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ def pydocumentation """
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
