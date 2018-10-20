import morerockets.spacelaunchnow_adapter as sp_adapter


def getEvents():
    eventsList = sp_adapter.getItems()

    # insert you event grabber here
    return [e.serialize() for e in eventsList]


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='morerockets')

def getCountry(latitude, longitude):
    return geolocator.reverse(str(latitude) + ", " + str(longitude)).raw['address']['country']
