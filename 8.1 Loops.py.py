

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():



	# Set up the number of iterations to perform
	num = 10

	# Setup name for loop
	name = 'Red'

	# We want to loop through each letter in a string
	for x in name:
		print(x)


	# Get some space
	print('')

	# We want to now loop over a specific amount of times
	# Note that with machines counting always starts with 0 then goes up from there
	# So our original count of 10 based on num if we counted would be 1,2,3,etc but on a computer its 0,1,2,3,etc
	for x in range(num):
		print(x)

	# Get some space
	print('')

	# If we want to loop until we hit a specific reason to stop we use a while loop
	i = 0
	while(i < 10):
		print('i == {0}'.format(i))
		# Lets stop the loop when i hits 5
		if(i == 5):
			# Break will cancel the loop and resume normal execution
			print('Breaking out with i == 5')
			break

		# Make sure we increase i otherwise it will loop forever!
		i += 1

# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()