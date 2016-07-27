#This library is used to allow for persistent use of dictionaries
import json
import os


def inFile(text):
	#returns if a string is in a file
	f=open(dataFile,'r')
	if text.lower() in f.read():
		return True
		f.close()
	else:
		return False
		f.close()

def replace(original,replacement):
	f=open(dataFile,'r')
	data=f.read()
	f.close()
	data=data.replace(original,replacement)
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
	if os.path.isfile('./'+datFile): 
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
	else:
		open(datFile,'w').write("{}")

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

def jsonifyDictionary(datFile,dictionary):
	for i in range(0,len(dictionary)):
		appendJson(datFile,dictionary.keys()[i],dictionary.values()[i])

