import requests
from bs4 import BeautifulSoup
import json

class Scrapper:
    
    def __init__(self) -> None:
        self.list_of_urls = ["https://www.pracuj.pl/praca/intern%20it;kw/krakow;wp?rd=0&et=1","https://nofluffjobs.com/pl/krakow?page=1&criteria=seniority%3Dtrainee"]
        self.main_dict = {'pracuj':None, 'nofluffjobs':None}
        self.noFluffJobs()
        self.pracuj()
        
    def noFluffJobs(self):

        url = self.list_of_urls[1]
        titles = []

        while True:

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            h3_elements = soup.select('nfj-postings-list h3')
            text_values = [h3.get_text(strip=True) for h3 in h3_elements]
            
            a_elements = soup.select('.posting-list-item')
            href_values = [element['href'] for element in a_elements]
            base_url = "https://nofluffjobs.com" 
                    
            for x in range(len(text_values)):
                try:
                    if x < len(href_values):
                        titles.append({'title': text_values[x], "link":(base_url + href_values[x])})
                except AttributeError:
                    None

            pagination = soup.select('a[aria-label="Next"]')
            if pagination:
                url = base_url + pagination[0]['href']
            else:
                break

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
            
# if __name__ == "__main__":           
#     scrap = Scrapper()
#     scrap.json()