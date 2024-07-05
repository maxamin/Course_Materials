# import will load up a module for use to use inside of this source files
from CheckingAccount import CheckingAccount

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():


	# We will now create a Person instance of the Person Class to be used
	# Since the constructor requires the name of the ccount and the starting amount we must provide them upon creation
	checking_account = CheckingAccount('Brandon', 500)
	print('Type of Account: {0}\n'.format(checking_account.getTypeOfAccount()))


	# Now we want to make a deposit
	print('Starting Cash: {0}'.format(checking_account.getAmount()))
	print('Withdrawling $250...')
	checking_account.withdraw(250)
	print('Balance Cash: {0}\n'.format(checking_account.getAmount()))

	# Now lets deposit
	print('Depositing $2500...')
	checking_account.deposit(2500)
	print('Balance Cash: {0}\n'.format(checking_account.getAmount()))


	# Now lets create another checking Account object and print the stats to see how the objects are different
	print('Creating new Checking account and withdrawing $900')
	checking_account2 = CheckingAccount('John', 500)
	checking_account2.withdraw(900)
	print('\nPrinting checking_account1\n{0}'.format(checking_account.getStats()))
	print('\nPrinting checking_account2\n{0}'.format(checking_account2.getStats()))


# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()