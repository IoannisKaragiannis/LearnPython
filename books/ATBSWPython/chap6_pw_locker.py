#!/usr/bin/python
# {}.py - An insecure password locker program
import sys, pyperclip

# global dictionary
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

def main():
	bound = ''.ljust(40, '*')
	start = ' [ STARTED ] '.center(40, '*')
	end = ' [ FINISHED ] '.center(40, '*')
	print(bound + '\n' + start + '\n' + bound)

	if len(sys.argv) < 2:
		print('Usage: python ' + str(sys.argv[0]) + ' [account] - copy account password')
		sys.exit()
	
	account = sys.argv[1] # first command linearg is the account name
	
	if account in PASSWORDS:
		pyperclip.copy(PASSWORDS[account])
		print('Password for ' + account + ' copied to clipboard')
	else:
		print('There is no account named ' + account)
	
	print(bound + '\n' + end + '\n' + bound)
	return 0
	
if __name__ == '__main__':
	sys.exit(main())