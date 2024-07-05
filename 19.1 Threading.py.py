import time
from threading import Thread


def threaded(thread_id):
	print('Thread ID {0} In Waiting State'.format(thread_id))

	# Sleeps for 2 seconds
	time.sleep(2)

	print('Thread ID: {0} Finished'.format(thread_id))


# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():

	# Loop through and start a new thread
	for i in range(5):

		# Create a new thread object
		thread = Thread(target=threaded, args=(i,))

		# Start the thread and fork it
		thread.start()


# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()