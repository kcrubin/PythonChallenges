#Task the user to enter a number over 100 and then 
#enter a number under 10 and 
#tell them how many times the smaller number goes into the larger number in a user-friendly format.

largeNumber = int(input('Enter a number over 100 '))
smallNumber = int(input('Enter a number under 10'))

print(largeNumber,' goes into ',int(largeNumber//smallNumber),' times than that of ',smallNumber)