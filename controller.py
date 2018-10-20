from flask import Flask, jsonify, request
from handler.database import db_session
from handler.database import init_db
import json

init_db()

app = Flask(__name__)
import handler.events as handler


@app.route("/api/events")
def getEvent():
    return jsonify(handler.getEvents())


@app.route("/api/subscribe")
def subsribe():
    email = request.args['email']
    handler.subscribe(email)
    return "OK"


@app.route("/api/user")
def getAllUsers():
    return jsonify(handler.getAllUsers())


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
