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

def giveMeFibonacciNumber():
	fibonacci = input('Calculate N-th fibonacci number, where N = ')
	
	# check if input is positive integer
	if not fibonacci.isdigit() or int(fibonacci) < 1:
		print('N should be positive integer!')
		giveMeFibonacciNumber()
	else:
		if int(fibonacci) > 71:
			print('Fib[',fibonacci,'] =',closed_form(int(fibonacci)), '(closed-form): beware inaccuracies here')
		else:
			print('Fib[',fibonacci,'] =',closed_form(int(fibonacci)), '(closed-form)')
		print('Fib[',fibonacci,'] =',recursively(int(fibonacci)), '(recursively)')		

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')
	print('Name of program:', sys.argv[0])
	print('Number of arguments:', len(sys.argv))
	print('Arguments:', sys.argv)
	try:
		
		giveMeFibonacciNumber()
		
		print('***************************************')
		print('************ [ FINISHED ] *************')
		print('***************************************')
		return 0
	except:
		print('Exception caught')
		return 1
	
if __name__ == '__main__':
	sys.exit(main())