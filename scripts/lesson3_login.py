#!/usr/bin/python
import sys

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
	print('Name of program:', sys.argv[0])
	print('Number of arguments:', len(sys.argv))
	print('Arguments:', sys.argv)
	try:
		if len(sys.argv) > 2:
			client = Client( sys.argv[1], sys.argv[2] )
		elif len(sys.argv) > 1:
			client = Client( sys.argv[1], input('Password: ') )
		else:
			client = Client( input('Username: '), input('Password: ') )
			
		if not verifyPassword(client):
			return 1
		
		return 0
	except:
		print('Exception caught')
		return 1
	
if __name__ == '__main__':
	sys.exit(main())