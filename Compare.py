class Compare:
    def __init__(self,s):
        self.s = s
    def __cmp__(self,st):
        if self.s < st.s:
            print("String 1 is greater")
        elif(self.s > st.s):
            print("String 2 is greater")
        else:
            print("Equal length")

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")            


          