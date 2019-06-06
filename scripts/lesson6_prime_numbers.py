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

def isPrime(num):
	if num < 2 or (num % 2 == 0 and num != 2):
		return False
	else:
		ctr = 0
		# devide with odd numbers up to the square root of the number in test
		num_sqrt = int(num ** 0.5) + 1
		# improvement: search division only with prime numbers
		for k in range(3, num_sqrt, 2):
			if num != k and num % k == 0:
				ctr += 1
				break				
		if ctr == 0:
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
		# devide with odd numbers up to the square root of the number in test
		new_sqrt = int(i ** 0.5) + 1
		# improvement: search division only with prime numbers
		for j in range(3, new_sqrt, 2):
			if i != j and i % j == 0:
				ctr += 1
				break				
		if ctr == 0:
			prime.list.append(i)	
	return prime

def isNumber(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

def identifyPrimarity():
	while True:
		c = input('Enter a number of your choise (positive integer): ')
		if isNumber(c):
			c_float = float(c)
			if c_float.is_integer():
				c_int = int(c)
				if c_int > 0:
					if isPrime(c_int):
						print(str(c_int) + ' is a prime number')
					else:
						print(str(c_int) + ' is not a prime number')
					break
				else:
					print(str(c_int) + ' is not positive')
			else:
				print(str(c_float) + ' is not an integer')				
		else:
			print(c + ' is not a number')

def listOfPrimes():	
	limits = Limits(0,0)
	
	while True:
		low = input('Enter the lower bound of your search (positive integer): ')
		if isNumber(low):
			low_float = float(low)
			if low_float.is_integer():
				low_int = int(low_float)
				if low_int > 0:
					limits.min = low_int
					break
				else:
					print(str(low_int) + ' is not positive')
			else:
				print(str(low_float) + ' is not an integer')				
		else:
			print(low + ' is not a number')

	while True:
		high = input('Enter the upper bound of your search (positive integer): ')
		if isNumber(high):
			high_float = float(high)
			if high_float.is_integer():
				high_int = int(high_float)
				if high_int > 0:
					if high_int >= limits.min:
						limits.max = high_int
						break
					else:
						print('Upper bound must be equal or larger than the lower bound')
				else:
					print(str(high_int) + ' is not positive')
			else:
				print(str(high_float) + ' is not an integer')				
		else:
			print(high + ' is not a number')
	
	
	return calculatePrimes(limits.min, limits.max)	

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
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)
	
	print('1: test primarity of a specific number')
	print('2: calculate prime numbers within a range')
	print('3: perform speed test')
	while True:
		ask = input('What do you want to do (1, 2, or 3)?: ')
		if isNumber(ask):
			ask_float = float(ask)
			if ask_float.is_integer():
				ask_int = int(ask_float)
				if ask_int == 1:
					identifyPrimarity()
					break
				elif ask_int == 2:
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
					break
				elif ask_int == 3:
					avgExecTime()
					break
				else:
					print(str(ask_int) + ' is not 1 or 2 or 3')
			else:
				print(str(ask_float) + ' is not an integer')
		else:
			print(ask + ' is not a number')
	
			
	print(bound + '\n' + end + '\n' + bound)

	return 0
	
if __name__ == '__main__':
	sys.exit(main())