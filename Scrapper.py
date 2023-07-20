import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

class Scrapper:
    
    def __init__(self) -> None:
        self.list_of_urls = ["https://www.pracuj.pl/praca/krakow;wp?rd=30&et=1&pn=1","https://nofluffjobs.com/pl/krakow?page=1"]        self.main_dict = {'pracuj':None, 'nofluffjobs':None}
        self.noFluffJobs()
        self.pracuj()
        
    def noFluffJobs(self):
       
        url = self.list_of_urls[1]
        titles = []
        base_url = "https://nofluffjobs.com" 
        
        while True:

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            h3_elements = soup.find_all('h3', class_="posting-title__position")
            text_values = [h3.get_text(strip=True) for h3 in h3_elements]        

            a_elements = soup.find_all('a', class_='posting-list-item')
            href_values = [element['href'] for element in a_elements]
            
                    
            for x in range(len(text_values)):
                try:
                    if x < len(href_values):
                        titles.append({'title': text_values[x], "link":(base_url + href_values[x])})
                except AttributeError:
                    None

            pagination = soup.find_all('a', {'aria-label': 'Next'})
            if pagination:
                url = base_url + pagination[0]['href']
            else:
                break

        self.main_dict['nofluffjobs'] = titles                
        
                
            
                
                
        self.main_dict['nofluffjobs'] = titles
        
        
    def pracuj(self):
        
        titles = []
        parent_url = self.list_of_urls[0]
        
        while True:
            
            response = requests.get(self.list_of_urls[0])
            soup = BeautifulSoup(response.text, "html.parser")
            list_of_headings = soup.find_all("h2", class_="listing_buap3b6")
            
            difference = len(parent_url)-len(self.list_of_urls[0])
            
            for x in range(len(list_of_headings)):
                try:
                    heading = list_of_headings[x].find("a")
                    titles.append({'title': heading.text, "link":heading["href"]})
                except AttributeError:
                    None
            if soup.find(class_="listing_n5kktfs size-small variant-secondary listing_b1fqykql"):
                
                
                arr = list(self.list_of_urls[0])
                digit = int(''.join(arr[(difference-1):]))
                digit+=1
                arr[(difference-1):] = str(digit)
                self.list_of_urls[0] = ''.join(arr)
                
                
            else:
                break
                
        
        self.main_dict['pracuj'] = titles
        


    def json(self):
        with open("plik.json", "w", encoding = "UTF-8") as jf:
            json.dump(self.main_dict, jf, indent = 4, ensure_ascii=False)
            
            
scrap = Scrapper()
scrap.json()