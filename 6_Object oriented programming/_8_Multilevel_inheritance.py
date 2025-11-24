# we can also derive a class from a derived class as well this is known as multilevel inheritance


# superclas Animal
class Animal:
    def Superclass_Animal_method(self):
        print("Animals are found on earth")


# level_1 derived class from the superclass Animal
class Humans(Animal):
    def derived_class_level_1_method(self):
        print("Humans are most intelligent animal")

# level_2 derived class from thwe class level_1 derived class
class Good_persons(Humans):
    def derived_class_level_2_method(self):
        print("Good humans helps everyone")

# creating an object of class Good_persons 
Ram=Good_persons()
Ram.Superclass_Animal_method()
Ram.derived_class_level_1_method()
Ram.derived_class_level_2_method()
