import requests
from bs4 import BeautifulSoup
from lxml import etree

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'})


class AppStoreExtractor:
    def __init__(self, url: str, fetch: bool = False):
        self.url = url
        if fetch:
            self.fetch_page()

    def fetch_page(self):
        webpage = requests.get(self.url, headers=HEADERS)
        self.soup = BeautifulSoup(webpage.content, "html.parser")
        self.dom = etree.HTML(str(self.soup))

    def get_downloads(self):
        span = self.dom.xpath('/html/body/div[3]/div[1]/div[3]/div/ul/li[3]/span/span[2]')
        downloads = span[0].text
        return downloads

    def get_app_type(self):
        app_type_dirty = self.dom.xpath('/html/body/div[3]/div[1]/div[3]/div/ul/li[2]/span/text()')
        # app_type = ["\n", "\nWatch Face\n"]
        app_type = ''.join(app_type_dirty).replace('\n', '')
        return app_type

    def get_ratings(self):
        rating_section = self.dom.xpath('/html/body/div[3]/div[1]/div[3]/div/ul/li[4]/span/span')
        rating = rating_section[0].attrib['title']

        rating_votes_element = self.dom.xpath('/html/body/div[3]/div[1]/div[3]/div/ul/li[4]/span/a/span')
        rating_votes = rating_votes_element[0].text
        return rating, rating_votes

    def get_developer(self):
        dev_element = self.dom.xpath('/html/body/div[3]/div[1]/div[3]/div/h1')
        value = dev_element[0].text
        return value

    def get_all(self):
        return self.get_developer(), self.get_ratings(), self.get_app_type(), self.get_downloads()
