#!/usr/bin/python3
""" Flask web application that handles different routes"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():


    """Returns a simple greeting message."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():


    """Returns 'HBNB' when visiting /hbnb."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):


    """Returns 'C' followed by the given text."""
    return "C " + text.replace("_", " ")

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):


    return "Python " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
