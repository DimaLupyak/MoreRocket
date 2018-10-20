class EventHandler():
	def __init__(self,name,date,desc,site,company,latitude,longitude,live):
		self.name = name
		self.date = date
		self.desc = desc
		self.site = site
		self.company = company		
		self.latitude = latitude
		self.longitude = longitude
		self.live = live

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
		return {'name':self.name,'date':self.date,'desc':self.desc,'site':self.site,'company':self.company,'latitude':self.latitude,'longitude':self.longitude,'live':self.live}