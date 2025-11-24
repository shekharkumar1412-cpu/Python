                # A program to write a table of a number
n=int(input("Enter a number:"))

for count in range(1,11):
    print(n,"x",count,'=',n*count)



print()
print('Table of {} is:'.format(n))
count1=1
while count1 < 11:
    print(n,'x',count1,'=',n*count1)
    count1+=1


                    # A program to find the sum of first n natural numbers
print()
sum=0
N=int(input("Enter the value of N:"))
for i in range(1,N+1):
    sum=sum+i

print("The sum of first {} digits is:".format(N),sum)
