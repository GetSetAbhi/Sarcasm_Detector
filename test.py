import os
from time import gmtime, strftime
'''
names = ["sheikhimaan", "Sarcasticsapien", "Roflindian", "KhapPanchayat", "hamrust"]

for name in names:
	print(name)

name = "hamrust"

if name in names:
	print("Exists")
else:
	print("Non Existent")
	pass

'''

def generateFilename():
	#path = "/home/abhishek/Desktop/twitter_machine/Test/JsonTweets"
	path = str(os.getcwd())+"/Checker"
	name = strftime("%Y-%m-%d-%H:%M:%S",gmtime())

	#Checks of the directory exists or not
	if not os.path.isdir(path):
		#os.makedirs(path)
		print "Does not exist"
		os.makedirs(path)
	else:
		print "Folder already exists"


generateFilename()
'''
	filename = path + "/" + str(name) + ".json"
	return filename
'''