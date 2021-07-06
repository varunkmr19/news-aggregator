import requests
from bs4 import BeautifulSoup
import urllib


class ZeeNewsScraper:
    def __init__(self):
        self.stories = []
        self.url = "https://zeenews.india.com/top-news"

    def getTheStories(self, news_stories):
        for data in news_stories:
            htmlatag = data.find("h3").find("a")
            headline = htmlatag.getText()
            url = htmlatag.get("href")
            d = {"headline": headline,
                 "url": url}
            self.stories.append(d)

    def scrapeWebsite(self):
        # Getting stories from Zee News.
        zeenews = self.url
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        req = urllib.request.Request(zeenews, headers=hdr)
        page = urllib.request.urlopen(req)
        r = requests.get(zeenews)
        data = r.text
        soup = BeautifulSoup(data, "lxml")
        foundstories = soup.find_all(
            "div", class_="sec-con-box")
        self.getTheStories(foundstories)
        return self.stories


class NdtvScraper:
    def __init__(self):
        self.stories = []
        self.url = "https://www.ndtv.com/top-stories"

    def getTheStories(self, news_stories):
        for data in news_stories:
            url = data.a.get("href")
            headline = data.getText()
            d = {"headline": headline,
                 "url": url}
            self.stories.append(d)

    def scrapeWebsites(self):
        # Getting stories from NDTV News.
        ndtv = self.url
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
        req = urllib.request.Request(ndtv, headers=hdr)
        page = urllib.request.urlopen(req)
        r = requests.get(ndtv)
        data = r.text
        soup = BeautifulSoup(data, "lxml")
        foundstories = soup.find_all(
            "h2", class_="newsHdng")
        self.getTheStories(foundstories)
        return self.stories
