#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text: str):
    """display “C ” followed by the value of the text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def py_text(text='is cool'):
    """display “Python ” followed by the value of the text"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)