from models import EventHandler
import spacelaunchnow_adapter

def getEvents():
    eventsList = pacelaunchnow_adapter.getItems()
    
    # insert you event grabber here
    return [e.serialize() for e in eventsList]
