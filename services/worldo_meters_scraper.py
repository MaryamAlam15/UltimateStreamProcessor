"""
Scrapper to fetch total corona cases in the world according to worldometers.info
"""

import requests
from bs4 import BeautifulSoup


class WorldoMetersScrapper:
    def __init__(self):
        self.url = 'https://www.worldometers.info/coronavirus/'
        self.case_counter_class_css = 'maincounter-number'

    def get_page_content(self):
        """
        fetch page content.
        """
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def get_cases_counter(self, soup):
        """
        finds div by css which shows total covid cases and returns its text.
        """
        text = soup.find('div', class_=self.case_counter_class_css).text.strip()
        return text

    def scrap_latest_cases(self):
        """
        wrapper method to:
            - fetch page content, and
            - get total covid cases.
        """
        soup = self.get_page_content()
        return self.get_cases_counter(soup)
