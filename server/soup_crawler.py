from bs4 import BeautifulSoup
import requests
   
# lists
urls=[]
   
# function created
def scrape(site):
       
    # getting the request from url
    r = requests.get(site)
       
    # converting the text
    s = BeautifulSoup(r.text,"html.parser")
    print(s)  
    
   
# main function
if __name__ =="__main__":
   
    # website to be scrape
    site="http://example.webscraping.com//"
   
    # calling function
    scrape(site)
