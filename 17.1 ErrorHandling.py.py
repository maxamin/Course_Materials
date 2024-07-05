
# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# The basics of error handling is a try except
	# its important to understand when to fail and when to silently continue when an error occurs

	# We want to tell the user something happened if we try to access a key in a dict that does not exist but we
	# Dont want to halt the application as we can default the result to None
	tmp_dict = {'Name': 'Brandon', 'Age': 26}
	try:
		result = tmp_dict['Does Not Exist']
	except KeyError as e:
		result = None

	print('Result of Dict Check: {0}'.format(result))


	# Now if we are doing type conversion this may not have a fall back and we want to let the user know!
	tmp_str = 'RedTeam Nation'
	try:
		tmp_digit = int(tmp_str)

	# Note that here we use Exception. This will catch any type of Excepton.
	# In our previous example we are only catching a single type
	except Exception as e:
		print(e)



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()