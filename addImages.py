import os
import re

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk("."):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

def clean(arr):
	output = []
	for fileName in arr:
		if(fileName.count("/") > 2 and fileName.count("/.") == 0 and fileName.count(".png") == 0 and fileName.count(".jpg") == 0):
			output.append(fileName)
	return output

listOfFiles = clean(listOfFiles)
k=0
for path in listOfFiles:
	fRead = open(path[2:], "r")
	text = fRead.read()
	if(text.find('<img src="https://matol.nomomon.repl.co/') + 1):
		print(path)
	fRead.close()
	text = text.replace("&amp;", "&")
	text = text.replace("https://matol.nomomon.repl.co/", "")

	fWrite = open(path[2:], "w")
	fWrite.write(text)
	fWrite.close()

print("done!")

# <img src="https://matol.nomomon.repl.co/http:&amp;&amp;matol.kz&amp;images&amp;14&amp;11_day1.png" height="150">

# response = requests.get("https://i.imgur.com/ExdKOOz.png")
# file = open("sample_image.png", "wb")
# file.write(response.content)
# file.close()