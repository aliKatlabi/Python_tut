import sys
sys.path.append('../')

from modules.server.connection import connect

def run(port):
	print("try to run on port:",port)
	connect(port)

