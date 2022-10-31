class Family:
    def _init_(self, srname):
        self.surname = srname
    
class Father(Family):
    def _init_(self, srname, frname, occupation):
        self.surname = srname
        self.father_name = frname
        self.occupation = occupation

class Mother(Family):
    def _init_(self, srname, mname, age):
        self.surname = srname
        self.mother_name = mname
        self.age = age

class Child(Father, Mother):
    def _init_(self, srname, frname, occupation, mname, age, chname):
        self.surname = srname
        self.father_name = frname
        self.occupation = occupation
        self.mother_name = mname
        self.age = age
        self.child_name = chname
    
    def display(self):
        print("Name: %s" %(self.child_name))
        print("Surname: %s" %(self.surname))
        print("Father's name: %s" %(self.father_name))
        print("Occupation: %s" %(self.occupation))
        print("Mother's name: %s" %(self.mother_name))
        print("Mother's age: %d" %(self.age))

child1 = Child("Chola", "Raja raja chola", "King", "Tribhuvana", 42, "Rajendra chola")
child1.display()