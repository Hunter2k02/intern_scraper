from Scrapper import Scrapper

titles1 = []
titles2 = []

Scrap = Scrapper()

titles1 = Scrap.pracuj()

for title in titles1:
    for value in title.values():
        print(value)
    print()
    


