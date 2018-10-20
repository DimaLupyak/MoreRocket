from morerockets.models import EventHandler


def getEvents():
    eventsList = []
    eventsList.append(EventHandler("name", "some date", "this is some description", "site some", "some company",
                                   "http://someurl.com").__dict__)
    eventsList.append(EventHandler("name", "some date", "this is some description", "site some", "some company",
                                   "http://someurl.com").__dict__)
    # insert you event grabber here
    return eventsList
