# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import json

jsonOutput = {"items":[]}

# Search the book with the keyword
url = 'http://chuangshi.qq.com/search/searchindex/type/all/wd/' + {query} + '.html'
searchPage = urlopen(quote(url, safe='/:?='))

# Analyze the searchPage by BeautifulSoup
bsObj = BeautifulSoup(searchPage, 'html.parser')

# Get the search result list
srList = bsObj.find('ul', {'id':'searchResultList'}).find_all('li')

# Get the title, author, cover and page address in each item
def getTitle(i):
	titlePosition = i.find('h1').find('a')
	title = re.sub(r'(\n|\s*)', '', titlePosition.get_text())
	return title

def getAuthor(i):
	authorPosition = i.find('div', {'class':'search_r_info'}).find_all('p')[0].find('a')
	author = re.sub(r'(\n|\s*)', '', authorPosition.get_text())
	return author

def getCover(i):
	coverPosition = i.find('div', {'class':'search_r_img'}).find('img')
	cover = coverPosition.get('src')
	return cover

def getPage(i):
	pagePosition = i.find('div', {'class':'search_r_img'}).find('a')
	page = pagePosition['href']
	return page

# Now get them!
item = {
    "title": "",
    "subtitle": "",
    "arg": "",
    "autocomplete": "",
    "icon": {
        "path": ""
    }
}

for i in srList:
	item['title'] = getTitle(i)
	item['subtitle'] = getAuthor(i)
	item['arg'] = getPage(i)
	item['autocomplete'] = item['title']
	item['icon']['path'] = getCover(i)
	jsonOutput['items'].append(item)

output = json.dumps(jsonOutput, ensure_ascii=False, indent=4)

print(output)