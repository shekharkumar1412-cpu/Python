# In  Python, 'is' and 'is not' are used to check if two values are located on the same part of the memory. 
# Two variables that are equal does not imply that they are identical.

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False (as x1 and y1 are same as well as identical)

print(x2 is y2)  # prints True (as x2 and y2 are same and identical too)

print(x3 is y3)  # prints False(as x3 and y3 are list They are equal but not identical. 
                    # It is because the interpreter locates them separately in memory although they are equal.