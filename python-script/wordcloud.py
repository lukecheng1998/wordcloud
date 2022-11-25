import requests
from bs4 import BeautifulSoup
import re
import sys
from googlesearch import search
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

link = "test link" #test link current, will change links to specific wikipedia articles
searchword = ""

def getTopSearchResults(query):
    result = []
    for i in search(query, tld = 'com', lang = "en", num = "50", start = 0, stop = 50, pause = 3.0):
        result.append(i)
    for i in result(): #Test for our results
        print(result[i])
    return result