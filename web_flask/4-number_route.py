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

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Returns 'n is a number' only if n is an integer."""
    return f"{n} is a number"

if __name__ == "__main__":
    # Running the app on all available IPs (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
