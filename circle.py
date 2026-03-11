from shape import Shape
import math

class Circle(Shape):
    def __init__(self,radius):        
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
            
        
    def area(self):
        return math.pi * self.radius ** 2
        
    

c = Circle(6)
print(c.area())
