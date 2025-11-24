# It is a concise and elegant way to create lists.
# A list comprehension consists of an expression followed 
# by the for statement inside square brackets.



# making a list with each item being increasing by power of 2.
numbers = [number*number for number in range(1, 6)]

print(numbers)  

                
                # method 2
numbers = []

for x in range(1, 6):
    numbers.append(x * x)

print(numbers)