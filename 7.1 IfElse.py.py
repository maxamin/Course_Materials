

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# Setup some variables
	age = 26
	name = 'Brandon'
	male = True
	female = False


	# Check if our name is Brandon
	# It will check to see if the string 'Brandon' is inside of the main string
	# if we set name = 'Brandon test' it will still work correctly
	if ('Brandon' in name):
		print('My name is: {0}'.format(name))


	# if we want to check for something specifically we can use the == sign
	if ('Brandon' == name):
		print('Specific: My name is: {0}'.format(name))


	# This can be done with Numbers as well!
	# When an if statement fails it will continue, however, you can add an else at the end as a fall back
	# To make sure some logic happens!
	if (age == 25):
		print('Since im not 26 this wont print!')
	else:
		print('I may not be 25 but I am {0}!'.format(age))


	# We can even look and see if number are greater than or less than each other!
	# Notice we can join arguments in the same if statement
	# With and both evaluations must be True
	if(age >= 21 and age <= 30):
		print('Check their ID!!!!!')


	# We can do something similar with the keyword or instead of and!
	if(age > 21 or 'Brandon' == name):
		print('It is {0}! We do not need to check his ID!'.format(name))



	# We can use if statements with booleans as well!
	# In this case male is True that means the evaluation is true for the if then we continue
	if (male):
		print('Male is {0}'.format(male))


	# We can now check the opposite
	# Not will be the inverse of the value. Normally if will try to evaluate to true
	# In this case we are saying we are looking for a value of False!
	# This can also be done with ==
	# EX: if(female == False)
	if(not female):
		print('I am not female!')


	# These were just standard If and If else
	# We have the ability to combine another if into the else section of the code to continue it further!
	if(age <= 21):
		print('Under Age!')
	elif(age >= 21):
		print('Of Age!')


# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()