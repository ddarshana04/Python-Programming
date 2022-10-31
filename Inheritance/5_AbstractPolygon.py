class Polygon:
    def __init__(self, n):
        self.number_of_sides = n

    def print_num_sides(self):
        print("There are " + str(self.number_of_sides) + " sides.")

class Rectangle(Polygon):
    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = lengths_of_sides  

    def get_area(self):
        x, y = self.lenghts_of_sides
        return x * y

class Triangle(Polygon):
    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 3)
        self.lengths_of_sides = lengths_of_sides  

    def get_area(self):
        a, b, c = self.lengths_of_sides
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5

class Square(Polygon):
    def __init__(self, lengths_of_sides):
        Polygon.__init__(self, 4)
        self.lengths_of_sides = [lengths_of_sides]  

    def get_area(self):
        x = self.lenghts_of_sides[0]
        return x * x

