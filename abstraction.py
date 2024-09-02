from abc import ABC,abstractmethod
class absclass(ABC):
    def print(self,x):
        print(x)
    @abstractmethod 
    def task(self):
        print("im am from parent classmethod")
        
class child(absclass):
    def task(self):
        print ("im from child class")
obj=child()
obj.task()
obj.print(9)            
    