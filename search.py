# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import re
import os
import json
import download

def query(query):
    jsonOutput = {"items":[]}

    # Search the book with the keyword
    url = 'http://chuangshi.qq.com/search/searchindex/type/all/wd/' + query + '.html'
    searchPage = urlopen(quote(url, safe='/:?='))

    # Analyze the searchPage by BeautifulSou
    bsObj = BeautifulSoup(searchPage, 'html.parser')

    # Get the search result list
    srList = bsObj.find('ul', class_='search_result_list').find_all('li')

    # Get the title, author, cover and page address in each item

    def getTitle(i):
        titlePosition = i.find('h1').find('a')
        title = re.sub(r'(\n|\s*)', '', titlePosition.get_text())
        return title
   
    def getAuthor(i):
        authorPosition = i.find('div', class_='search_r_info').find_all('p')[0].find('a')
        author = re.sub(r'(\n|\s*)', '', authorPosition.get_text())
        return author
    
    def getCover(i):
        coverPosition = i.find('div', class_='search_r_img').find('img')
        cover = coverPosition.get('src')
        file = download.getImage(cover, path, getTitle(i))
        coverPath = file
        return coverPath

    def getPage(i):
        pagePosition = i.find('div', class_='search_r_img').find('a')
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

    # Create a file fold for icons
    path = os.getcwd()
    path = os.path.join(path, 'icons')
    if not os.path.exists(path):
        os.mkdir(path)

    for r in srList:
        item['title'] = getTitle(r)
        item['subtitle'] = getAuthor(r)
        item['arg'] = getPage(r)
        item['autocomplete'] = item['title']
        item['icon']['path'] = getCover(r)
        jsonOutput['items'].append(item)
        item = {
            "title": "",
            "subtitle": "",
            "arg": "",
            "autocomplete": "",
            "icon": {
                "path": ""
            }
        }

    output = json.dumps(jsonOutput, ensure_ascii=False, indent=4)
    print(output)