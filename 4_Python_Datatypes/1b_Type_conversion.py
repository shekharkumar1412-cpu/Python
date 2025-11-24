# Operations like addition, subtraction 
# convert integers to float implicitly (automatically), if one of the operands is float.

print(1 + 2.0)     # prints 3.0 (here int (1) and float(2.0) are added thats why our result is in float)

# Explicit Type Conversion using built_in functions

#  functions like int(), float() and complex() converts between types explicitly. 
# These functions can even convert from strings.

num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3) # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)
