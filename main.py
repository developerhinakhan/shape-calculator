from rectangle import Rectangle
from circle import Circle

# create shape objects
shapes = [
    Rectangle(5, 6),
    Circle(5)
]

# polymorphism in action
for shape in shapes:
    print(type(shape).__name__, "Area:", shape.area())