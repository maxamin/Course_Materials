

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():

	# Print uses the standard python libraries to print the string to the screen
	# Note this is followed by a new line or \n
	print('Hello World!')


# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()