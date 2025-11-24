# A function is a block of code that performs a specific task.

# syntax to declare a function 
    # def function_name(arguments):
                # function body 
                # return



def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
print()
print()



# function with two arguments and adding two numbers
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

# function call with two values
r=add_numbers(5, 4)
print('sum is:',r)





# A function to find the square of a number

def find_sq(num1):
    res=num1**2
    return res

n=int(input("Enter a number:"))
print("Square of {} is:".format(n),find_sq(n))