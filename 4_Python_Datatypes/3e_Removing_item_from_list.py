#  1.) Using del()   : It removes one or more items from a list.

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']

# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']

# delete first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)


#   2.)  Using remove()    : Deletes a list item

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']

# remove 'Python' from the list
languages.remove('Python')
languages.remove('R')

print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust']

num =[1,3,5,7,9]
num.remove(1)
num.remove(num[2]) # remove the element present at index 2 i.e 7
print(num)




