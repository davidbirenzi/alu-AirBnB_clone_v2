#!/usr/bin/python3
"""Module for flask app with routes"""


from flask import Flask, render_template
"""Importing the Flask class from the flask module"""

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
    return f"C {text.replace('_', ' ')}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Returns 'Python' followed by the given text, with underscores replaced by spaces."""
    return f"Python {text.replace('_', ' ')}"

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Returns 'n is a number' only if n is an integer."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('6-number_odd_or_even.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)

if __name__ == "__main__":
    """Running the app on all available IPs (0.0.0.0) and port 5000"""
    app.run(host="0.0.0.0", port=5000)
