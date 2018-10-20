from flask import Flask, jsonify, request
from handler.database import db_session
from handler.database import init_db
import handler.events as eventHandler
import handler.user as userHandler

init_db()

app = Flask(__name__)


@app.route("/api/events")
def getEvent():
    return jsonify(eventHandler.getEvents())


@app.route("/api/subscribe")
def subsribe():
    email = request.args['email']
    userHandler.subscribe(email)
    return "OK"


@app.route("/api/user")
def getAllUsers():
    return jsonify(userHandler.getAllUsers())


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route("/data")
def data():
    data = spacelaunchnow_adapter.getItems()
    return jsonify(results=[d.serialize() for d in data])
