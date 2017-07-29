import os

path = os.getcwd()
path = os.path.join(path, 'icons')
if not os.path.exists(path):
    os.mkdir(path)

for file in os.listdir(path):
	os.remove(os.path.join(path,file))