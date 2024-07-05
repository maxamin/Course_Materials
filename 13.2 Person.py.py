
# This defines a class using the Class keyword followed by the name of the Class
# The name of the Class is often the same as the name of the file
class Person():

	# __init__ is refered to as the constructor
	# The constructor is first ran when the object or instance of the object is create
	# Such as with person = Person(What is in here is below!)
	def __init__(self, name, age):
		# Self is used to refer to this instance of the object.
		# We can have a lot of person objects but the age, name and title will be attached to their own instance
		self.age = age
		self.name = name
		self.title = ''

	# We must pass self to any function inside of a class that we want to use

	def setTitle(self, title):
		self.title = title

	def getTitle(self):
		return self.title


	def getStats(self):
		return 'Name: {0}\nAge: {1}\nTitle: {2}'.format(self.name, self.age, self.title)
