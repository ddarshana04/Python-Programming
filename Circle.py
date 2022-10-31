class Circle:
    PI = 3.1415
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 2*Circle.PI*self.radius*self.radius

C = Circle(7.5)
print("Area is :" + C.area())
print("Circumference = "+C.circumference())
