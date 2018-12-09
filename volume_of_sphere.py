# This script calculates the volume of a sphere and print it  to the screen

import math

# d = float(input("Specify the diamiter of the sphere which you want to calculate the volume: "))

# in_file = open('input_diameter.txt') --> this make just the file ready to be read 
# d = in_file.read() --> this read the txt file '10\n' and save it in d
# d = float(d)

r = d/2
volume = 4.0/3*math.pi*math.pow(r,3)
print("Volume of the sphere is: %f" %(round(volume, 3)))


