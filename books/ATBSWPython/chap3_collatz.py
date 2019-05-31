#!/usr/bin/python
import sys

def collatz(number):
	if number%2 == 0:
		number = number // 2
		print(number)
	else:
		number = 3 * number + 1
		print(number)
	return number
	

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')
	
	try:
		col = collatz(int(input('Enter integer number: \n')))
		while col != 1:
			col = collatz(col)
			
	except ValueError:
		print('ValueError exception: The input should be an integer')
	
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())