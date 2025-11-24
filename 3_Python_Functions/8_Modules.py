# Module is a file that contains code to perform a specific task.
# A module may contain variables, functions, classes etc.


# We can import the definitions inside a module to 
# another module or the interactive interpreter in Python using the keyword import
# similar to the constant.py and main.py





# importing math module in our current file to use the names defined in that  module 
# this imports all the names of the math module
import math
print('square root of 64 is:',math.sqrt(64) ) # accesing the sqrt function from math module using dot operator



# importing math module with renaming as m

import math as m
print("The value of pi is",m.pi)

# importing specific names from a module

from math import pi,sin,sqrt
value=sin(pi/2)
print('square root :',sqrt(4*value))



# importing everything from a module using asterik(*) 

from math import *
print("value:",sin(pi/2))
