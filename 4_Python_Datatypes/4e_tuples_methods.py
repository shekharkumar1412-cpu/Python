# In python tuples only count() and index() methods are applicable

num=(1,2,3,4,1,5,6,1,7,6)


# count() returns the number of times an elements is showed in the tuple
print(num.count(1))  #  prints 3
print(num.count(5))  #  prints 1
print(num.count(6))  #  prints 2


# index() return the first occurence index of item/element
print('printing index using method index():')
print(num.index(1))
print(num.index(6))