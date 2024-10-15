#duck typing
"""class pycharm:
    def execute(self):
        print("compiling")
        print("running")
class editor:
    def execute(self):
        print("spell check")
        print("compiling")
class laptop:
    def code(self,ide):
        ide.execute()
ide = editor()

lap1 = laptop()
lap1.code(ide)"""


#method overloading
"""class student:
    def __init__(self):
        pass
    def sum(self,a = None, b = None,c=None):
        s=0
        if a != None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1 = student()
print(s1.sum(6,3,))"""

#method overriding

class a:
    def show(self):
        print("in a show")
class b(a):
    def show(self):
        print("in b show")

a1 = b()
a1.show()