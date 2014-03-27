import sys

class VendingMachineException(Exception): pass
class NotEnoughMoneyException(VendingMachineException): pass
class OutOfStockException(VendingMachineException): pass

class VendingMachine:
	def __init__(self):
		self.__inventory = [[]]
		self.__money = 0

	def getInventory(self):
		return self.__inventory

	def setInventory(self, inventory):
		self.__inventory = inventory

	def inputMoney(self, money):
		self.__money += money
		return self.__money

	def getItem(self, row, col):
		return self.__inventory[row - 1][col - 1]

	def getPrice(self, row, col):
		return self.getItem(row, col)['price']

	def getStock(self, row, col):
		return self.getItem(row, col)['stock']

	def inStock(self, row, col):
		return self.getStock(row, col) > 0

	def hasPaidEnough(self, row, col):
		return self.__money >= self.getPrice(row, col)

	def deliverItem(self, row, col):
		if self.getStock(row, col) < 1:
			raise OutOfStockException()
		if self.getPrice(row, col) > self.__money:
			raise NotEnoughMoneyException()

		# everything OK
		self.__money -= self.getPrice(row, col)
		self.__inventory[row - 1][col - 1]['stock'] = self.getStock(row, col) - 1
		return self.getItem(row, col)['name']


if __name__ == "__main__":
	vm = VendingMachine()

