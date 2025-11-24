num={1,3,5,7,9,0}

# all(): Returns True if all elements of the set are true (or if the set is empty).
print(all(num))   


# any(): Returns True if any element of the set is true. If the set is empty, returns False.
print(any(num))

# enumerate(): Returns an enumerate object. 
# It contains the index and value for all the items of the set as a pair.
print(enumerate(num))

# len():  Returns the length (the number of items) in the set.
print(len(num))

# max():  Returns the largest item in the set.
print(max(num))

# min():  Returns the smallest item in the set.
print(min(num))

# sorted(): Returns a new sorted list from elements in the set(does not sort the set itself).
num1=sorted(num)
print(num1)

# sum():  Returns the sum of all elements in the set.
print(sum(num))