import socket

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():

	# First we need to create a socket obect
	sock = socket.socket()

	# We then get the local hosts name
	host = socket.gethostname()

	# We now set the port we will be using
	port = 4444

	# Next we need to bind the port and reserve it on the system
	sock.bind((host, port))

	# We will now listen for any connection with a max of 5 
	sock.listen(5)

	print('Starting Server!')

	# We now run the while loop to consistantly check for connections and send back a response
	while True:

		# Establish a connection with the client
		client, address = sock.accept()

		print('Connection From {0}'.format(address))

		# We now send data over to the client
		client.send('Recieved a connection! Closing!')

		# We now close the connection
		client.close()




# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()