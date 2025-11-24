# In python global keyword is used to read or declare a global variable inside a function
# It is used to create a global variable and make changes to the variable in a local context.

#  global variable
c = 1 

def add():
    global c
     # increment c by 2
    c = c + 2

    print(c)

add()   




                    # Global in Nested Functions

def outer_function():
    num = 20

    def inner_function():
        global num
        num = 25
    
    print("Before calling inner_function(): ", num)    # o/p: 20
    inner_function()
    print("After calling inner_function(): ", num)     # o/p: 20

outer_function()
print("Outside both function: ", num)      # o/p: 25 (global variable inside inner function
                                           #             is declared which is used here)