#Inheritance allows us to create a new class from an existing class.

# The new class that is created is known as subclass (child or derived class) and 
# existing class from which the child class is derived is known as superclass (parent or base class).



# creating a Superclass/parent class named Animal
class Animal: 
    name=''
    type=''

    # methods in the superclass Animal
    def eat(self):      
        print('I can eat')

    def sleep(self):
        print("I can sleep")


# creating a subclass (named Dog) of the superclass Animal
class Dog(Animal):
    # method of the Subclass Dog
    def bark(self):
        print("I can bark!")

#  creating an object of the subclass Dog()

dog1=Dog()

#  accessing the attributes/methods of the superclass Animal for object dog1
dog1.name='Motu'
dog1.type='Pet'
print(dog1.name)
print(dog1.type)
dog1.eat()
dog1.sleep()

# Accesing the attribute of the subclass Dog(Animal)
dog1.bark()