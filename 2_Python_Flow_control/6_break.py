# The break statement is used to terminate the loop immediately when it is encountered.
# The break statement is almost always used with decision-making statements.

for i in range(5):
    if i == 3:              # when i equals 3 break will terminate the for loop
        break
    print(i)

print()
print()




# program to find first 5 multiples of 6

i = 1

while (i<=10):
    print('6 * ',(i), '=',6 * i)

    if i >= 5:                  # when i equals 5 here break will terminate the while loop
        break
    
    i = i + 1