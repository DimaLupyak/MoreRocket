from models import EventHandler
from morerockets.models import EventHandler

def getEvents():
    eventsList = pacelaunchnow_adapter.getItems()
    
    # insert you event grabber here
    return [e.serialize() for e in eventsList]
