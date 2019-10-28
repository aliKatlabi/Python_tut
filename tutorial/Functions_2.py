i=5
def fun(par=i): #default values evaluated only once at the definition point
	print(par)

i=6
fun() #par will be 5


# important warning
# default values evaluated only ((once)) at the definition point
# this is important for mutables cause the default mutable will change and wont be
# evaluated again to give the previous value intended to be as default

# (mutable object such as a list, dictionary, or instances of most classes)

def connect(id=0, port=[443]):#mutable default
	port.append(port[len(port)-1]+1)
	return port
		
print(connect()) #[443, 444]
print(connect())# prints [443, 444, 455]
# this is like calling connect() on port =[443,444] (not [443] the wanted default)
print(connect())
#[443, 444, 455, 456] 

#to prevent sharing default (mutable) between subsequent calls 
def connect(id=0, port=None):
	if port is None:
		port=[433] #evaluated only on execution
	port.append(port[len(port)-1]+1)
	return port
		
print(connect()) #[443, 444]
print(connect()) #[443, 444]
print(connect()) #[443, 444] 





























