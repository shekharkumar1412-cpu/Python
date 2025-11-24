# In Python, nonlocal variables are used in nested functions whose local scope is not defined. \
# This means that the variable can be neither in the local nor the global scope.

# We use the nonlocal keyword to create nonlocal variables.
# Any change in the value of nonlocal variables leads to the change in the value of the local variables


# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal variable'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()   #  output is: inner: nonlocal variable
#                      outer: nonlocal variable


