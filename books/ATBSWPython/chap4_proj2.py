#!/usr/bin/python
import sys

def printTransposedImage(x):
	# loop over columns
	for i in range(len(x[0])):
		tmp = ''
		# loop over rows
		for j in range(len(x)):
			tmp += x[j][i]
		print(tmp)

def printRawImage(x):
	# loop over rows
	for i in range(len(x)):
		tmp = ''
		# loop over columns
		for j in range(len(x[0])):
			tmp += x[i][j]
		print(tmp)

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')

	grid = [ ['.', '.', '.', '.', '.', '.'],
			 ['.', '0', '0', '.', '.', '.'],
			 ['0', '0', '0', '0', '.', '.'],
			 ['0', '0', '0', '0', '0', '.'],
			 ['.', '0', '0', '0', '0', '0'],
			 ['0', '0', '0', '0', '0', '.'],
			 ['0', '0', '0', '0', '.', '.'],
			 ['.', '0', '0', '.', '.', '.'],
			 ['.', '.', '.', '.', '.', '.']]
			 
	print('=======================')
	print('====== RAW IMAGE ======')
	print('=======================')
	printRawImage(grid)
	print('=======================')
	print('==== INVERSE IMAGE ====')
	print('=======================')
	printTransposedImage(grid)
	
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())