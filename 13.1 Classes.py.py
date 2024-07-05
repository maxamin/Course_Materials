# import will load up a module for use to use inside of this source files
from Person import Person

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# We will now create a Person instance of the Person Class to be used
	# Since the constructor requires the name and age we must provide them upon creation
	person = Person('Brandon', 26)

	# Now we want to set their title with the setTitle function
	person.setTitle('CEO')

	# We can now issue out getTitle funtion on that class and see what it was set to
	print('Title: {0}'.format(person.getTitle()))

	# Now lets print the name, age and where they work!
	# This can be done quickly based on the function we created!
	print('\nPrinting Stats')
	print(person.getStats())


	# Now lets create another person object and print the stats to see how the objects are different
	person2 = Person('John', 32)
	person2.setTitle('CISO')
	print('\nPrinting Person1\n{0}'.format(person.getStats()))
	print('\nPrinting Person2\n{0}'.format(person2.getStats()))


# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()