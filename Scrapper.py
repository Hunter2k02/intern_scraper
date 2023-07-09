import requests
from bs4 import BeautifulSoup


class Scrapper:
    
    def __init__(self) -> None:
        self.list_of_urls = ["https://www.pracuj.pl/praca/intern%20it;kw/krakow;wp?rd=0&et=1","https://nofluffjobs.com/pl/krakow?criteria=seniority%3Dtrainee&page=1"]
    
    def noFluffJobs(self):
        pass
    
    def pracuj(self):
        response = requests.get(self.list_of_urls[0])
        soup = BeautifulSoup(response.text, "html.parser")
        titles = []
        list_of_headings = soup.find_all("h2", class_="listing_buap3b6")
        for x in range(len(list_of_headings)):

            heading = list_of_headings[x].find("a")
            titles.append({'title': heading.text, "link":heading["href"]})

        return titles    
    