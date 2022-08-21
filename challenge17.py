#Ask the user’s age. If they are 18 or over, display the
#message “You can vote”, if they are aged 17, 
#display the message “You can learn to drive”, if they are 16, display
#the message “You can buy a lottery ticket”, if they are under 16, display the
#message “You can go Trickor-Treating”.

age = int(input('Enter the age'))

if age>=18:
    print('you can vote')
if age>=17:
    print('you can drive')
if age>=16:
    print('you can buy lottery ticket')
if age<16:
    print('you can go Trickor-treating')