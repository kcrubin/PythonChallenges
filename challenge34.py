#Display the following message:
#1) Square
#2) Triangle
#Enter a number :
#If the user enters 1, then it should ask them for the length of one of its sides and display the
#area. If they select 2, it should ask for the base and height of the triangle and display the area. 
# If they type in anything else, it should give them a suitable error message.

print('1) Square\n 2) Triangle')
value = int(input('Enter a number: '))

if value==1:
    length = int(input('Enter the lenhth of the square'))
    print('Area: ',length*length)
elif value==2:
    base = int(input('Enter the base of the triangle'))
    height = int(input('Enter the height of the triangle'))
    print('Area: ',0.5*base*height)
else:
    print('wrong input')