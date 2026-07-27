# Earlier we assigned a default value to a class attribute,

class Bike:
    name = ""
...
# create object
bike1 = Bike()


# However, we can also initialize values using the constructors. \
# For example,

class Bike:
    # constructor function    
    def __init__(bike ,name = "",mileage = 0):
        bike.name = name     # Here, __init__() is the constructor function that 
                                  #  is called whenever a new object of that class is instantiated.
        bike.mileage=mileage

bike1 = Bike()  # Here, nothing is passed to the name parameter of __init__().
print(bike1.name)
print(bike1.mileage)



# If we use a constructor to initialize values inside a class, 
# we need to pass the corresponding value during the object creation of the class.

bike2 = Bike("Mountain Bike",90)   # Here, "Mountain Bike" is passed to the name parameter of __init__().
print(bike2.name)
print(bike2.mileage)
