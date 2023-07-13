import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

class Scrapper:
    
    def __init__(self) -> None:
        self.list_of_urls = ["https://www.pracuj.pl/praca/intern%20it;kw/krakow;wp?rd=0&et=1","https://nofluffjobs.com/pl/krakow?criteria=seniority%3Dtrainee&page=1"]
        self.main_dict = {'pracuj':None, 'nofluffjobs':None}
        self.noFluffJobs()
        self.pracuj()
        
    def noFluffJobs(self):
        
        response = requests.get(self.list_of_urls[1])
        soup = BeautifulSoup(response.text, "html.parser")
        h3_elements = soup.select('nfj-postings-list h3')
        text_values = [h3.get_text(strip=True) for h3 in h3_elements]
        titles = []
        a_elements = soup.select('.posting-list-item')
        href_values = [element['href'] for element in a_elements]
        base_url = "https://nofluffjobs.com" 
                
        for x in range(len(text_values)):
            if x < len(href_values):
                titles.append({'title': text_values[x], "link":urljoin(base_url, href_values[x])})
        self.main_dict['nofluffjobs'] = titles
        
        
    def pracuj(self):
        response = requests.get(self.list_of_urls[0])
        soup = BeautifulSoup(response.text, "html.parser")
        titles = []
        list_of_headings = soup.find_all("h2", class_="listing_buap3b6")
        for x in range(len(list_of_headings)):
            try:
                heading = list_of_headings[x].find("a")
                titles.append({'title': heading.text, "link":heading["href"]})
            except AttributeError:
                None
            
        self.main_dict['pracuj'] = titles
        


    def json(self):
        with open("plik.json", "w", encoding = "UTF-8") as jf:
            json.dump(self.main_dict, jf, indent = 4, ensure_ascii=False)
            
            
scrap = Scrapper()
scrap.json()