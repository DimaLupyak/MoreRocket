from sqlalchemy import Column, Integer, String
from morerockets.handler.database import Base
from collections import OrderedDict


class EventHandler(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String(70))
    date = Column(String(50))
    desc = Column(String(250))
    site = Column(String(100))
    live = Column(String(100))

    def __init__(self, name, date, desc, site, company, latitude, longitude, live, mission):
        self.name = name
        self.date = date
        self.desc = desc
        self.site = site
        self.company = company
        self.latitude = latitude
        self.longitude = longitude
        self.live = live,
        self.mission = mission

    def __str__(self):
        return ", ".join((
            str(self.name),
            str(self.date),
            str(self.desc),
            str(self.site),
            str(self.company),
            str(self.latitude),
            str(self.longitude),
            str(self.live)))

    def serialize(self):
        return {'name': self.name, 'date': self.date, 'desc': self.desc, 'site': self.site, 'company': self.company,
                'latitude': self.latitude, 'longitude': self.longitude, 'live': self.live}


class User(Base):
    __tablename__ = 'user'
    email = Column(String(100), primary_key=True)

    def asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    def __init__(self, email):
        self.email = email
