from persistentDictionary import *
jsonFile="file.txt"
diction = {'Age': 7, 'Name': 'Manni', 'This':'That',"Here":"There"}
#print diction.keys()
jsonifyDictionary(jsonFile,diction)
print diction.keys()
print diction.values()