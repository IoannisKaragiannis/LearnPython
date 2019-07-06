#!/usr/bin/python
# {}.py - Program that takes a string and identifies if
# a specific phone number patter can be matched.

import sys, re

def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] != '-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)
	
	'''num = '415-555-4242'
	print(num + ' is a phone number: ' + str(isPhoneNumber(num)))
	num = 'bla bla bla'
	print(num + ' is a phone number: ' + str(isPhoneNumber(num)))
		
	message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
	for i in range(len(message)):
		chunk = message[i:i+12]
		if isPhoneNumber(chunk):
			print('Phone number found: ' + chunk)
	print('Done')'''
	
	# no groups
	phoneNumRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	# groups
	phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	# parenthesis of the first 3 numbers included in the pattern
	phoneNumRegex3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
	# groups in a neater way
	phoneNumRegex4 = re.compile(r'(\d{3})-(\d{3}-\d{4})')
	#optional matching
	phoneNumRegex5 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
	
	phone = 'Cell: 416-555-9999 Work: 210-555-3333'
	mo = phoneNumRegex1.search(phone)
	'''if mo != None:
		print('Phone number found: ' + mo.group())
		if mo.groups() != None:
			areaCode, mainNumber = mo.groups()	
			print('AreaCode: ' + str(areaCode) + '\n' +
				'Number: ' + str(mainNumber))'''
	
	print(phoneNumRegex1.findall(phone))
	
	print(bound + '\n' + end + '\n' + bound)
	return 0
	
if __name__ == '__main__':
	sys.exit(main())