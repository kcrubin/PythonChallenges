#Ask the user to enter their first name and then ask them to
#enter their surname. Join them together with a space between
#and display the name and the length of whole name.

fName = input('Enter your first name')
lName = input('Enter your last name')

fullName = fName+lName
print('Length of the name is',len(fullName))
