# In Python, a lambda function is a special type of function without the function name.

# Syntax to declare lambda function:
#    lambda argument(s) : expression 

 
                # Example1: Python lambda Function

# declare a lambda function
greet = lambda : print('Hello World')

# call lambda function
greet()                         # Output: Hello World




                #  Example2 :Python lambda Function with an Argument

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)
     # Here, name after the lambda keyword specifies that the lambda function accepts the argument named name.



# lambda call
greet_user('Shekhar')       # Output: Hey there, Shekhar
                # Here, we have passed a string value 'Shekhar' to our lambda function.

