#  1.) Using append() : This  method adds an item at the end of the list.

numbers = [21, 34, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(32)
print("After Append:", numbers)


#  2.) Using extend() : This method is used to add all items of one list to another.

prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)

# adding all elements of even_numbers to prime_numbers.
prime_numbers.extend(even_numbers)

print("List after append:", prime_numbers) 

# adding all elements of updated prime_numbers to even_numbers
even_numbers.extend(prime_numbers)
print('list after appending:',even_numbers)



