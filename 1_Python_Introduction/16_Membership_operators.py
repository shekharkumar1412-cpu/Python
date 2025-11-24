# In Python, in and not in are the membership operators. 
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
# In a dictionary we can only test for presence of key, not the value.


x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True (due to case-sensitivity)

# check if '1' key is present in y
print(1 in y)  # prints True (since 1 is the kry is the dictionary)

# check if 'a' key is present in y
print('a' in y)  # prints False (since a is the value in the dictionary)