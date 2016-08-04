from persistentDictionary import *
#Name the file you will be using to store your dictionary
jsonFile="file.txt"
#Create sample dictionary 
diction = {'Age': 7, 'Name': 'Manni', 'This':'That',"Here":"There"}
#Make the dictionary persistent at the predefined location
storeDictionary(diction,jsonFile)
#Create the dictionary from the stored version
diction2= createDictionary(jsonFile)
#print diction2.keys()
print diction2[diction2.keys()[1]]