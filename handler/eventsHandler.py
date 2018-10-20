import main


def getEvents():
    eventsList = []
    eventsList.append(main.EventHandler("name", "some date", "this is some description", "site some", "some company",
                                        "http://someurl.com").__dict__)
    eventsList.append(main.EventHandler("name", "some date", "this is some description", "site some", "some company",
                                        "http://someurl.com").__dict__)
    # insert you event grabber here
    return eventsList
