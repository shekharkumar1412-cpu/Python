# A set is a collection of unqiue data(i.e elements of a set can't be duplicate) (eg. student-IDs)


# creating a set
# In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.
# Elements of a set can be of datatypes: integer, float, tuple, string etc.
# But a set cannot have mutable elements like lists, sets or dictionaries as its elements.


# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# To make a set without any elements, we use the set() function without any argument.


empty_set = set()         # creates an empty set

empty_dictionary = { }    # creates an empty dictionary


# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))
