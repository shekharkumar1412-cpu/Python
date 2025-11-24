# Recursion is the process of defining something in terms of itself.
# Every recursive function must have a base condition that stops the 
    #        recursion or else the function calls itself infinitely.




#  A program to calculate the factorial of a number using for loop
def fac(N):
        res=1
        for i in range(1,N+1):
            res*=i
        return res

n=int(input("Enter the number for which you want to find the factorial:"))
print("Using for loop The factorial of {} is:".format(n),fac(n))



        #  A program to calculate factorial using recursion function

def factorial (Numn):
    if(Numn==1):
        return 1

    else:
        return Numn*factorial(Numn-1)

num=int(input("enter a number:"))
print("using recursion Factorial of {} is:".format(num),factorial(num))