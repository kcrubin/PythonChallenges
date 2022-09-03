#Ask for the radius and the depth of a cylinder
#and work out the total volume (circle
#area*depth) rounded to three decimal
#places.

import math
radius = int(input('Enter the radius of cylinder '))
depth = int(input('Enter the depth '))

volume = math.pi*(radius**2)*depth
print(volume)