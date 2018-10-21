import requests
import json

baseUrl = 'https://api.rocket.watch/launch'


def setLinksForEvent(event):
    missionsDictionary = getLaunches()
    if (event.mission in missionsDictionary):
        setAdditionalInfo(missionsDictionary[event.mission], event)


def setAdditionalInfo(missionId, event):
    details = json.loads(requests.get(baseUrl + '/' + str(missionId)).text)

    setType(event, details)
    setVideos(event, details)
    setSocial(event, details)


def setSocial(event, details):
    pads = details['launches'][0]['location']['pads']
    for pad in pads:
        if pad['agencies'] is not None:
            for agency in pad['agencies']:
                if agency['infoURLs'] is not None:
                    for url in agency['infoURLs']:
                        if 'https://twitter' in url:
                            event.twitter = url
                        if 'https://www.facebook' in url:
                            event.facebook = url


def setVideos(event, details):
    # videourls
    videoUrls = details['launches'][0]['vidURLs']
    live = ""
    if (len(videoUrls) > 0):
        for url in videoUrls:
            if ('youtube' in url):
                live = url
                break
    event.live = live


def setType(event, details):
    # launch type(commercial ect.)
    type = details['launches'][0]['agency']['type']
    event.ltype = type


def getLaunches():
    launches = json.loads(requests.get(baseUrl + '?limit=1500').text)['launches']
    missions = {}
    for item in launches:
        missions[item['mission']] = item['id']

    return missions
