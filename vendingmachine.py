import sys

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
		return self.getItem(row, col).get('price')

	def getAmount(self, row, col):
		return self.getItem(row, col).get('amount')

	def hasPaidEnough(self, row, col):
		return self.__money >= self.getPrice(row, col)


if __name__ == "__main__":
	vm = VendingMachine()

