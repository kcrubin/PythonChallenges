#Ask how many slices of pizza the user started with and ask how many slices they have eaten.
#Work out how many slices they have left and display the answer in a userfriendly format.

from turtle import left


totalSlices = int(input('Enter the total slices of Pizza that you have '))
eatenSlices = int(input('Enter the eatan number of Slices '))

leftSlices = totalSlices - eatenSlices

print('You have ',leftSlices,' slices left.')