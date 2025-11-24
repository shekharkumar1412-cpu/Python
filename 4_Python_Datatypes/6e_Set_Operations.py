# We use the | operator or the union() method to perform the set union operation. 

set1={1,3,5}
set2={3,7,9,5}

print('Union of set1 and set2 using | operator:',set1|set2)
print('Union of set1 and set2 using using union() method:',set1.union(set2))
print('Union of set2 and set1 using using union() method:',set2.union(set1))


# We use & operator or the intersection() method to perform set intersection operation

print('Intersection of set1 and set2 using & operator:',set1&set2)
print('Intersection of set1 and set2 using intersection() method:',set1.intersection(set2))
print('Intersection of set2 and set1 using intersection() method:',set2.intersection(set1))


# We use the - operator or the difference() method to perform the difference between two sets.

print('Difference of set1 and set2 using - operator:', set1-set2)
print('Difference of set2 and set1 using - operator:', set2-set1)
print('Difference of set1 and set2 using difference() method:', set1.difference(set2))
print('Difference of set2 and set1 using difference() method:', set2.difference(set1))


# In Python, we use the ^ operator or the symmetric_difference() method
# to perform symmetric difference between two sets.
# (The symmetric difference between two sets A and B includes all elements of A and B without 
                        # the common elements.)


set1={1,3,5,7}
set2={2,4,5,7}
print('using ^:', set1 ^ set2)
print('using ^:', set2 ^ set1)
print('using symmetric_difference():', set1.symmetric_difference(set2)) 
print('using symmetric_difference():', set2.symmetric_difference(set1)) 

