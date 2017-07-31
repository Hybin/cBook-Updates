from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import json
import re
import os
import download

def addTo(page):
	jsonOutput = json.loads(open('bookshelf.txt').read())

	# open the page of introduction
	introPage = urlopen(quote(page, safe='/:?='))
	soup = BeautifulSoup(introPage, 'html.parser')

	# get the title, author, icon and link
	def getTitle(o):
		titlePosition = o.find('div', class_='main1').find('div', class_='title').find('a')
		title = re.sub(r'(\n|\s*)', '', titlePosition.get_text())
		return title

	def getAuthor(o):
		authorPosition = o.find('div', class_='au_name').find('a')
		author = authorPosition.get_text()
		return author

	def getCover(o):
		coverPosition = o.find('a', class_='bookcover').find('img')
		cover = coverPosition.get('src')
		file = download.getImage(cover, path, getTitle(o))
		coverPath = file
		return coverPath

	def getContentPage(o):
		linkPosition = o.find('div', class_='tablist').find_all('li')[1].find('a')
		link = linkPosition['href']
		return link

	item = {
		"title": "",
		"subtitle": "",
		"arg": "",
		"icon": {
			"path": ""
		}
	}

	# Create a file fold for icons
	path = os.getcwd()
	path = os.path.join(path, 'shelf-icons')
	if not os.path.exists(path):
		os.mkdir(path)

	item['title'] = getTitle(soup)
	item['subtitle'] = getAuthor(soup)
	item['arg'] = getContentPage(soup)
	item['icon']['path'] = getCover(soup)
	jsonOutput['items'].append(item)
	
	output = json.dumps(jsonOutput, ensure_ascii=False, indent=4)
	
	fileToStore = open('bookshelf.txt', 'w')
	fileToStore.write(output)
	fileToStore.close()

	print(output)