
##way 01
##direct call math module
# import math

# print(math.sqrt(64))
# print(math.sin(math.radians(180)))

## way 02
## you can rename the module name

# import math as mm

# print(mm.sin(mm.radians(0)))
# print(mm.sqrt(64))

##way 03
## call some function from math module
# from math import sqrt, pow

# print(sqrt(9))
# print(pow(20, 2))


##way 04
## * for universal selector, call all the function
# from math import *
# print(sqrt(25))
# print(sin(radians(90)))