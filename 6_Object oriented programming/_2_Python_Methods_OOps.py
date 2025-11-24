# We can also define a function inside a Python class. 
# A Python Function defined inside a class is called a method

# create a class
class Room:
    length = 0.0
    breadth = 0.0
    
    # method to calculate area(i.e function defined to calucalte area inside the class)
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

# create object of Room class
study_room = Room()

# assign values to all the attributes 
study_room.length = int(input("Enter the length of the room        :"))
study_room.breadth = int(input("Enter the breaqdth of the study_room:"))

# access method inside class
study_room.calculate_area()