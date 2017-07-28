import os
import urllib.request
import random

def getImage(url, path, name):
	filename = name + str(random.randint(0,99)) + '.jpg'
	local_path = os.path.join(path, filename)
	urllib.request.urlretrieve(url, local_path)
	return local_path