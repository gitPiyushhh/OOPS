from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def name(self):
        pass

class Triangle(Shape):
    
    ## // Triangle implements in its own way
    def name(self):
        print('I am triangle')

class Square(Shape):
    
    ## // Square implements in its own way
    def name(self):
        print('I am square')

o1 = Triangle()
o2 = Square()

o1.name()
o2.name()