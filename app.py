from asyncio import run
from flask import Flask


app = Flask(__name__)

from controllers import controller

if __name__ == '__main__':
    app.run(debug=True)

#To run, create an (alias?) flask server:
# in terminal: export FLASK_APP=app.py
# flask run


#test end-points

@app.route('/')
def index():
    return "Hello World"

@app.route('/<name>')
def greet(name):
    return f"Hello {name}, how's it going?!"


