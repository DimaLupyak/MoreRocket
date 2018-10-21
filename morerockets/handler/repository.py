from morerockets.handler.database import db_session
import morerockets.handler.media as media
from morerockets.models import User

from morerockets.models import EventHandler

def saveUser(user: User):
    db_session.add(user)
    db_session.commit()

def saveEvent(event: EventHandler):
    media.setLinksForEvent(event)
    db_session.add(event)
    db_session.commit()

def clearEvents():
    db_session.query(EventHandler).delete()
    db_session.commit()

def getAllEvent():
    return EventHandler.query.all()

def getFirstEvent():
    return EventHandler.query.first()

def getAllUsers():
    return User.query.all()