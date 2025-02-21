#!/usr/bin/python3
"""
Flask web application that handles different routes with dynamic parameters
"""
from flask import Flask

# Creating the Flask app instance
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a simple greeting message."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' when visiting /hbnb."""
    return "HBNB"


