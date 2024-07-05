
# This defines a class using the Class keyword followed by the name of the Class
# The name of the Class is often the same as the name of the file
class Account():

	# __init__ is refered to as the constructor
	# The constructor is first ran when the object or instance of the object is create
	def __init__(self, name_of_account, amount):
		# Self is used to refer to this instance of the object.
		self.name_of_account = name_of_account
		self.amount = amount

	# We must pass self to any function inside of a class that we want to use

	def setAmount(self, amount):
		self.amount = amount

	def getAmount(self):
		return self.amount


	def withdraw(self, amount):
		# We dont want the mount to be withdrawn if we are already at 0 or less
		if(self.amount <= 0):
			return

		self.amount -= amount

	def deposit(self, amount):
		self.amount += amount



	def getStats(self):
		return 'Name: {0}\nAge: {1}\nTitle: {2}'.format(self.name, self.age, self.title)
