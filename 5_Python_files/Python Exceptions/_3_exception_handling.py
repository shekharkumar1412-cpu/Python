print("--------------------Example 1-----------------------------")
try:
    even=[2,4,6]
    print(even[6])          # Here index is 6 which doesn't exist for list even error occurs all lines 
                                # below this will be skipped and it will go to except block
    num=22
    deno=0
    res=num/deno
    print(res)

except IndexError:              # no of exception block can be zero more than 0
    print("Index Out of Bound.")

except ZeroDivisionError:
    print("Error: denominator can't be zero")

finally:
    print("This block get executed whether there is a exception in try or no exception in try block")
    print("==========================================================================================")

# -----------------------------------------------------------------------------------------------


# else block get executed when there is no exception inside the try block

try:
    odd=[1,3,5,7,9]
    res=(odd[3])

except IndexError:
    print("Index Out of Bound.")

except ZeroDivisionError:
    print("Error: denominator can't be zero")

else:
    print("required reciprocal is:",(1/(odd[2])))

finally:
    print("This will get executed even if there is no error in try block")
    print("=======================================================================")