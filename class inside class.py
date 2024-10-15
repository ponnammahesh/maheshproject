"""class student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name , self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student('mahesh',5) #these are objects
s2 = student('satish',4)

s1.show()
#lap1 = student.laptop()
"""

class a:
    def mahesh(self):
        print('in a init')
    def feature1(self):
        print("feature 1-a working")
    def feature2(self):
        print("feature 2 working")
class b:
    def __init__(self):
        print('in b init')
    def feature1(self):
        print("feature 1-b working")
    def feature4(self):
        print("feature 4 working")

class c(a,b):
    def __init__(self):
        super().__init__()
        print('in c init')

    def feat(self):
        super().feature2()
a1 = a()
a1.mahesh()
