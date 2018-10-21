import requests
import json

baseUrl = 'https://api.rocket.watch/launch'


def setLinksForEvent(event):
    missionsDictionary = getLaunches()
    result = ""
    if (event.mission in missionsDictionary):
        links = getLinksFor(missionsDictionary[event.mission])
        result = ",".join(links)
    event.live = result


def getLinksFor(missionId):
    details = json.loads(requests.get(baseUrl + '/' + str(missionId)).text)
    videoUrls = details['launches'][0]['vidURLs']
    result = []
    if (len(videoUrls) > 0):
        for url in videoUrls:
            if ('youtube' in url):
                result.append(url)

    return result


def getLaunches():
    launches = json.loads(requests.get(baseUrl + '?limit=100').text)['launches']
    missions = {}
    for item in launches:
        missions[item['mission']] = item['id']

    return missions
