import requests
import json

baseUrl = 'https://api.rocket.watch/launch'


def setLinksForEvent(event):
    missionsDictionary = getLaunches()
    if (event.mission in missionsDictionary):
        setAdditionalInfo(missionsDictionary[event.mission], event)


def setAdditionalInfo(missionId, event):
    details = json.loads(requests.get(baseUrl + '/' + str(missionId)).text)

    type = details['launches'][0]['agency']['type']
    event.ltype = type

    videoUrls = details['launches'][0]['vidURLs']
    live = ""
    if (len(videoUrls) > 0):
        for url in videoUrls:
            if ('youtube' in url):
                live = url
                break
    event.live = live


def getLaunches():
    launches = json.loads(requests.get(baseUrl + '?limit=1500').text)['launches']
    missions = {}
    for item in launches:
        missions[item['mission']] = item['id']

    return missions
