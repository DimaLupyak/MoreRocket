from flask import Flask
from flask_cors import CORS

application = app = Flask(__name__)
CORS(app)

import morerockets.handler

from morerockets.handler.events import updateEvents
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

scheduler = BackgroundScheduler()
scheduler.add_job(func=updateEvents, trigger="interval", hours=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
