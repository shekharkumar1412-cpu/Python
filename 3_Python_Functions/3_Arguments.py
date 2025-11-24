# Function Argument with Default Values

def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)
add_numbers(b = 2)

# function call with no arguments
add_numbers()



            # Python Keyword Argument

def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

 # Here the position of arguments doesn't matter.
 # first_name in the function call is assigned to 
 # first_name in the function definition.
display_info(last_name = 'Cartman', first_name = 'Eric')