#Ask for two numbers. If the first one is larger than the second, display the second number first
#and then the first number, otherwise show the first number first and then the second.

fNumber = int(input('Enter the first number'))
sNumber = int(input('Enter the second number'))

if fNumber > sNumber:
    print('Numbers are ',sNumber,',',fNumber)
else:
    print('Numbers are ',fNumber,',',sNumber)