import scrapy

class Crawler(scrapy.Spider):
	name = 'crawler'
	allowed_domains = []
	start_urls = []
	def __init__(self, domain, url):
		allowed_domains.add(domain)
		start_urls.add(url)

