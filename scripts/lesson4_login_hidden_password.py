#!/usr/bin/python

# We make use of the getpass library which allows
# the user to type the password without revealing it.
# Similar to when we do sudo in Linux, or when we
# push/pull with git.

import sys
import getpass

secret_pwd = 'txd'

class Client():
	def __init__(self, usr, pwd):
		self.usr = usr
		self.pwd = pwd


def verifyPassword(client):
	if client.pwd == secret_pwd:
		print('Welcome ', client.usr, ': access granted')
		return True
	else:
		print('Access denied: wrong password')
		return False
	

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')
	print('Name of program:', sys.argv[0])
	print('Number of arguments:', len(sys.argv))
	print('Arguments:', sys.argv)
	try:
		
		if len(sys.argv) > 2:
			client = Client( sys.argv[1], sys.argv[2] )
		elif len(sys.argv) > 1:
			client = Client( sys.argv[1], getpass.getpass('Password:') )
		else:
			client = Client( input('Username: '), getpass.getpass('Password:') )
			
		if not verifyPassword(client):
			return 1
		
		print('***************************************')
		print('************ [ FINISHED ] *************')
		print('***************************************')
		return 0
	except:
		print('Exception caught')
		return 1
	
if __name__ == '__main__':
	sys.exit(main())