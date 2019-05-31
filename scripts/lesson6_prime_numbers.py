#!/usr/bin/python

import sys
import math
import timeit
import os

class Limits():
	def __init__(self, min, max):
		self.min = min
		self.max = max

class Prime():
	def __init__(self, list, min, max):
		self.list = list 
		self.min = min
		self.max = max

def sumOfDigits(num):
	sum = 0
	while num > 0:
		d = num%10
		num = num//10
		sum += d
	return sum

def isLastDigitFive(num):
	if num % 10 == 5:
		return True
	else:
		return False

def calculatePrimes(low, high):
	prime = Prime([], low, high)		
	if low == 1:
		low += 1
		if low > high:
			return prime
	if low == 2:
		prime.list.append(2)
		if low+1 > high:
			return prime			
	if low % 2 == 0:
		low += 1
	high += 1 # include the upper bound in the search		
	for i in range(low, high ,2):
		ctr = 0
		new_sqrt = int(i ** 0.5) + 1
		# improvement: search division only with prime numbers
		for j in range(3, new_sqrt, 2):
			if i != j and i % j == 0:
				ctr += 1
				break				
		if ctr == 0:
			prime.list.append(i)	
	return prime

def isValidInput(low, high):
	if not low.isdigit() or not high.isdigit():
		print('The limits must be positive integers!')
		return False
	elif int(low) < 1 or int(high) < 1:
		print('The limits must be positive integers!')
		return False
	elif int(low) > int(high):
		print('Upper limit must be equal or greater than the lower!')
		return False
	else:
		return True

def listOfPrimes():	
	limits = Limits(input('Enter the lower bound of your search (positive integer): '), input('Enter the upper bound of your search (positive integer): '))	
	while not isValidInput(limits.min, limits.max):
		limits = Limits(input('Enter the lower bound of your search (positive integer): '), input('Enter the upper bound of your search (positive integer): '))
	return calculatePrimes(int(limits.min), int(limits.max))	

def avgExecTime():
	print('prime(1,100):', timeit.timeit('calculatePrimes(1,100)', globals=globals(), number=10000)/10000, 'seconds')
	print('prime(1,1000):', timeit.timeit('calculatePrimes(1,1000)', globals=globals(), number=1000)/1000, 'seconds')
	print('prime(1,10000):', timeit.timeit('calculatePrimes(1,10000)', globals=globals(), number=100)/100, 'seconds')
	print('prime(1,100000):', timeit.timeit('calculatePrimes(1,100000)', globals=globals(), number=10)/10, 'seconds')
	print('prime(1,1000000):', timeit.timeit('calculatePrimes(1,1000000)', globals=globals(), number=2)/2, 'seconds')

def write2File(folder, file, data):
	# test if folder exists
	if not os.path.exists(folder):
		os.makedirs(folder)
	
	full_name = folder+'/'+file
	open(full_name, 'w').close()
	prime_file = open(full_name,"a") 
	size = len(data)
	for i in range(size):
		prime_file.write(str(data[i])+'\n')
	prime_file.close() 	

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')
	print('Name of program:', sys.argv[0])
	print('Number of arguments:', len(sys.argv))
	print('Arguments:', sys.argv)
		
	primes = listOfPrimes()
	size = len(primes.list)
	if size > 0:
		print( len(primes.list),'prime numbers where found in [',int(primes.min),',',int(primes.max),']')
		print('prime[',size, '] =',primes.list[-1])
	else:
		print('No prime numbers where found in [',int(primes.min),',',int(primes.max),']')
	
	dir = 'primes'
	name = str(primes.min)+'_to_'+str(primes.max)+'.txt'
	write2File(dir, name, primes.list)
	
	test = input('Do you want to perform speed-test (Y/N)?: ')
	if test == 'yes' or test == 'YES' or test == 'Y' or test == 'y':
		avgExecTime()
			
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())