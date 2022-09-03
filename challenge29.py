#Ask the user to enter an integer that is over 500. Work
#out the square root of that number and display it to two
#decimal places.
import math
userInput = int(input('Enter an integer over 500'))
sqrdNum = math.sqrt(userInput)
print(round(sqrdNum,2))
