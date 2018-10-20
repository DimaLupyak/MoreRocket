from handler.database import db_session
from models import User

def saveUser(user):
    db_session.add(user)
    db_session.commit()