#Ask for the total price of the bill, then ask how many diners there are. 
#Divide the total bill by the number of diners and show how much each person must pay.

billAmount = int(input('Enter total price of the bill'))
dinerNumber = int(input('Enter the number of diners'))

print('Each individual will pay', billAmount/dinerNumber)

