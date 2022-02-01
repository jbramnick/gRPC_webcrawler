import scrapy

class Crawler(scrapy.Spider):
	name = 'crawler'
	allowed_domains = []
	def __init__(self, domain, url):
		allowed_domains.add(domain)

