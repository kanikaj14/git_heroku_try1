import __future__
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ("bla bla bla bla!")

if __name__ == "__main__":
    app.run()