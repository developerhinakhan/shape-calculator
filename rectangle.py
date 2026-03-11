from shape import Shape

class Rectangle(Shape):
    def __init__(self,length,width):
        if length <= 0 or width <= 0:
            raise ValueError("Values must be positive")
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
        

rectangle = Rectangle(6,6)
print(rectangle.area())
