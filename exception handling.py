#compile time error
#logical error
#runtime error
"""
a=5
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print("cannot" , e)
except Exception as e:
    print("error" , e)
finally:
    print("closed")
print("bye")"""

#multithreading
from threading import *
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(8):
            print("hello")
            sleep(0.1)

class hi(Thread):
    def run(self):
        for i in range(8):
            print("hi")
            sleep(0.1)

t1 = hello()
t2 = hi()
t1.start()
sleep(0.01)
t2.start()

t1.join()
t2.join()
print("bye")












