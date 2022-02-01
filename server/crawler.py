import scrapy
from scrapy.crawler import CrawlerProcess

class Crawler(scrapy.Spider):
	name = 'crawler'

	def parse(self, response):
		print (response.url)
		urls = response.css('a::attr(href)').extract()
		for url in urls:
			yield response.follow(url, callback=self.parse)
		
if __name__ == "__main__":
	Crawler.custom_settings = {'RETRY_TIMES':0,'LOG_ENABLED':False}
	process = CrawlerProcess()
	process.crawl(Crawler, start_urls=["https://crawler-test.com/"], allowed_domains = ["crawler-test.com"])
	process.start()
