from persistentDictionary import *
jsonFile="file.txt"
diction = {'Age': 7, 'Name': 'Manni', 'This':'That',"Here":"There"}
diction2={}
#print diction.keys()
jsonifyDictionary(diction,jsonFile)
# print diction.keys()
# print diction.values()
diction2= makeDictionary(jsonFile)
#print diction2.keys()
print diction2[diction2.keys()[1]]