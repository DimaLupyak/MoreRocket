import requests
from models import EventHandler as eh
from bs4 import BeautifulSoup as bs


def get_next(tag,value):
	for item in tag:
		if value in item:
			yield item.next_sibling
def get_values(tag,value):
	buf = []
	for value in get_next(tag,value):
		buf.append(value)
	return buf

def object_generator(dates,vehicles,missions,sites,times):
	for value in zip(dates,vehicles,missions,sites,times):
		object = eh(name=None,date=None,desc=None,site=None,company=None,latitude=None,longitude=None,live=None)
		object.name = value[1] #vehicles
		object.date = value[0] #times
		object.desc = value[4]+value[2] #missions
		object.site = None
		object.company = None
		object.live = None
		yield object
			
if __name__ == "__main__":
	data = eh(name='Test',date=None,desc=None,site=None,company=None,latitude=None,longitude=None,live=None)
	r = requests.get("https://spacecoastlaunches.com/blog/launch-list/")
	soup = bs(r.content,'html.parser')
	tag = soup.findAll("span", {"class":"sc-launch__title--secondary"})
	dates = get_values(tag,'Date:')
	vehicles = get_values(tag,'Vehicle:')
	missions = get_values(tag,'Mission:')
	sites = get_values(tag,'Launch Site:')
	times = get_values(tag,'Launch Window:')
	output = list()
	for object in object_generator(dates,vehicles,missions,sites,times):
		"""
		print(object.serialize())
		print(object.name)
		print(object.date)
		print(object.desc)
		print(object.site)
		print(object.company)
		print(object.latitude)
		print(object.longitude)
		print(object.live)"""
		output.append(object.serialize())
	return output