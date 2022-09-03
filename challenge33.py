#Ask the user to enter two numbers. Use whole number division to divide
#the first number by the second and also work out the remainder and
#display the answer in a user-friendly way (e.g. if they enter 7 and 2 display
#“7 divided by 2 is 3 with 1 remaining”).

from math import remainder


num1 = int(input('Enter the first number'))
num2 = int(input('Enter the second number'))

output = num1//num2
remainder = num1%num2

print(num1,' divided by ',num2,' is ',output,' with ',remainder,' remaining.')