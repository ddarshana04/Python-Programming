class Triangle: 
    def__init__(self, a, b, c):
    self.a = a 
    self.b = b
    self.c= c
    def area(self): 
        s = (self.a + self.b + self.c)/2 
        return((s*(s-self.a) * (s-self.b) * (s-self.c) ** 0.5))
        a = input("Enter 1st side: ") 
        b = input("Enter 2nd side: ") 
        c = input("Enter 3rd side: ") 
        print("area: ")