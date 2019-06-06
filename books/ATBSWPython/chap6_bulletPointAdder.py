#!/usr/bin/python
# {}.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
import sys, pyperclip


def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)

	text = pyperclip.paste()
	
	# Separate lines and add stars
	lines = text.split('\n')
	for i in range(len(lines)):
		lines[i] = '* ' + lines[i]

	text = '\n'.join(lines)
	pyperclip.copy(text)
	
	print('Modified text is stored in the clipboard')
	
	print(bound + '\n' + end + '\n' + bound)
	return 0
	
if __name__ == '__main__':
	sys.exit(main())