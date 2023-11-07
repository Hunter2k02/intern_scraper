
import sys
sys.path.append("C:/Users/Szymon/Desktop/scrapper")
import unittest
from InternWebScrapper.Scrapper import Scrapper

class TestScrapper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scrapper()

    def test_noFluffJobs(self):

        # Test if the 'noFluffJobs' method returns non-empty titles and links
        self.assertIsNotNone(self.scraper.main_dict['nofluffjobs'])
        self.assertGreater(len(self.scraper.main_dict['nofluffjobs']), 0)

        # Test if each title has a corresponding link
        for item in self.scraper.main_dict['nofluffjobs']:
            self.assertIn('title', item)
            self.assertIn('link', item)

    def test_pracuj(self):

        # Test if the 'pracuj' method returns non-empty titles and links
        self.assertIsNotNone(self.scraper.main_dict['pracuj'])
        self.assertGreater(len(self.scraper.main_dict['pracuj']), 0)

        # Test if each title has a corresponding link
        for item in self.scraper.main_dict['pracuj']:
            self.assertIn('title', item)
            self.assertIn('link', item)
        
        

    def test_json(self):

        # Test if the 'json' method creates a file named "plik.json"
        self.scraper.json()
        import os
        self.assertTrue(os.path.exists("plik.json"))
        # Clean up after the test
        os.remove("plik.json")


if __name__ == "__main__":
    unittest.main()