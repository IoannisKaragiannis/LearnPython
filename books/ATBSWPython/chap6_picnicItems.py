#!/usr/bin/python
import sys
		
def my_printPicNic(itemsDict):
	# find max size of keys and values
	max_key = -1
	max_value = -1
	for k, v in itemsDict.items():
		if len(k) > max_key:
			max_key = len(k)
		if len(str(v)) > max_value:
			max_value = len(str(v))
	l_width = max_key + 2
	r_width = max_value + 2
	print(''.center(l_width + r_width + 1, '-'))
	print('| PICNIC ITEMS |'.center(l_width + r_width + 1, '-'))
	print(''.center(l_width + r_width + 1, '-'))
	for k, v in itemsDict.items():
		print(k.ljust(l_width, '.') + str(v).rjust(r_width))
 

def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)

	picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000,
	'chocolates': 2, 'ice-cream': 1, 'beers': 20, 'coke': 2,
	'bottles-of-water': 4, 'candles': 2, 'books': 1, 'bluetooth-speaker': 1}

	my_printPicNic(picnicItems)
	
	print(bound + '\n' + end + '\n' + bound)
	return 0
	
if __name__ == '__main__':
	sys.exit(main())