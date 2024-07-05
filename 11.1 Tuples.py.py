

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# Create a tuple
	tmp_tuple = ('Brandon', 26, 'RedTeam Nation')

	# To access a value in a dict we provide it's index
	print('My Name is {0} and I am {1} years old.'.format(tmp_tuple[0], tmp_tuple[1]))

	# Tuples are immutable
	# You cannot delete or add to them once they are created

	# We want to see if a value exists in a list
	if 'Brandon' in tmp_tuple:
		print('\nBrandon is inside the list!')

	# What if we need to loop through the data?
	# There are a few ways to do this

	# Print all of the values
	print('\nPrinting List')
	for x in tmp_tuple:
		print(x)

	# If we want to access the element by its index through a tuple
	print('\nPrinting list with index')
	for i in range(len(tmp_tuple)):
		print(tmp_tuple[i])





# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()