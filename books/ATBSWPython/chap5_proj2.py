#!/usr/bin/python
import sys

def displayInventory(inventory):
	print('Inventory:')
	item_total = 0
	for k,v in inventory.items():
		print(str(v)+' '+str(k))
		item_total += v
	print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
	for item in addedItems:
		if item not in inventory.keys():
			inventory[item] = 1
		else:
			inventory[item] += 1
	return inventory

def main():
	print('***************************************')
	print('************ [ STARTED ] **************')
	print('***************************************')

	inv = {'gold coin': 42, 'rope': 1}
	dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
	inv = addToInventory(inv, dragonLoot)
	displayInventory(inv)
	
	print('***************************************')
	print('************ [ FINISHED ] *************')
	print('***************************************')
	return 0
	
if __name__ == '__main__':
	sys.exit(main())