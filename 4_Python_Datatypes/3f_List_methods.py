num=[1,3,1,3,5,1,7]


# sorting the list in increasing/decreasing order
num.sort()
print(num)



# removing first element from the first ocuurence index
num.remove(1)
print(num)



# counting the number of times an item appeared in the list
print(num.count(1))
print(num.count(3))



# getting the index of first ocuuerence of 1 and 7
print('index of 1 is:',num.index(1))
print(num.index(7))






# Reversing the list
num.reverse()
print(num)



# copying a list

num1=num.copy()
print(num1)


# Removing all items from the list 
num.clear()
print(num)



# inserting element at specific index

num.insert(0,12)
print(num)
num.insert(0,13)
print(num)
num.insert(1,121)
print(num)
num.insert(0,12)
print(num)