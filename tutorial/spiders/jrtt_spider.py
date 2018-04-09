import scrapy

class JrttSpider(scrapy.Spider):
	"""docstring for JrttSpider"""
	# def __init__(self, arg):
	# 	super(JrttSpider, self).__init__()
	# 	self.arg = arg
	name = 'jrtt'

	start_urls = [
		'',
		'',
	]

	def parse(self,response):
		filename = response.url.split("&")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)