# Add Items to a Set in Python

# using the add() method to add an item to a set.

numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Final Set after adding an element:', numbers) 


# The update() method is used to update the set with items of 
# other collection types (lists, tuples, sets, etc).

companies = {'Microsoft', 'HP'}
tech_companies = ['apple', 'google', 'apple']
com= ('dell','asus')
companies.update(tech_companies)
print(companies)
print()
companies.update(com)
print(companies)
