class Polygon:

    # constuctor function to initialize the number of sides
    def __init__(self, no_of_sides):

        # N is the total number of the sides of tye polygon
        self.N = no_of_sides

        # sides(list type) is a data attributes to store no. of sides (n) and magnitude of each side
        self.sides = [0 for i in range(self.N)] 

    # method to take in the magnitude of each side
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.N)]

    # method to display the side lengths
    def dispSides(self):
        for i in range(self.N):
            print("Side",i+1,"is",self.sides[i])

#---------------------------------------------------------------------------------------------------

# creating a subclass triangle from the superclass polygon 
class Triangle(Polygon):
     # Initializing the number of sides of the triangle to 3 by 
      # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# ---------------------------------------------------------------------------------------------

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()
