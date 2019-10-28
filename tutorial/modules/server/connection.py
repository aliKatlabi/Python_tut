
ports = 443,445,1031

def check(port):
	"""
	checking
	"""
	if port in ports:
		return True
		
def connect(port):
	"""
	connecting
	"""
	if(check(port)):
		print("connected")
	else:
		print("bad port")
