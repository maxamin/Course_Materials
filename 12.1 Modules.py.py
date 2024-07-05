# import will load up a module for use to use inside of this source files
import urllib2

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# Web Request
	# Accessing modules tends to be done with . notation
	# urlopen is a function or method inside of the class urllib2
	content = urllib2.urlopen('https://redteamnation.com')

	# .read() is a function inside of the urlopen object that is returned
	print(content.read())



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()