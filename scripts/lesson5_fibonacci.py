#!/usr/bin/python

import sys
import math

# This closed-form has some built-in limits for the number of decimal places
# it can accurately compute. It starts diverging after F[72]
def closed_form(n):
	phi = (1.0 + math.sqrt(5))*0.5
	tmp = phi**n
	return int( math.floor( (tmp - (-1)**n/tmp ) / math.sqrt(5) ) ) 

# This is more accurate but way more expensive. In order to return the 1000th
# fibonacci number, all the fibonacci numbers up to the 999th must be calculated
# beforehand.
def recursively(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		f = [None]*(n)
		f[0] = 1
		f[1] = 1
		for i in range(2, n):
			f[i] = f[i-1] + f[i-2]
		return f[n-1]

def isNumber(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def giveMeFibonacciNumber():
	while True:
		n = input('Calculate N-th fibonacci number, where N = ')		
		if isNumber(n):
			n_float = float(n)
			if n_float.is_integer():
				n_int = int(n_float)
				if n_int >= 1 and n_int < 72:
					print('Fib[',n_int,'] =',closed_form(n_int), '(closed-form)')
					print('Fib[',n_int,'] =',recursively(n_int), '(recursively)')
					break
				elif n_int >= 72:
					print('Fib[',n_int,'] =',closed_form(n_int), '(closed-form): beware inaccuracies here')
					print('Fib[',n_int,'] =',recursively(n_int), '(recursively)')
					break
				else:
					print(str(n_int) + ' is not positive!')
			else:
				print(str(n_float) + ' is not an integer!')
		else:
			print(n + ' is not a number!')

def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)
	print('Name of program:', sys.argv[0])
	print('Number of arguments:', len(sys.argv))
	print('Arguments:', sys.argv)
		
	giveMeFibonacciNumber()
		
	print(bound + '\n' + end + '\n' + bound)
	return 0	

	
if __name__ == '__main__':
	sys.exit(main())