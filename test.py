import sys
import unittest
from vendingmachine import VendingMachine, NotEnoughMoneyException, OutOfStockException



class TestVendingMachine(unittest.TestCase):
	def test_exists(self):
		vm = 3
		self.assertNotIsInstance(vm, VendingMachine)
		vm = VendingMachine()
		self.assertIsInstance(vm, VendingMachine)

	def test_getInventory(self):
		vm = VendingMachine()

		expected = [1, 2, 3]
		self.assertNotEquals(vm.getInventory(), expected)

		expected = [[]]
		self.assertEquals(vm.getInventory(), expected)

		vm._VendingMachine__inventory = [
			[{'name' : 'cola'}, {'name': 'fanta'}],
			[{'name': 'sprite'}, {'name': 'applejuice'}]
		]

		expected = [
			[{'name' : 'cola'}, {'name': 'fanta'}],
			[{'name': 'sprite'}, {'name': 'applejuice'}]
		]

		self.assertEquals(vm.getInventory(), expected)

	def test_setInventory(self):
		vm = VendingMachine()

		expected = ['a']
		vm.setInventory(expected)
		self.assertEquals(vm.getInventory(), expected)

		expected = [
			[{'name' : 'cola'}, {'name': 'fanta'}],
			[{'name': 'sprite'}, {'name': 'applejuice'}]
		]
		vm.setInventory(expected)
		self.assertEquals(vm.getInventory(), expected)

	def test_getMoney(self):
		vm = VendingMachine()
		expected = 3
		self.assertEquals(vm.inputMoney(3), expected)
		expected = 6
		self.assertEquals(vm.inputMoney(3), expected)

	def test_getItem(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'price': 1}, {'name': 'fanta', 'price': 3}],
			[{'name': 'fristi', 'price': 2}, {'name': 'sprite', 'price': 4}]
		]
		vm.setInventory(inventory)
		expected = {'name': 'fristi', 'price': 2}
		self.assertEquals(vm.getItem(2, 1), expected)
		expected = {'name': 'fanta', 'price': 3}
		self.assertEquals(vm.getItem(1, 2), expected)		


	def test_getPrice(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'price': 1}, {'name': 'fanta', 'price': 3}],
			[{'name': 'fristi', 'price': 2}, {'name': 'sprite', 'price': 4}]
		]
		vm.setInventory(inventory)
		expected = 1
		self.assertEquals(vm.getPrice(1, 1), expected)
		expected = 4
		self.assertEquals(vm.getPrice(2, 2), expected)

	def test_getStock(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'stock': 1}, {'name': 'fanta', 'stock': 3}],
			[{'name': 'fristi', 'stock': 2}, {'name': 'sprite', 'stock': 4}]
		]
		vm.setInventory(inventory)
		expected = 1
		self.assertEquals(vm.getStock(1, 1), expected)
		expected = 4
		self.assertEquals(vm.getStock(2, 2), expected)

	def test_hasPaidEnough(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'price': 1}, {'name': 'fanta', 'price': 3}],
			[{'name': 'fristi', 'price': 2}, {'name': 'sprite', 'price': 4}]
		]
		vm.setInventory(inventory)
		vm._VendingMachine__money = 1;
		self.assertTrue(vm.hasPaidEnough(1, 1))
		self.assertFalse(vm.hasPaidEnough(1, 2))

	def test_inStock(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'stock': 1}, {'name': 'fanta', 'stock': 3}],
			[{'name': 'fristi', 'stock': 0}, {'name': 'sprite', 'stock': 4}]
		]
		vm.setInventory(inventory)
		self.assertFalse(vm.inStock(2, 1))
		self.assertTrue(vm.inStock(2, 2))

	def test_deliverItem(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'stock': 1, 'price': 1}, {'name': 'fanta', 'stock': 3, 'price': 2}],
			[{'name': 'fristi', 'stock': 0, 'price': 1}, {'name': 'sprite', 'stock': 4, 'price': 4}]
		]
		vm.setInventory(inventory)

		self.assertRaises(OutOfStockException, vm.deliverItem, 2, 1)

		# can't deliver if you haven't inputted money
		self.assertRaises(NotEnoughMoneyException, vm.deliverItem, 1, 2)
		vm.inputMoney(1)
		self.assertRaises(NotEnoughMoneyException, vm.deliverItem, 1, 2)
		vm.inputMoney(1)
		# inputted money = 2, fanta price = 2
		self.assertEquals(vm.deliverItem(1, 2), 'fanta')

		self.assertRaises(NotEnoughMoneyException, vm.deliverItem, 1, 1)
		vm.inputMoney(6)
		# money = 6
		self.assertEquals(vm.deliverItem(2, 2), 'sprite')
		# money = 2
		self.assertEquals(vm.deliverItem(1, 1), 'cola')
		# money = 1, but cola is now out of stock
		self.assertRaises(OutOfStockException, vm.deliverItem, 1, 1)
 
if __name__ == "__main__":
	unittest.main()
























