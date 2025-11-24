# A class can be derived from more than one superclass in Python. This is called multiple inheritance.

# For example, A class Bat is derived from superclasses Mammal and WingedAnimal. 
# It makes sense because bat is a mammal as well as a winged animal.


# superclass 1
class Mammal:
    def Mammal_info(self):
        print("Mammals can give direct birth.")

# superclass 2
class WingedAnimal:
    def Winged_animal_info(self):
        print("Winged animals can flap.")

# superclass 3
class CBA:
    def CBA_info(self):
        print("This is cold blooded animal")
        

# Derived class from the three above Superclasses
class Bat(CBA,WingedAnimal,Mammal,):
    pass

# create an object of Bat class
b1 = Bat()

b1.Mammal_info()            # accessing superclass 1 method
b1.Winged_animal_info()     # accessing superclass 2 method
b1.CBA_info()               # accessing superclass 3 method\

