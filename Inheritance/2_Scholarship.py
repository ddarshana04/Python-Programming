class student:
    def _init_(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)

class grade(student):
    def _init_(self, id, name, cgpa):
        super()._init_(id, name)
        self.cgpa = cgpa

    def display(self):
        super().display()
        print("CGPA:", self.cgpa)

class scholarship(grade):
    def _init_(self, id, name, cgpa):
        super()._init_(id, name, cgpa)

    def display(self):
        super().display()
        if self.cgpa > 9:
            print("Scholarship: Rs.10,000/-")
        elif self.cgpa > 8:
            print("Scholarship: Rs.7500/-")
        elif self.cgpa > 7.5:
            print("Scholarship: Rs.5000/-")

s1 = scholarship(20020, "Darshana", 9.8)
s1.display()