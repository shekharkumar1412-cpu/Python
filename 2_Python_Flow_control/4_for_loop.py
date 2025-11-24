# In Python, the for loop is used to run a block of code for a certain number of times. 
# It is used to iterate over any sequences such as list, tuple, string, etc.

                                # Syntax


# for value in sequence:
    # statement(s)


languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for la in languages:
    print(la)

else:
    print("No more language is left in list language ")
    print()
    print()


            # for loop with python range()
value=range(1,4)
for i in value:
    print(i)




                # Example 3
print()
print("printing each character of a string using for loop")
text='python'

for i in text:
    print(i)