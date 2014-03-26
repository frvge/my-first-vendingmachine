import sys
import unittest
from vendingmachine import VendingMachine

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

	def test_getAmount(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'amount': 1}, {'name': 'fanta', 'amount': 3}],
			[{'name': 'fristi', 'amount': 2}, {'name': 'sprite', 'amount': 4}]
		]
		vm.setInventory(inventory)
		expected = 1
		self.assertEquals(vm.getAmount(1, 1), expected)
		expected = 4
		self.assertEquals(vm.getAmount(2, 2), expected)

	def test_hasPaidEnough(self):
		vm = VendingMachine()
		inventory = [
			[{'name': 'cola', 'amount': 1}, {'name': 'fanta', 'price': 3}],
			[{'name': 'fristi', 'amount': 2}, {'name': 'sprite', 'price': 4}]
		]
		vm.setInventory(inventory)
		vm._VendingMachine__money = 1;
		self.assertTrue(vm.hasPaidEnough(1, 1))
		self.assertFalse(vm.hasPaidEnough(1, 2))

 
if __name__ == "__main__":
	unittest.main()
























