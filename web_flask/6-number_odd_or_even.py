#!/usr/bin/python3
# This script starts a Flask web application with multiple routes.
# It listens on 0.0.0.0, port 5000, and defines routes for '/', '/hbnb',
# '/c/<text>', '/python/(<text>)', '/number/<n>', '/number_template/<n>',
# and '/number_odd_or_even/<n>'.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return f"C {text.replace('_', ' ')}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return f"Python {text.replace('_', ' ')}"

@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('6-number_odd_or_even.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

