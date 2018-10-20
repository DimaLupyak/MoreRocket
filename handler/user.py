import handler.repository as repository
from models import User
import re

email_pattern = '[^@]+@[^@]+\.[^@]+'


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
