import scrapy
from scrapy.crawler import CrawlerProcess

class Crawler(scrapy.Spider):
	name = 'crawler'
	def parse(self, response):
		print ("Processing: "+response.url)
		print (response)
process = CrawlerProcess()

if __name__ == "__main__":
	process.crawl(Crawler, start_urls=["https://crawler-test.com/"], allowed_domains = ["https://crawler-test.com/"])
	process.start()
