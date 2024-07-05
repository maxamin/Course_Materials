

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# The number 5 as a string
	sample_digit = '5'

	# print out the type
	print('sample_digit is type: {0}'.format(type(sample_digit)))

	# We are now casting the digit as an int fomr a str
	sample_digit_2 = int(sample_digit)

	# print out the type
	print('sample_digit_2 is type: {0}'.format(type(sample_digit_2)))


	# Setting the type from int to str
	sample_digit_3 = str(sample_digit_2)

	# print out the type
	print('sample_digit_3 is type: {0}'.format(type(sample_digit_3)))



	# This will produce an error when 2 types are trying to be combined
	print(5 + sample_digit)


# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()