import requests
import json
import models

kennedyUrl = 'https://www.kennedyspacecenter.com'
baseUrl = kennedyUrl + '/api/'
getEventUrlPath = 'sitecore/Event/GetEvents'

headers = {'Content-Type': 'application/json'}

datasourceId = "{5CEC271B-AFD1-4DC5-B872-E450B9CA1B1D}"
categoryList = "{C5A59F38-0044-45B3-A04B-BCA1FC9F5344}"


def requestEvents(start, end):
    payload = {'startDate': start,
               'endDate': end,
               'datasourceID': datasourceId,
               'categoryList': categoryList,
               'Query': '',
               'PageIndex': 0,
               'PageSize': 10,
               'Start': "201811"}
    resp = requests.post(baseUrl + getEventUrlPath, headers=headers, params=payload)

    if ('JsonResult' not in str(resp.content)):
        return None
    return kennedyArrToEventHandlerArr(json.loads(json.loads(resp.text)['JsonResult']))


def kennedyArrToEventHandlerArr(eventList):
    res = []
    for event in eventList:
        res.append(kannadyToEventHandler(event))
    return res


def kannadyToEventHandler(event):
    return models.EventHandler(event['title'], event['start'], event['eventShortSummary'], event['location'], None,
                               kennedyUrl + event['url'])


result = requestEvents("", "")


# def ticketSearcher(fromStation, toStation, date, time):
#     payload = {'from': fromStation, 'to': toStation, 'date': date, 'time': time, 'get_tpl': 1}
#     resp = requests.post(baseUrl + trainSearch, headers=postHeaders, data=payload)
#     return json.loads(resp.text)
