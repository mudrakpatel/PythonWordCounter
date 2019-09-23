import requests
from bs4 import BeautifulSoup
import operator

def wordCounterFunction(url = 'http://quotes.toscrape.com/'):
    wordList = []
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, features = 'html.parser')
    for tagTitle in soup.select('a.item-header-title.dyn-link'):
        content = tagTitle.string
        words = content.lower().split()
        for word in words:
            wordList.append(word)
    # print('>>> All words appended')
    cleanUpWordList(wordList)


def cleanUpWordList(wordList):
    cleanWordList = []
    for word in wordList:
        symbols = "!@#$%^&*()_+-={}<>?,.'[];:|/\""
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            # print(word)
            cleanWordList.append(word)
    createDictionary(cleanWordList)


def createDictionary(cleanWordList):
    wordCount = {}
    for word in cleanWordList:
        if word in wordCount:
            wordCount[word] = wordCount[word] + 1
        else:
            wordCount[word] = 1
    for key, value in sorted(wordCount.items(), key = operator.itemgetter(1)):
        '''0 for key and 1 for value and so on...
            depending on the number of loop variables'''
        print(key, ':', value)