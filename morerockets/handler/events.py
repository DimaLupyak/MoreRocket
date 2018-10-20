import morerockets.spacelaunchnow_adapter as sp_adapter


def getEvents():
    eventsList = sp_adapter.getItems()

    # insert you event grabber here
    return [e.serialize() for e in eventsList]
