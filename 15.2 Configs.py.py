# import will load up a module for use to use inside of this source files
import ConfigParser

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# First we need to create a config parser object
	config = ConfigParser.ConfigParser()

	# Next we read in our config.ini file
	config.read('config.ini')

	# We can see what sections we have in the config file
	print('Config File Sections AKA inside the []: {0}'.format(config.sections()))

	# To get the value of something we need to know its name and section
	# Lets get the name, age and company
	print('Name from config.ini: {0}'.format(config.get('general', 'Name')))
	print('Age from config.ini: {0}'.format(config.get('general', 'Age')))
	print('Company from config.ini: {0}'.format(config.get('general', 'Company')))

	# Lets also Grab secretid!
	print('secretid from config.ini: {0}'.format(config.get('secret', 'secretid')))



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()