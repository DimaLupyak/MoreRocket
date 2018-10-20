import urllib.request
import json 
from models import EventHandler
URL = "https://spacelaunchnow.me/3.2.0/launch/upcoming/?format=json"

def getItems():
    output = []
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
        for result in data['results']:
            try: 
                name = result['rocket']['configuration']['name']
            except: pass
            try: 
                date = result['window_start']
            except: pass
            try: 
                desc = result['mission']['description']
            except: pass
            try: 
                mission = result['mission']['name']
            except: pass
            try: 
                site = result['pad']['location']['name']
            except: pass
            try: 
                company = result['rocket']['configuration']['launch_service_provider']
            except: pass
            try: 
                latitude = result['pad']['latitude']
            except: pass
            try: 
                longitude = result['pad']['longitude']
            except: pass
            output.append(
                EventHandler(
                    name = name,
                    date = date,
                    desc = desc,
                    company = mission,
                    site = site,
                    latitude = latitude,
                    longitude = longitude,
                    live = None
                )
            )
    return output