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

if __name__ == "__main__":
    # Running the app on all available IPs (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)  

