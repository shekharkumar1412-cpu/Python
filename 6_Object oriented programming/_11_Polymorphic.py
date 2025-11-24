# It simply means more than one form.
# i.e the same entity (method or operator or object) can perform different
#  operations in different scenarios.


# Superclass
class Polygon:
    # method to render a shape
    def render(self):
        print("Rendering Polygon...")

#Subclass 1
class Square(Polygon):
    # renders Square
    def render(self):
        print("Rendering Square...")

# Subclass 2
class Circle(Polygon):
    # renders circle
    def render(self):
        print("Rendering Circle...")
    
# create an object of Square
s1 = Square()
s1.render()

# create an object of Circle
c1 = Circle()
c1.render()

# The render() method(whose function is to render shapes) are
#  behaveing differently in different classes. Or, we can say render() is polymorphic.