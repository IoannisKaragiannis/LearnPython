#!/usr/bin/python
import sys

def main():
	print('***************************************')
	print('Name of program:', sys.argv[0])
	print('Number of arguments:', len(sys.argv))
	print('Arguments:', sys.argv)
	try:
		print('Hello World')
		print('***************************************')
		return 0
	except:
		print('Exception caught')
		print('***************************************')
		return 1
	
if __name__ == '__main__':
	sys.exit(main())