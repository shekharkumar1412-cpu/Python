# An object is simply a collection of data (variables) and methods (functions).
#  Similarly, a class is a blueprint for that object.


# For example We can think of the class as a sketch (prototype) of a house
# which contains all the details about the floors, doors, windows, etc. 
# Based on these descriptions we build the house (object.)
# Since many houses can be made from the same description, we can create many objects from a class





# creating a class named Person using the keyword class

class Person:
    name=''   # attribute of the class Person here with default value as empty string
    age=0     # attribute of the class Person here with default value 0


# Creatring an object named P1 for the class Person
P1=Person()

# Accesing the attributes of the class Person using dot opereator and assigning values to those attributes
P1.name='Ram'
P1.age=25

# creating second object of the same class named Person
P2=Person()

# accesing the attributes of the class person for the second Object P2 using dot operator
# and assigning new values to those attributes 

P2.name='Shyam'
P2.age=66


# printing trhe values:

print(f"Age of the person {P1.name} is {P1.age}")
print("Age of the person",P2.name,'is',P2.age)