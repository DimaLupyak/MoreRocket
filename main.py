class EventHandler():
	def __init__(self,name,date,desc,site,company,live):
		self.name = name
		self.date = date
		self.desc = desc
		self.site = site
		self.company = company
		self.live = live
		
a = EventHandler(name = 'Test',date = None,desc=None, site = None,company = None,live= None)
print(a.name)