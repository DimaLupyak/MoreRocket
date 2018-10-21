from flask import Flask, jsonify, request
from morerockets.handler.database import init_db
from morerockets.handler import mail as mailHandler, events as eventHandler, user as userHandler
from morerockets import app
application = app
init_db()


@app.route("/api/events")
def getEvent():
    return jsonify(eventHandler.getDbEvents())


@app.route("/api/subscribe")
def subsribe():
    email = request.args['email']
    userHandler.subscribe(email)
    return "OK"


@app.route("/api/user")
def getAllUsers():
    return jsonify(userHandler.getAllUsers())

@app.route("/api/mail")
def sendMail():
    return mailHandler.sendOnAllMails("Title", "Hello", ["dima.lupyak@gmail.com"])
