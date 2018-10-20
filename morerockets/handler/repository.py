from morerockets.handler.database import db_session
from morerockets.models import User

from morerockets.models import EventHandler

def saveUser(user: User):
    db_session.add(user)
    db_session.commit()

def saveEvent(event: EventHandler):
    db_session.add(event)
    db_session.commit()

def getEvent():
    return EventHandler.query.get(1)

def getAllUsers():
    return User.query.all()