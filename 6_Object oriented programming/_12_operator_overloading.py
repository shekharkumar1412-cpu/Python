# In Python, we can change the way a operators work for user-defined types.
# This feature in Python that allows the same operator to have different meaning 
# according to the context is called operator overloading.


# ------------------------ SPECIAL FUNCTIONS -----------------------------

# Class functions that begin with double underscore __ are called special functions in Python.
# They are called "double underscore" functions because they have a double underscore as
# prefix and suffix, such as __init__() or __add__().

#   Function	    Description
# __init__()	    initialize the attributes of the object
# __str__()     	returns a string representation of the object
# __len__()     	returns the length of the object
# __add__()	        adds two objects
# __call__()    	call objects of the class like a normal function
 
 
 
 
# ---------------- Overloading '+' operator -----------------------------------

# To overload the + operator, we will need to implement __add__() function in the class.
# it is more sensible to return the Point object of the coordinate sum.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(1, 2)
p2 = Point(2, 3)

p=(p1+p2)
print(p)    # Here when we use p1 + p2, Python calls p1.__add__(p2) which in turn is Point.__add__(p1,p2).
                    #  After this, the addition operation is carried out the way we specified.

# Output: (3,5)



# -------------------------------Overloading < operator to compare two objects------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # overload < operator
    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Alice", 20)
p2 = Person("Bob", 30)

print(p1 < p2)  # prints True
print(p2 < p1)  # prints False

# Here, __lt__() overloads the < operator to compare the age attribute of two objects.
