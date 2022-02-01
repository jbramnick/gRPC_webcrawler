import scrapy
from scrapy.crawler import CrawlerProcess

class Crawler(scrapy.Spider):
	name = 'crawler'
	allowed_domains = ['crawler-test.com']
	start_urls = ['https://crawler-test.com/']
	
	def parse(self, response):
		print ("Processing: "+response.url)
		print (response)
process = CrawlerProcess()

if __name__ == "__main__":
	process.crawl(Crawler)
	process.start()
