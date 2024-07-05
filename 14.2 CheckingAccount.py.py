from Account import Account


# This defines a class using the Class keyword followed by the name of the Class
# The name of the Class is often the same as the name of the file
class CheckingAccount(Account):

	# __init__ is refered to as the constructor
	# The constructor is first ran when the object or instance of the object is create
	def __init__(self, name_of_account, amount):
		# Self is used to refer to this instance of the object.
		Account.__init__(self, name_of_account, amount)
		self.type_of_account = 'Checking'

	# We must pass self to any function inside of a class that we want to use

	def getTypeOfAccount(self):
		return self.type_of_account


	def getStats(self):
		return 'Name of Account: {0}\nType Of Account: {1}\nBalance: ${2}'.format(self.name_of_account, self.type_of_account, self.amount)

