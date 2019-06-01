#!/usr/bin/python
import sys

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkForWinner(board):
	# winning combinations
	winner = ''
	win_comb = []
	win_comb.append(board['top-L'] + board['top-M'] + board['top-R'])
	win_comb.append(board['mid-L'] + board['mid-M'] + board['mid-R'])
	win_comb.append(board['low-L'] + board['low-M'] + board['low-R'])
	win_comb.append(board['top-L'] + board['mid-L'] + board['low-L'])
	win_comb.append(board['top-M'] + board['mid-M'] + board['low-M'])
	win_comb.append(board['top-R'] + board['mid-R'] + board['low-R'])
	win_comb.append(board['top-L'] + board['mid-M'] + board['low-R'])
	win_comb.append(board['low-L'] + board['mid-M'] + board['top-R'])
	
	for i in range(len(win_comb)):
		if win_comb[i] == 'XXX':
			winner = 'X'
			break
		if win_comb[i] == 'OOO':
			break
			winner = 'O'
	return winner

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')

	theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
				'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
				'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
	
	turn = 'X'
	for i in range(9):
		printBoard(theBoard)
		if checkForWinner(theBoard) != '':
			print(checkForWinner(theBoard)+' is the winner')
			break
		move = input('Turn for ' + turn + '. Move on which space? \n')
		while move not in theBoard.keys() or theBoard[move] != ' ':
			move = input('Wrong input: Turn for ' + turn + ' again. \n')
		theBoard[move] = turn
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
	
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())