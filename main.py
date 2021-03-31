import os
import json

file = open('задачи.js')
jsonFile = file.read();

y = json.loads(jsonFile)

def clean(str):
	str = str.strip()
	if str[:len("&nbps;")] == "&nbsp;":
		str = str[len("&nbps;"):]
	if str[-len("<br>"):] == "<br>":
		str = str[:-len("<br>")]
	return str.strip()


for olymp in y:
	if olymp["title"].find("Городская олимпиада по математике среди физ-мат школ")+1:
		print(olymp["title"])
		year = olymp["title"].split(" ")[-2]
		# group = olymp["title"].split(" ")[7]
		# group = "junior"

		for problem in range(len(olymp["problems"])):
			file_path = "musab/"+ str(year) #+"/" + str(group)

			if not os.path.exists(file_path):
				os.makedirs(file_path)

			f = open(file_path + "/problem"+str(problem+1)+".md", "w")
			f.write(clean(olymp["problems"][problem]))
			f.close()

print("done!")