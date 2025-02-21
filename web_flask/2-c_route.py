#!/usr/bin/python3
"""
A simple Flask web application.
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
    return "HBNB"  # Another route, another win!

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C' followed by the given text, with underscores replaced by spaces."""
    return "C " + text.replace("_", " ")  # Dynamic route magic!
f __name__ == "__main__":
    # Running the app on all available IPs (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
