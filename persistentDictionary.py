#This library is used to allow for persistent use of dictionaries

import json
def inFile(text):
	#returns if a string is in a file
	f=open(dataFile,'r')
	if text.lower() in f.read():
		return True
		f.close()
	else:
		return False
		f.close()
	
def writeCommand(text):
	#Writes text to the file
	if not inFile(text):
		f=open(dataFile,'a')
		f.write(text.lower()+":\n")
		f.close()

def replace(original,replacement):
	f=open(dataFile,'r')
	data=f.read()
	f.close()
	print "old: " + data
	data=data.replace(original,replacement)
	print "new: " + data
	f=open(dataFile,'w')
	f.writeCommand(data)
	f.close()

def readJson(datFile,key,upperKey=None):
	try:
		with open(datFile) as data_file:
			data = json.load(data_file)
		if upperKey==None:
			return data[key]
		else:
			return data[upperKey][key]
	except:
	 	return False

def appendJson(datFile,key,value,upperKey=None):
	with open(datFile) as data_file:
		data = json.load(data_file)
		if upperKey==None:
			if not data.has_key(key):
				data[key] = value
		else:
			if not data[upperKey].has_key(key):
				data[upperKey][key]=value
	with open(datFile,'w') as outfile:
		json.dump(data, outfile,sort_keys=True)

def deleteJson(datFile,key,upperKey=None):
	with open(datFile) as data_file:
		data  = json.load(data_file)                                                
	try:
		if upperKey==None:
			del data[key]
		else:
			del data[upperKey][key]
		with open(datFile,'w') as outfile:
			json.dump(data,outfile)
	except:
		return False

def replaceJson(datFile,key,value,upperKey=None):
	with open(datFile) as data_file:
		data = json.load(data_file)
	if upperKey==None:
		data[key]=value
	else:
		data[upperKey][key]=value
	with open(datFile,'w') as outfile:
		json.dump(data, outfile)

def jsonifyCommand(com):
	#exlusions:
	splitc=com.split()
	if "google" in com and "open" not in com:
		executeCommand(com)
		return
	if any(x in splitc for x in ["craigslist","buy","c"]):
		if len(splitc)==3:
			# buy datsun fresno
			executeCommand("openb "+"https://"+splitc[2]+".craigslist.org/search/sss?sort=rel&query="+splitc[1])
			return
	if "read" == splitc[0]:
		executeCommand(com)
		return
	command=readJson(commandFile,com)
	if command==False:
		value=raw_input("This command has not been used before, please enter in the command\n:")
		if any(x in value for x in ["copy","cp"]):
			value=value.replace("copy ","")
			value=readJson(commandFile,value)
			appendJson(commandFile,com,value)
		else:
			appendJson(commandFile,com,value)
		executeCommand(value)
	else:
		executeCommand(command)
