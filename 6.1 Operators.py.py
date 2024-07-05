

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():

	# Setting up the inital digit as 10
	tmp_int = 10

	# Print to show the value before we increment it
	print('tmp_int before tmp_int += 1: {0}'.format(tmp_int))

	# Takes the current value of tmp_int and adds the value after the = to it
	# Then it reassigns the new value into tmp_int
	tmp_int += 1

	# Print to show the value after we increment it
	print('tmp_int after tmp_int += 1: {0}'.format(tmp_int))


	# Takes the current value of tmp_int and subtracts the value after the = to it
	# Then it reassigns the new value into tmp_int
	tmp_int -= 1

	# Print to show the value after we decrement from it
	print('tmp_int after tmp_int -= 1: {0}'.format(tmp_int))


	# This can be done with any digit
	# Lets do it again but with 5 instead of 1

	# Print to show the value before we increment it
	print('tmp_int before tmp_int += 5: {0}'.format(tmp_int))

	# Takes the current value of tmp_int and adds the value after the = to it
	# Then it reassigns the new value into tmp_int
	tmp_int += 5

	# Print to show the value after we increment it
	print('tmp_int after tmp_int += 5: {0}'.format(tmp_int))


	# Takes the current value of tmp_int and subtracts the value after the = to it
	# Then it reassigns the new value into tmp_int
	tmp_int -= 5

	# Print to show the value after we decrement from it
	print('tmp_int after tmp_int -= 5: {0}\n'.format(tmp_int))

	
	# This can be done with multiplication * as well as division /

	# Takes the current value of tmp_int and divide the value after the = to it
	# Then it reassigns the new value into tmp_int
	tmp_int /= 2

	# Print to show the value after we divide from it
	print('tmp_int after tmp_int /= 2: {0}\n'.format(tmp_int))


	# Takes the current value of tmp_int and multiply the value after the = to it
	# Then it reassigns the new value into tmp_int
	tmp_int *= 2

	# Print to show the value after we multiply from it
	print('tmp_int after tmp_int *= 2: {0}\n'.format(tmp_int))

# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()