

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# Creates an empty dictionary
	tmp_dict = dict()

	# Another way to create a dict
	tmp_dict = dict(name='Brandon', age=26, male=True)

	# Creates a dictonary with values
	# Each element in a dict has a key and value pair
	# The keys are name.age,male
	# Values are after the :
	tmp_dict2 = {
		'Name': 'Brandon',
		'Age': 26,
		'Male': True
	}

	# To access a value in a dict we provide it's key
	print('My Name is {0} and I am {1} years old.'.format(tmp_dict2['Name'], tmp_dict2['Age']))

	# What if we want to overwrite the age to be 27?
	tmp_dict2['Age'] = 27
	print('My Name is {0} and I am {1} years old.'.format(tmp_dict2['Name'], tmp_dict2['Age']))

	# If we want to add something new to the dict we do the following
	tmp_dict2['Bored'] = False
	print('Bored: {0}'.format(tmp_dict2['Bored']))

	# We want to see if a key exists in a dict
	if 'Age' in tmp_dict2:
		print('\nAge is inside the dict!')


	# Now lets delete the Bored Key
	print('\nDict before delete: {0}'.format(tmp_dict2))
	tmp_dict2.pop('Bored')
	print('Dict after delete: {0}'.format(tmp_dict2))

	# What if we need to loop through the data?
	# There are a few ways to do this

	# Print all Keys and their values
	print('\nPrinting Keys Only')
	for x in tmp_dict2:
		print('Key: {0} - Value: {1}'.format(x, tmp_dict2[x]))

	# Print all the values NO Key
	print('\nPrinting just Values')
	for x in tmp_dict2.values():
		print(x)

	# Print the keys and values but in seperate variables
	print('\nPrinting Keys and Values in Seperate Vars')
	for key, value in tmp_dict2.items():
		print('Key: {0} - Value: {1}'.format(key, value))




# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()