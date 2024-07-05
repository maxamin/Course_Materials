# import will load up a module for use to use inside of this source files
import logging

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# We first need to init the basic config of the logger
	# We will set the name of the file
	logging.basicConfig(filename='logger.log')

	# Make a reference of the logger directly
	logger = logging.getLogger()

	# Set the log level to INFO
	logger.setLevel(logging.INFO)

	# There are different log levels.
	# Each log level will only log the value in specific wasy
	# Because log level is INFO this will not be logged
	logger.debug('This is a debug message')

	# This will be logged
	logger.info('This is a info message')

	# If we change the log level to debug we can now see info an debug
	logger.setLevel(logging.DEBUG)
	logger.debug('This debug will make it!')
	logger.info('This info will make it as well!')


	# Set the log level to INFO
	logger.setLevel(logging.INFO)

	# Critical and Error will always show up!
	logger.critical('This is a critical message')
	logger.error('This is an error message')



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()