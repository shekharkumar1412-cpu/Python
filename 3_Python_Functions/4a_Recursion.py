# The Python interpreter limits the depths of recursion to help avoid infinite recursions,
# resulting in stack overflows.

# By default, the maximum depth of recursion is 1000. 
# If the limit is crossed, it results in RecursionError. 



# Let's look at one such condition.

def recursor():
    recursor() # recursive call of function


# function call
recursor()