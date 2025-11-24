                                    # superclass1
class Mammal:
    def info(self):
        print("Mammals can give direct birth.")

                                    
                                    # superclass 2
class WingedAnimal:
    def info(self):
        print("Winged animals can flap.")

                                    
                                    # superclass 3
class CBA:
    def info(self):
        print("This is cold blooded animal")
        

# subclass derived from all three superclasses
class Bat(CBA,WingedAnimal,Mammal,):
    pass

# create an object of Bat class
b1 = Bat()

# accesing info() method which is present in all three superclasses
b1.info()

# here python will use Method resolution order(MRO) to determine method of which superclass to be called
# in this case leftnmost superclass's method will be called