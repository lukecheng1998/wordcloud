# Webscrape the 50 most popular articles on wikipedia
import requests
from bs4 import BeautifulSoup
import re
import sys
from googlesearch import search
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

mainpagelink = "https://en.wikipedia.org/wiki/Wikipedia:Popular_pages"

def getarticles (link):
    res = requests.get(link)
    if res.status.code == 200 and 'content-type' in res.headers and res.headers.get('content-type'.startswith('text/html')):
        html = res.text
    else:
        print("This wikipedia page no longer exists")
        return
    print(html)
    return

def scrapeWikipedia ():
    return