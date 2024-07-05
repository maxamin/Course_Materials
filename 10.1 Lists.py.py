

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# Creates an empty list
	tmp_list = list()

	# Another way to create a list
	tmp_list = ['Brandon', 26, 'RedTeam Nation']

	# To access a value in a dict we provide it's index
	print('My Name is {0} and I am {1} years old.'.format(tmp_list[0], tmp_list[1]))

	# What if we want to overwrite the age to be 27?
	tmp_list[1] = 27
	print('My Name is {0} and I am {1} years old.'.format(tmp_list[0], tmp_list[1]))

	# If we want to add something new to the list we do the following
	tmp_list.append(3)
	print('Element: {0}'.format(tmp_list[3]))

	# We want to see if a value exists in a list
	if 'Brandon' in tmp_list:
		print('\nBrandon is inside the list!')


	# Now lets delete the Bored element
	print('\nList before delete: {0}'.format(tmp_list))
	tmp_list.remove(3)
	print('List after delete: {0}'.format(tmp_list))

	# What if we need to loop through the data?
	# There are a few ways to do this

	# Print all values
	print('\nPrinting List')
	for x in tmp_list:
		print(x)

	# If we want to access the element by its index through a list
	print('\nPrinting list with index')
	for i in range(len(tmp_list)):
		print(tmp_list[i])





# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()