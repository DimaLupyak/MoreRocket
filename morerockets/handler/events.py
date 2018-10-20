import morerockets.spacelaunchnow_adapter as sp_adapter
from morerockets.models import EventHandler

def getEvents():
    eventsList = sp_adapter.getItems()
    
    # insert you event grabber here
    return [e.serialize() for e in eventsList]
