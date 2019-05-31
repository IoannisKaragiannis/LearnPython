#!/usr/bin/python
import sys

def list2String(x):
	out = ''
	for i in range(len(x) - 1):
		out += str(x[i]) + ', '
	out += 'and ' + str(x[len(x) - 1])
	return out

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')

	spam = ['apples', 'bananas', 'tofu', 'cats']
	spam2 = ['apples', 'bananas', 'tofu', 'cats', 4, 7, 'dogs']
	print(list2String(spam))
	print(list2String(spam2))	
	
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())