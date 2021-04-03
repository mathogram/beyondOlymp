import os

listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk("."):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]

def clean(arr):
	output = []
	for fileName in arr:
		if(fileName.count("/") > 2 and fileName.count("/.") == 0):
			output.append(fileName)
	return output

listOfFiles = clean(listOfFiles)
k=0
for path in listOfFiles:
	fRead = open(path[2:], "r")
	text = fRead.read()
	text = text.replace("&gt;", ">")
	text = text.replace("&ge;", "\ge")
	text = text.replace("&lt;", "<")
	text = text.replace("&le;", "\le")
	text = text.replace("&amp;", "&")
	text = text.replace("\[", " $$ ")
	text = text.replace("\]", " $$ ")
	text = text.replace("\(", " $ ")
	text = text.replace("\)", " $ ")
	fRead.close()

	fWrite = open(path[2:], "w")
	fWrite.write(text)
	fWrite.close()

print("done!")