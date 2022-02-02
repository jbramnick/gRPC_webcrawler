from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse
   
urls=[]
   
def scrape(site):

	r = requests.get(site)

	s = BeautifulSoup(r.text,"html.parser")

	domain = urlparse(site).netloc

	for i in s.find_all("a"):
		href = i.attrs['href']
		if href.startswith("/") and href!="/":
			site = site+href
			if site not in urls and urlparse(site).netloc==domain: 
				urls.append(site) 
				print(site+"\n")
				scrape(site) 

if __name__ =="__main__":
	site="https://crawler-test.com"

	scrape(site)
