import morerockets.spacelaunchnow_adapter as sp_adapter
from morerockets.handler import repository
from morerockets.models import EventHandler

def getEvents():
    eventsList = sp_adapter.getItems()    

    return [e.serialize() for e in eventsList]

def saveEvents():
    eventsList = sp_adapter.getItems()
    for e in eventsList:
        repository.saveEvent(e)

def getEventFromDb():
    event = repository.getEvent()
    return event.serialize()
