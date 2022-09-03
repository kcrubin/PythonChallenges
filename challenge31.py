#Ask the user to enter the radius of a circle
#(measurement from the centre point to the edge). Work
#out the area of the circle (π*radius2).
import math
radius = int(input('Enter the radius of circle'))
piNum = math.pi
print('Area: ',round(piNum*(radius**2),4))