from flask import Flask
from flask import jsonify

app = Flask(__name__)
import handler.eventsHandler as handler


@app.route("/api/events")
def getEvent():
    return jsonify(handler.getEvents())
