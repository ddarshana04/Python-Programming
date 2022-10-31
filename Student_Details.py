class Student_Details:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def E_Marks (self):
        for i in range(5):
            m = int(input('Enter marks of subject %d: ' %(i+1)))
            self.marks.append(m)
    def D_Marks (self):
        print('Student name: ' + self.name)
        print('Student marks: ' + str(self.marks))

s1 = Student_Details("Darshana")
s1.E_Marks()
s1.D_Marks()

