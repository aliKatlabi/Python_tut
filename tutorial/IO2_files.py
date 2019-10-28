#open(filename , mode)
#modes w(writ only) r (read only) a (append) r+(read + write) ..
#appending mode to b opens file in binary mode
#in text mode every thing is ok regarding differences (like line endings \n Unix , \r \n on windows)
#between platforms , BUT in binary these differences need handling


f = open("IOrelated" , "r+")
f.write("this is a first write in python")
content = f.read()
f.close()

print(content)

#It is good practice to use the with keyword when dealing with file objects.
#The advantage is that the file is properly closed

with open('IOrelated') as f:
    read_data = f.read()
    
print(read_data)

print(f.closed)

##Saving structured data with json

##The standard module called json can take Python data hierarchies, and convert them to string representations; t
#his process is called serializing.
#Reconstructing the data from the string representation is called deserializing

import IO
import json

#note:Object of type set is not JSON serializable

usersList = list(IO.users)

with open("IO_json","r+") as jsonf:
    json.dump(usersList,jsonf,sort_keys=True, indent=4) #json.dump(x, f) serialize to text file

with open("IO_json","r+") as jsonf:
    decodedlist = json.load(jsonf)#json.load(f) deserialize 

#json.dumps(usersList) seriliaze to the screen

print(decodedlist)






















