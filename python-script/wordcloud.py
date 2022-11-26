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

def combineStrings(links):
    articles = ""
    for link in links:
        articles += ((scrape_article(link))) #scrape article here
    articles = cutString(articles)
    print(articles)

def cutString(fullText):
    stop = stopwords.words('english')
    fullText = word_tokenize(fullText.lower())
    fullText = [w for w in fullText if not w in stop]
    listToStr = ' '.join([str(elem) for elem in fullText])
    return listToStr

def scrape_article(url):
    res = requests.get(url)
    if res.status.code == 200 and 'content-type' in res.headers and res.headers.get('content-type'.startswith('text/html')):
        html = res.text
    else:
        print("error loading webpage")
        return
    soup = BeautifulSoup(html, 'html.parser') #find the article title

    h1 = soup.body.find('h1') # looks for the comment parent for h1
    root = h1
    if(root == None):
        print(URL + " contains no content")
        return
    #ensure that an article does not have fewer than 4 paragraphs
    while root.name != 'body' and len(root.find_all('p') < 4):
        root = root.parent
    
    #get all meaningful paragraphs/content
    ps = root.find_all(['h2', 'h3', 'h4', 'h5', 'p', 'pre'])
    ps.insert(0, h1) # insert title
    content = [tag2md(p) for p in ps]
    strings = str(content).lower()
    #remove special characters and numbers
    strings = strings.replace("\\r", "")
    strings = strings.replace("\\n", "")
    listquery = searchword.split()
    for w in listquery:
        strings = strings.replace(w, "*****")
    filter = ''.join([chr(i) for i in range(1, 32)])
    strings.translate(str.maketrans('', '', filter))
    pat = re.compile(r'[^A-Za-za-z ]+')
    answer = re.sub(pat, '', strings)
    return answer

def tag2md(tag):
    if tag.name == 'p':
        return tag.text
    elif tag.name == 'h1':
        return f'{tag.text}\n{"=" * len(tag.text)}'
    elif tag.name == 'h2':
        return f'{tag.text}\n{"-" * len(tag.text)}'
    elif tag.name in ['h3', 'h4', 'h5', 'h6']:
        return f'{"#" * int(tag.name[1:])} {tag.text}'
    elif tag.name == 'pre':
        return f'```\n{tag.text}\n```'

def printResult(query):
    return