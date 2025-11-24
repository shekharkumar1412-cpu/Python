# We use the discard() method to remove the specified element from a set.

languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)


num={1,2,3,7,'3','1'}
print(num)
num.discard(1)
print(num)
num.discard('1')
print(num)