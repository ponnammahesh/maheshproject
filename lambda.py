"""from functools import reduce

nums = [45,3,64,77,54,74,436,59]

evens = list(filter(lambda n: n%2==0,nums ))

double = list(map(lambda n: n*2, evens))

sum = reduce(lambda a,b: a+b,double)

print(evens, double, sum, sep='\n')"""

class student:
    school = "telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is rkejfb ekjrb")
#object
s1 = student(34,67,32)
s2 = student(89,32,12)

print(student.getschool())
student.info()

