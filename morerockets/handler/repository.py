from morerockets.handler import db_session
from morerockets.models import User


def saveUser(user):
    db_session.add(user)
    db_session.commit()


def getAllUsers():
    return User.query.all()
