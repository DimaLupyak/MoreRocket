import morerockets.spacelaunchnow_adapter as sp_adapter
from morerockets.handler import repository
from morerockets.models import EventHandler
from datetime import datetime
import morerockets.handler.mail as mail
from morerockets import app

def getEvents():
    eventsList = sp_adapter.getItems()
    return [e.serialize() for e in eventsList]

def updateEvents():
    with app.app_context():
        repository.clearEvents()
        eventsList = sp_adapter.getItems()
        for e in eventsList:        
            repository.saveEvent(e)
        first_event = repository.getFirstEvent()
        event_datetime = datetime.strptime(first_event.date, '%Y-%m-%dT%H:%M:%SZ')
        current_datetime = datetime.utcnow()
        diffInHours = int((event_datetime - current_datetime).total_seconds() / 60.0 / 60.0)
        if diffInHours == 24 or diffInHours == 1:
            recipients = []
            for user in repository.getAllUsers():
                recipients.append(user.email)
            sbj = f"{first_event.name} will launch in {diffInHours} Hours"
            msg = f"{first_event.name} will launch in {diffInHours} Hours. {first_event.desc}. For more details you can visit http://nasa.spaceappchallenge.s3-website-us-east-1.amazonaws.com/"
            mail.sendOnAllMails(sbj, msg, recipients)
    
