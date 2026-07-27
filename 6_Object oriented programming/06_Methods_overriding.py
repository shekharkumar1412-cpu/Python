# When we are having same methods defined in both superclass as well as in the subclass then the method
# defined in the subclass overrides the method of the superclass

class Animal:
    name=''

    def Sleep(self):
        print('I can sleep!')

class person(Animal):
    def Sleep(self):
        super().Sleep()      # this allows to access the superclass Sleep method from here
        print("They sleep on beds.")

Ram=person()
Ram.Sleep()       # prints the Sleep defined in subclass 

