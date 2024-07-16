from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod
from urllib.parse import urljoin
from .config import config

class BaseScraper():
    def __init__(self):
        self.base_url = config.get_base_url()

    @abstractmethod
    def scrape(self, endpoint: str, params: dict) -> str:
        pass

    def get_soup(self, endpoint: str, params: dict) -> BeautifulSoup:
        full_url = urljoin(self.base_url, endpoint)
        response = requests.get(full_url, params=params)
        return BeautifulSoup(response.text, 'html.parser')
