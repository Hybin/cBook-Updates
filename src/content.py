# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import json
import re
import os
import clear

def getList(page):
	jsonOutput = {"items":[]}

	# open the page of introduction
	introPage = urlopen(quote(page, safe='/:?='))
	soup = BeautifulSoup(introPage, 'html.parser')

	# get the content list page
	url = soup.find('div', class_='tablist').find_all('li')[1].find('a')['href']
	contentPage = urlopen(url)
	bsObj = BeautifulSoup(contentPage, 'html.parser')

	# get the title and link
	def getTitle(o):
		title = re.sub(r'\n*', '', o.find('a').get_text())
		return title

	def getLink(o):
		link = o.find('a')['href']
		return link

	def getInfo(o):
		info = re.sub(r'\xa0', ' ', o.find('a')['title'])
		return info

	item = {
		"title": "",
		"subtitle": "",
		"arg": "",
	}

	volumes = bsObj.find_all('ul', class_='block_ul')
	for v in volumes:
		chapters = v.find_all('li')
		for c in chapters:
			item['title'] = getTitle(c)
			item['subtitle'] = getInfo(c)
			item['arg'] = getLink(c)
			jsonOutput['items'].insert(0, item)
			item = {
				"title": "",
				"subtitle": "",
				"arg": "",
			}

	output = json.dumps(jsonOutput, ensure_ascii=False, indent=4)
	
	# clear the cache of file icons
	clear.on()
	
	# output the results
	print(output)
