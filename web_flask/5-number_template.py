#!/usr/bin/python3

"""
Flask web application that handles different routes with dynamic parameters.
Yeah, we're making the web talk!
"""

from flask import Flask, render_template

# Creating the Flask app instance
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a simple greeting message."""
    return "Hello HBNB!"  # Our first Flask route

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' when visiting /hbnb."""
    return "HBNB"  # Another route

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C' followed by the given text, with underscores replaced by spaces."""
    return "C " + text.replace("_", " ")  # Dynamic route

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Returns 'Python' followed by the given text, with underscores replaced by spaces.
    If no text is provided, defaults to 'is cool'.
    """
    return "Python " + text.replace("_", " ")


