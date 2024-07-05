

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():

	# String
	# A String will hold text
	sample_string = "RedTeam Nation Rocks! - 01"

	# Integer
	# This is a digit
	sample_int = 4444

	# Float
	# This is a decimal number
	sample_float = 3.14

	# Boolean
	# This handles if something is True or False
	sample_bool = True

	# None
	# This is a defualt value of a variable. Commonly used for when something is not set by the user or an error occured
	sample_none = None


	# This will subsitute variable(s) into a string with the .format function
	#                                                                                                {0}				 {1}         {2}      {3}
	print('Sample Print with .Format\nString: {0}\nInteger: {1}\nFloat: {2}\nBoolean: {3}'.format(sample_string, sample_int, sample_float, sample_bool))



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()