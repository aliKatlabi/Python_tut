import sys
sys.path.append('../')

from execution.runnable import run

if __name__ == "__main__":
	import sys
	run(int(sys.argv[1]))
