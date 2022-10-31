class Compare:
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2 = s2
        def __cmp__ (self):
            if self.s1 == self.s2:
                print("Same strings")
            else:
                print("Strings not equal")

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")
obj = Compare(s1, s2)                
