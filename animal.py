from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move (self):
        print("i can walk and run")
        
class lion(animal):
    def move (self):
        print("i can roar and attack")

class  snake(animal):
    def move (self):
        print("i crawl and can bite")
        
obj=human()
obj.move()
obj=lion()
obj.move()
obj=snake()        
obj.move()