# Indexing is used to access elements of a tuple similar to list
# index must be an integer
# To access nested tuple we use nested indexing



letters =  ("p", "r", "o", "g", "r", "a", "m", "i", "z")
# index    : 0    1    2    3    4    5    6    7    8
# -ve index: -9   -8   -7   -6   -5   -4   -3   -2   -1

num=    (  1,  3.5, 'hi', (   11,      21,       31     ),   7)
# index:  [0]  [1]   [2]    [3][0]   [3][1]    [3][2]       [4]
#-ve index:-5   -4   -3    [-2][-3]  [-2][-2]  [-2][-1]     [-1]


print(num[0])
print(num[1])
print(num[3][1])      
print(num[3][2])
print(num[-2][-2])