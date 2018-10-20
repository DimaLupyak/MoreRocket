from flask import Flask
from flask import jsonify
import spacelaunchnow_adapter 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World1!"

@app.route("/data")
def data():
    data = spacelaunchnow_adapter.getItems()
    return jsonify(results=[d.serialize() for d in data])