import models
from models import EventHandler, User
import handler.repository as repository
import re

email_pattern = '[^@]+@[^@]+\.[^@]+'


def getEvents():
    eventsList = []
    eventsList.append(EventHandler("name", "some date", "this is some description", "site some", "some company",
                                   "http://someurl.com").__dict__)
    eventsList.append(EventHandler("name", "some date", "this is some description", "site some", "some company",
                                   "http://someurl.com").__dict__)
    # insert you event grabber here
    return eventsList


def subscribe(email):
    if not re.match(email_pattern, email):
        return

    repository.saveUser(User(email))


def getAllUsers():
    models = []
    users = repository.getAllUsers()
    for user in users:
        models.append(user.asdict())
    return models
