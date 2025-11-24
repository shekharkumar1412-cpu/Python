# The continue statement is used to skip the current iteration of the loop 
            # and the control flow of the program goes to the next iteration.

for i in range(5):
    if i == 3:
        continue        # here when i equals 3 then this step will be skipped and 3 will not be outputted
    print(i)

print()


# program to print odd numbers from 1 to 10

num = 0
while num < 10:
    num += 1
    
    if (num % 2) == 0:
        continue

    print(num)