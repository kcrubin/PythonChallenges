#Ask the user to enter their first name and surname in lower
#case. Change the case to title case and join them together.
#Display the finished result.

fName = input('Enter the first name in lower case')
lName = input('Enter the last name in lower case')
print('Full name:',fName.title(),' ',lName.title())