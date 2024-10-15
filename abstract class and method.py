from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
class programmer(laptop):
    def work(self,com):
        print("solving prob")
com1 = laptop()
com1.process()
prog1 = programmer()
prog1.work(com1)
