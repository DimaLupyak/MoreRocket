from sqlalchemy import Column, Integer, String
from handler.database import Base


class EventHandler(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String(70))
    date = Column(String(50))
    desc = Column(String(250))
    site = Column(String(100))
    live = Column(String(100))

    def __init__(self, name, date, desc, site, company, live):
        self.name = name
        self.date = date
        self.desc = desc
        self.site = site
        self.company = company
        self.live = live


class User(Base):
    __tablename__ = 'user'
    email = Column(String(100))

    def __init__(self, email):
        self.email = email
