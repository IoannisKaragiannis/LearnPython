#!/usr/bin/python
import sys

def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k,v in inventory.items():
		print(str(v)+' '+str(k))
		item_total += v
	print('Total number of items: ' + str(item_total))

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')

	stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
	displayInventory(stuff)
	
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())