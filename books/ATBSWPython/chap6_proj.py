#!/usr/bin/python
# {}.py - Program that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified.

import sys, math

def isTableValid(data):
	max = 0
	min = math.inf
	for row in range(len(data)):
		if len(data[row]) > max:
			max = len(data[row])
		if len(data[row]) < min:
			min = len(data[row])
	if min == max:
		return True
	else:
		return False

def printTable(data):
	if isTableValid(data):
		rows = len(data)
		cols = len(data[0])
		colWidths = [0] * rows
		totalRowLength = [0] * cols
		
		for i in range(rows):
			colWidths[i] = len(max(data[i], key = len))
			print('longest string = ' + str(colWidths[i]))
		
		for j in range(cols):
			for i in range(rows):
				totalRowLength[j] += len(' ' + data[i][j].rjust(colWidths[i])+'|')
		
		print(''.center(max(totalRowLength)+1, '-'))	
		for j in range(cols):
			tmp = '|'
			for i in range(rows):
				tmp += ' ' + data[i][j].rjust(colWidths[i])+'|'
			print(tmp)
		print(''.center(max(totalRowLength) +  1, '-'))
	else:
		print('The inner lists of the table do not contain the same number of strings')
	return 0
 

def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)

	tableData = [['red-apples', 'oranges', 'cherries', 'banana'],
				['Big-Alice', 'Bob-Marley', 'Charles-Dickens', 'David-Bowie'],
				['dogs', 'cats', 'moose', 'goose']]
	
	printTable(tableData)
		
	print(bound + '\n' + end + '\n' + bound)
	return 0
	
if __name__ == '__main__':
	sys.exit(main())